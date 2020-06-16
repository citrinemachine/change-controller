import configparser
from pathlib import Path
import os



#roaming_dir = os.getenv('APPDATA')
#path_string = roaming_dir + r'\yuzu\config\qt-config.ini'
path_string = r'C:\Users\apple\AppData\Roaming\yuzu\config\qt-config.ini'

yuzu = Path(path_string)

config = configparser.ConfigParser()
config.read(yuzu)


print(config.sections())


print(path_string)

controls_data = config['Controls']

print(*controls_data.items(), sep="\n")

