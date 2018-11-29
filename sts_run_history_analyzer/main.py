import sys
import os
import json

import all_runs.store_console_messages
from individual_runs import store_console_messages

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer/config"))
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer/helpers"))
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer/report"))
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer/run_data"))
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer/store_console_messages"))

from config import check_config  # noqa
from config import config_helper  # noqa
from config import config_item  # noqa

from datetime import datetime # noqa

from report import report_summary  # noqa

from run_data import sts_run_data  # noqa


def character_folder_name(path):
    return path.rsplit('\\', 1)[-1]


# Key will be character and the value is  and will be populated with sts_run_data objects
def create_run_set_dict(include_characters):
    config_section_dict_x = {}
    for character in include_characters:
        config_section_dict_x.update({character.upper(): []})
    return config_section_dict_x


# Responsible for populating the sts_run_data objects for the value
def add_to_run_set(run_set_dict, current_run, character_name_from_path):
    for character in run_set_dict.keys():
        if character == character_name_from_path:
            run_set_dict[character].append(current_run)
    return run_set_dict


def create_character_paths(target_path, include_characters):
    target_path = target_path.strip('\"').strip('\'')
    return [target_path + '\\' + character for character in os.listdir(target_path)
            if character in include_characters]


def main():
    # Declarations
    script_start_time = datetime.now()
    parsed_config = config_helper.read_config('config\\report_config.ini')
    target_path = config_helper.read_target_path(parsed_config)
    include_characters = \
        [element.strip(' -') for element in parsed_config['DIRECTORIES']['CharactersToInclude'].split(',')]
    character_paths = create_character_paths(target_path, include_characters)
    run_set_dict = create_run_set_dict(include_characters)

    # Holds a collection of all Slay the Spire runs
    run_set = set([])
    character_timestamp_dict = {}
    config_item_print_all = config_item.config_item_list(parsed_config, 'PRINT_ALL_RUNS')
    config_item_print_individual = config_item.config_item_list(parsed_config, 'PRINT_INDIVIDUAL_RUN')
    sorted_print_all_runs = []

    # Inform the user what path the script is pointing to and what characters to report information on
    print("\nInformation from report_config.ini file...")
    print("  TargetPath specified:\n    %s" % target_path)
    print("  CharactersToInclude:\n    %s" % include_characters)

    # Close out the script if the user did not include at least one file
    if len(include_characters) == 1 and '' in include_characters:
        print("\nNo characters have been specified in the config for 'CharactersToInclude'")
        print("Exiting script")
        exit()

    # Close out the script if the user supplies a character that does not exist
    if len(character_paths) == 0:
        print("\nThe TargetPath (%s) does not include any of the character folders specified in the report_config.ini"
              % target_path)
        print("Please check the folder location: %s" % target_path)
        print("Exiting script")
        exit()

    # Cycle through all the characters to include in the report
    for path in character_paths:
        character_start_time = datetime.now()
        # Retrieve the folder name for the character from the full_path
        character_name_from_path = character_folder_name(path)

        # Provide a header for the character_chosen that will be reported on
        if len(config_item_print_all) > 0 or len(config_item_print_individual) > 0:
            print('\n')
            print('***** %s Data: *****' % character_name_from_path)
        # Close out the script if no config flags set to true
        else:
            print("Stopping script execution...")
            exit(0)

        print("Processing %s files..." % len(os.listdir(path)))

        # Cycle through all the files in each character folder
        if len(os.listdir(path)) > 0:
            for file in os.listdir(path):
                current_run = sts_run_data.STSRunData(file)

                with open(str(path) + '\\' + str(file), 'r') as f:
                    parsed = json.load(f)

                    # Only supply the file name if at least one config flag for 'REPORT_SINGLE_RUNS' is true
                    if len(config_item_print_individual) > 0:
                        print("  File Name: %s" % current_run.id)

                    # Determine which items will be included based on the report_config.ini file
                    config_item_print_single = \
                        store_console_messages.store_console_messages(current_run, parsed, config_item_print_individual)

                    # Store the values of an individual run that are needed for any items in the print_all_runs section
                    config_item_print_all = check_config.all_runs_section(current_run, parsed, config_item_print_all)

                    # Prioritized and sort printable_config_items
                    sorted_print_all_runs = \
                        config_item.prioritize_config_items(config_item_print_single, config_item_print_all)

                    # Only report on the individual runs if there is at least one config flag is true
                    if len(config_item_print_individual) > 0:
                        # Print the non-json list data
                        report_summary.individual_run(config_item_print_single)

                    # Add each current_run object to its respective character set
                    add_to_run_set(run_set_dict, current_run, character_name_from_path)
                    run_set.add(current_run)

        else:
            print("There are no .run_data files for character %s" % character_name_from_path)

        # Store the console messages for any options set to True in the print all runs section
        all_runs.store_console_messages.store_console_messages(run_set, sorted_print_all_runs)

        # Print information about all runs based on config
        for character, current_run_set in run_set_dict.items():
            if character == character_name_from_path:
                report_summary.all_runs(sorted_print_all_runs)
                character_timestamp_dict[character] = [(datetime.now() - character_start_time), len(os.listdir(path))]
                character_start_time = datetime.now()

    # @TODO: Make this section less gross and move it to report_summary
    print('**************************************************')
    print('********************Summary***********************')
    print('**************************************************')
    for character, processed_data in character_timestamp_dict.items():
        # count = 0
        print("\n***** %s ******\n" % character)
        for data in processed_data:
            # print(count)
            # print(data, '||', type(data), '||', isinstance(data, int))
            # count += 1
            if isinstance(int, type(data)) is False:
                print("Number of files processed: %s" % data)
            else:
                print("Time to process files: %s\n" % data)

    print('**************************************************')
    print("\nTotal files processed: %s" % len(run_set))
    print("Total Script Execution time: %s\n" % (datetime.now() - script_start_time))
    print('**************************************************')


main()
