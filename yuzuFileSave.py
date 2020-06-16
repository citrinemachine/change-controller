"""
Save
Load
"""


from pathlib import Path
import os
import time
from shutil import copyfile 


##VARS##
roaming_dir = os.getenv('APPDATA')
yuzu_dir = roaming_dir + '\\yuzu\\config\\'
control_cache = yuzu_dir + 'control_cache'
path_string = yuzu_dir + 'qt-config.ini'


def save_controls():
    controller_name = ''
    while controller_name == '':
        controller_name = input('What is the name of this controler profile?')
    p = Path(control_cache)
    p.mkdir(exist_ok=True)
    src = path_string
    dst = control_cache + '\\' + controller_name + '.ini'
    copyfile(src, dst)
    # if controller_name is True:
    #     new_name = controller_name + '.ini'
    #     os.rename('qt-config.ini', new_name)
    # else:
    #     print("Please name controller profile")

def list_controllers():
    try:
        enteries = os.listdir(control_cache)
        #print([entery for entery in enteries])
        for a, b in enumerate(enteries, 1):
            print(f'{a}  :  {b}')
    except:
        print('Missing control cache.  Have you saved profiles?')

    
        #print '{} {}'.format(a, b)

def select_controller():
    number = ''
    while type(number) is not int: # isinstance(number, int)
        try:
            number = int(input('Which controller do you want?'))
        except:
            print('Type a number')
    enteries = os.listdir(control_cache)
    selection = enteries[number-1]
    return selection

##copy from cache to config and rename
def load_controller():
    controller_selection = select_controller()
    controller_string = control_cache + '\\' + controller_selection
    controller_string = controller_string.split('.')
    controller_string = controller_string[0]
    try:
        src = controller_selection
        dst = yuzu_dir
        copyfile(src, dst)
        os.remove(path_string)
        os.rename(controller_string, 'qt-config.ini')
    except NameError:
        print("There is a name error")
    except:
        print("There is something else wrong")

def backup_config():
    src = path_string
    dst = control_cache + '\\BACKUP_qtconfig.ini'
    copyfile(src, dst)
    print('Configuration backed up')

while True:
    print('OPTIONS')
    print('1.) Save Controller Configs \n'+
            '2.) See list of Saved Configs \n'+
            '3.) Load configs \n'+
            '4.) Backup Config \n'
            '5.) Exit')
    try:
        option = int(input('What do you want to do (Select Number)'))  
        if option == 1:
            save_controls() 
        elif option == 2:
            list_controllers()
            input('Press enter')
            os.system("cls")
        elif option == 3:
            load_controller()
        elif option == 4:
            backup_config()
        elif option == 5:
            break
        else:
            print('Choose an Option') 
    except ValueError:
        print('Choose a number')

    