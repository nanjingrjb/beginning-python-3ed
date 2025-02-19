from configparser import ConfigParser

CONFIGFILE = "listing19_1.cfg"

config = ConfigParser()
# Read the configuration file:
cont=config.read(CONFIGFILE)
print(config)

# Print out an initial greeting;
# 'messages' is the section to look in:
print(config['messages'].get('greeting'))

# Read in the radius, using a question from the config file:
radius = float(input(config['messages'].get('question') + ' '))

# Print a result message from the config file;
# end with a space to stay on same line:
print(config['messages'].get('result_message'), end=' ')

# getfloat() converts the config value to a float:
print(config['numbers'].getfloat('pi') * radius**2)
