#getpass模块中的getpass方法，隐藏敏感的密码
import getpass          #调用改函数可以在命令行窗口里面无回显输入密码

username = input('username: ')
password = getpass.getpass('password: ')

if username == 'zl' and password == '123456':
    print('\033[32;lmLogin successful!\033[0m')         #绿色粗体显示
else:
    print('\033[31;lmLogin incorrect!\033[0m')           #红色粗体显示