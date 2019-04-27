# vim login2-v3.py
#!/usr/bin/env python3

import getpass          #调用模块中的函数在命令行窗口无回显输入密码
username = input('username: ')
password = getpass.getpass('password: ')

if username = 'zl' and password = '123456':
    print('\033[32;1mLogin successful!\033[0m')     #绿色粗体显示
else:
    print('\033[31;1mLogin incorrect!\033[0m')      #红色粗体显示