#1,基本数字类型
#简单理解为： 整数  和  小数
int
bool
    True:1
    false:0
float
complex         #复数

#python表示整数，如果没有前缀----表示10进制，
# 2进制0b开头，8进制是0o开头，16进制数0x开头
#cp /etc/hosts /tmp/
#ll /tmp/hosys
import os
os.chmod('/tmp/hosts, 400')
#ll /tmp/hosts
os.chmod('/tmp/hosts, 0o400')

#2、字符串
#在python中，单双引号没有区别

'%s a digit' % 100
'%s is %s years old' % ('zl', 29)

#三引号，三个连续单引号或双引号，他可以保留输入格式

worlds = 'hello\nnihao'

dicts = '''hello
nihao
welcome'''

print(worlds)
print(dicts)


#字符串切片
>>> py_str = 'python'
>>> len(py_str)
6

#拼接和重复
>>> py_str
'python'
>>> py_str + '' + 'good'
'pythongood'
>>> py_str + ' ' + 'good'
'python good'

>>> '*' * 30
'******************************'
>>> '#*#' * 10
'#*##*##*##*##*##*##*##*##*##*#'
>>>


#3、列表 ：把各种数据集中存储到一个容器中

>>> alist = [10, 20, 'zl', 'nicke', [1, 2] ]
>>> alist
[10, 20, 'zl', 'nicke', [1, 2]]
>>> len(alist)
5

>>> alist[-1]
[1, 2]
>>> alist[4]
[1, 2]
>>> 10 in alist
True
>>> 1 in alist
False
>>> alist * 3
[10, 20, 'zl', 'nicke', [1, 2], 10, 20, 'zl', 'nicke', [1, 2], 10, 20, 'zl', 'nicke', [1, 2]]

>>> alist[-1] = 100
>>> alist
[10, 20, 'zl', 'nicke', 100]
>>> alist.append(200)
>>> alist
[10, 20, 'zl', 'nicke', 100, 200]


#4、元组---（）

>>> atuple = (10, 20, 'zl', 'nicke', 100, 200)
>>> atuple[2:4]
('zl', 'nicke')
>>> atuple[-1]
200

#5、字典 {key: val},key不能重复，val可以相同，是无序的

>>> adict = {'name': 'zl', 'age': 29}
>>> adict
{'name': 'zl', 'age': 29}
>>> len(adict)
2
>>> adict['name']
'zl'















































