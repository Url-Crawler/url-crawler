from configobj import ConfigObj

def get_value_from_name(name):
    config_file = 'develop.conf'
    config = ConfigObj(config_file)
    return config.get(name)


