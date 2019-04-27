#判断合法用户,模拟用户登录窗口

username = input("username: ")
password = input("password: ")
if username == "zl" and password == "123456":
    print('Login successful')
else:
    print('Login incorrect')