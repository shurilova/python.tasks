Задача 1. Информация о системе. Нужно собрать информацию об операционной системе и версии пайтона. Для этого запустим код ниже из файла main.py. 

````python
import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
````
