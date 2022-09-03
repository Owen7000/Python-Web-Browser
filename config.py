import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'Default_URL': 'https://google.com'}

with open('MainConfig.ini', 'w') as configfile:
    config.write(configfile)