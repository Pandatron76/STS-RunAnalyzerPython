import configparser


def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


def read_target_path(config):
    target_path = config['DIRECTORIES']['TargetPath']
    return target_path


def read_config_boolean(config, section, value):
    return config.getboolean(section, value)


def config_option_to_list(config, section, option):
    config_list = [element.strip(' -') for element in config[section][option].split(',')]
    return config_list