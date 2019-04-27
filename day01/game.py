# vim game.py
#!/usr/bin/env python3
#石头剪刀布，游戏
import random                       #调用random模块，生成随机数
#1.提示并回去用户的输入，赋值运算符必须是=
player = int(input("请输入 0石头 1剪刀 2布: "))

#2.让电脑出一个随机数
computer = random.randint(0,2)

#3.判断用户输入，然后显示对应的结果
# if 玩家获胜的条件,判断是==
if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
    print("赢了,,,,可以去泡妹子了.......")
# elif 玩家平局的条件
elif player == computer:
    print("平局了,,,洗个手，决战到天亮......")
else:
    print("输了,,,没钱了......")

