import configparser


def read_config(config_file):
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(config_file)
    return config


def read_target_path(config):
    target_path = config['DIRECTORIES']['TargetPath']
    return target_path


def section_to_bool_dict(config, section_name):
    section_dict = {}
    if config.has_section(section_name) is True:
        for option_boolean in config.items(section_name):
            (option, include) = option_boolean
            section_dict[option] = string_to_bool(include)
    else:
        print("Name: %s" % config.has_section(section_name))
        print("\nSection specified (%s) does not have a section in the config." % section_name)
        print("Script will continue to execute but results may not be accurate")
    return section_dict


def section_to_set(config, section_name):
    config_section_list = set()

    if config.has_section(section_name):
        for key, value in config.items(section_name):
            if string_to_bool(value):
                config_section_list.add(key)

    return config_section_list


def string_to_bool(string_boolean):
    if string_boolean == "True":
        return True
    elif string_boolean == "False":
        return False
    else:
        print("Issue with string_to_bool function. Passed value %s" % string_boolean)
        return None
