#  vim grade-v2.py
#!/usr/bin/env python3
#判断成绩的脚本

if score >= 60 and score < 70:
    print('及格')
elif 70 <= score < 80:
    print('良')
elif 80 <= score < 90:
    print('好！！')
elif score >= 90:
    print('优秀')
else:
    print('吃干饭，行')