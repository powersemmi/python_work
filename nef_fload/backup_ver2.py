import os
import time


def parse(text):

    text = text.replace(' ', '_')
    text = text.replace('~', '_')
    text = text.replace('#', '_')
    text = text.replace('%', '_')
    text = text.replace('&', '_')
    text = text.replace('*', '`')
    text = text.replace('{', '[')
    text = text.replace('}', ']')
    text = text.replace('<', '_')
    text = text.replace('>', '_')
    text = text.replace(':', ';')
    text = text.replace('?', '_')
    text = text.replace('\\', '_')
    text = text.replace('/', '_')
    text = text.replace('+', '_')
    text = text.replace('|', '_')

    return text


# Files for BackUp
source = [r"C:\Users\Пуфик\Desktop\python_work"]

# Target float
target_dir = r"C:\Users\Пуфик\Desktop\BackUp"

# Name floater
today = target_dir + os.sep + time.strftime("%d.%m.%Y")

# Name file
now = time.strftime('%I;%M%p')

comment = input('Enter comment there (max 20 symbols) -->')
if len(comment) <= 20:
    comment = parse(comment)
else:
    comment = input('Enter comment there (max 20 symbols) -->')


# Create catalog if it does not exist
if not os.path.exists(today):
    os.mkdir(today)
    print('\nCreate catalog\n')
else:
    print('\nThe directory has already been created, the backup will be moved there\n')

# Name for zip-file
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Create BackUp
if os.system(zip_command) == 0:
    print('Success\nTarget file:\n', target)
else:
    print('Error')

