# vim grade.py
#!/usr/bin/env python3
#coding: utf8               #为了程序可以支持中文，指定UTF8编码

score = int(input('成绩: '))
if score >= 90:
    print('优秀')
elif score >= 80:
    print('好')
elif score >= 70:
    print('良')
elif score >= 60:
    print('及格')
else:
    print('你鸡巴用！')