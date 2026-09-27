"""
文档字符串
文档字符串（docstring）：用于描述模块、函数、类或方法的功能、参数和返回值，帮助其他程序员理解如何使用这些代码实体，并可被Python内置函数help()调用生成文档提示 
"""

import keyword

def is_valid_identifier(name):
    try:
        exec(f"{name} = None")
        return True
    except:
        return False

print(is_valid_identifier("2var"))  # False
print(is_valid_identifier("var2"))  # True

print(keyword.kwlist)


# 注释
'''
也是注释  也是字符串字面量
'''

"""
也是注释  也是字符串字面量
"""

# 数字Number类型
# int整形 长整型
print(10)  # 十进制
print(548411555161151565131516511561165)  # 长整型
print(0b1010)  # 二进制 
print(0o12)  # 八进制
print(0xA)  # 十六进制

# 布尔类型 
print(True)
print(False)

# 浮点数
print(3.1415926)
print(3.14e-10)  # 科学计数法 3.14 * 10^-10 = 0.000000000314
print(1.56E10)   # 1.56 * 10^10

# 复数

# 字符串
# 单引号和双引号使用完全一致
# 使用三引号可以指定多行字符串 也可以用于注释 也可以用于文档字符串

print(__doc__)  # 输出当前模块的文档字符串

# 转义符 \
print("使用转义符\n 换行 ")
print(r"使用r \n使转义符失效 ")

# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python 中的字符串不能改变。
# Python 没有单独的字符类型

# 字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引
str = 'hello world'
print(str[0:-1])
print(str[0:5])
print(str[1:])

import sys

print('命令行参数')
for i in sys.argv:
    print(i)

print('\n python 路径为', sys.path, '\n')  # 输出python路径


