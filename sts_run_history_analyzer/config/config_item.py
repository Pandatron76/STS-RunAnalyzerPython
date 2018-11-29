# Stores details about config settings that can be printed

from config import config_helper


class ConfigItem:

    def __init__(self, config_item_name):
        self.config_item_name = config_item_name
        self.console_message = ''
        self.priority = 0
        self.section = ''


def config_item_list(config, section_name):
    sect_dict = config_helper.section_to_bool_dict(config, section_name)
    printable_config_items = []

    for option, value in sect_dict.items():
        if value is True:
            config_item = ConfigItem(option)
            config_item.section = section_name
            printable_config_items.append(config_item)

    if len(printable_config_items) == 0:
        print("\n***** Note: The %s section has no flags set to True. *****\n" % section_name)

    return printable_config_items


def config_list():
    config = config_helper.read_config('config\\report_config.ini')
    config_all_runs_list = config_helper.section_to_set(config, 'PRINT_INDIVIDUAL_RUN')
    config_individual_run_list = config_helper.section_to_set(config, 'PRINT_ALL_RUNS')

    combined_set = config_all_runs_list | config_individual_run_list

    return combined_set


def list_to_enumerated_dict(string_list):
    return {k: v for v, k in enumerate(string_list)}


def prioritize_config_items(config_item_print_single, config_item_print_all):
    combined_config_items = []

    if len(config_item_print_single) >= 1:
        combined_config_items += config_item_print_single

    if len(config_item_print_all) >= 1:
        combined_config_items += config_item_print_all

    for config_item in combined_config_items:
        config_item.priority = list_to_enumerated_dict(config_list()).get(config_item.config_item_name)

    # For Debugging Purposes to determine priority
    # for config_item in combined_config_items:
         # print(config_item.config_item_name, config_item.priority)

    if len(config_item_print_single) > 1:
        print("\n")

    return sorted(combined_config_items, key=lambda x: x.priority, reverse=False)
