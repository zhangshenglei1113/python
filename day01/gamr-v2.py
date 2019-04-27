#引用random模块choice方法随机生成‘石头’、‘剪刀’、‘布’中任意一项，提示并获取用户的输入字符，应用if扩展语句对随机数与输入值进行对比判断，满足指定条件，输出结果问题结果
import random
computer = random.choice(['石头','剪刀','布'])
player = input('请出拳(石头/剪刀/布): ')

#print('你出了:', player, '计算机出的是:', computer)
print('你出了: %s, 计算机出的是: %s' % (player,computer))
if player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '剪刀':
        print('You win !!!')
    else:
        print('You lose !!!')
elif player == '剪刀':
    if computer == '石头':
        print('You lose!!!')
    elif computer == '剪刀':
        print('平局')
    else:
        print('You win!!!')
else:
    if computer == '石头':
        print('You win!!!')
    elif computer == '剪刀':
        print('You lose!!!')
    else:
        print('平局')