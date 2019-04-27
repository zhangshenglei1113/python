#引用random模块生成1-100的随机数，用while循环语句让猜数字次数大于0，提示并获取用户输入整数值，在进行猜数字对错判断前先用if嵌套判断方式确定输入值是否合法，如果合法进行猜数字对错判断，判断结束后猜数字次数需减1，如果不合法重新进入循环，此时循环次数不减少
#此程序需要注意的部分在于：
#每局对错判断之后，猜数字次数一定要减1，这样猜数字次数等于0的时候，循环就结束了
# vim guess.py
#! /usr/bin/env python3

import random
secret = random.randint(1,100)          #生成随机数
time = 5                                #猜数据的次数
print("-----欢迎来到猜数字，请开始------------")
while time > 0:
    guess = int(input("*数字区间0-100，请输入你彩的数字："))
    print("你输入的数字是：",guess)
    if 0 <= guess < 100:
        if guess == secret:
            print("猜对了，你牛逼")
        else:
            print("太遗憾了，你猜错了，你还有",time-1,"次机会")
        time -= 1
    else:
        print("输入非法，请重新输入")
print("游戏结束，正确的结果是：",secret)