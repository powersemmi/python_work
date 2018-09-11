import os
import time

source = ['"C:\\Users\\Пуфик\\Desktop\\python_work"']
target_dir = 'C:\\Users\\Пуфик\\Desktop\\BackUp'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S')
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Done', target)
else:
    print('Error')
