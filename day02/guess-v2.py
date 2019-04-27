#改进彩数字脚本 V2版本
import random

num = random.randint(1, 100)
counter = 0

while counter < 5:
    answer = int(input('guess the number: '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break
    counter += 1
else:           #循环被break中断，就不执行了，没有被break才执行
    print('the number is:', num)