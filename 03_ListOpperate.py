# 第三章 对列表进行操作

# 预设一个列表：
c9_list = [
    "清华大学",
    "北京大学",
    "上海交通大学",
    "西安交通大学",
    "南京大学",
    "浙江大学",
    "复旦大学",
    "哈尔滨工业大学",
    "中国科学技术大学",
]

# 1. 遍历整个列表
print("##########################")
print("1.遍历整个列表:")
for universities in c9_list:  # 这个for后面的变量可以是任意名字
    print(universities)


# 2.扩展for的操作
print("\n##########################")
print("2.扩展for的操作:")
for universities in c9_list:
    print(f"{universities}算什么东西？不如同济大学一根")
    print("\n")
print("同济大学天下第一")

# python代码中缩进代表着函数和语句的归属，请务必注意

# 3.使用range函数
print("\n##########################")
print("3.使用range函数")
for value in range(1, 5):
    print(value)
print("注意到range(1,5)只打印四个数，等效于for(i = 1; i < 5; i++)")

# 4.创建range列表
print("\n##########################")
print("4.创建range列表")
# 可以使用list函数将range直接变成一个列表
number = list(range(1, 5))
print(number)

print("使用range函数时还可以指定步长（第三个参数）")
even_number = list(range(1, 11, 2))
print(even_number)

# 5.数值列表的简单统计
print("\n##########################")
print("5.数值列表的简单统计")
print(even_number)
print("min:", min(even_number))
print("max:", max(even_number))
print("sum:", sum(even_number))

# 6.列表推导式
print("\n##########################")
print("6.列表推导式")
# 格式； 列表名称 = [追加列表变量表达式 for 变量 in range(a, b)]
# 生成一个完全平方数构成的列表
squares = [value**2 for value in range(1, 11)]  # 符号**表示乘方
print(squares)

# 7.列表切片
print("\n##########################")
print("7.列表切片")
# 列表切边用的是索引值，同时遵循右侧小于的规则

c9_Beijing = c9_list[0:2]  # 索引值从0开始，小于2为止，也就是0,1
print(c9_Beijing)
# 如果没有指定第一个参数，则从第一个开始，如果没有最后一个参数，到最后一个截止
# 可以用负数（代表到列表末尾相应距离的数值）来表示最后几个数
# 另外，可以加入第三个参数，用于控制步长
c9_notBeijing = c9_list[-7:]  # -1会给出一个，如果想要最后n个元素就直接指定左参数是-n
print(c9_notBeijing)

# 复制列表可以用一个[:]的切片来表示

# 8.元组（静态列表）
print("\n##########################")
print("8.元组（静态列表）")
# 元组就是Python中不可以修改的列表
c9_list_pro = (
    "清华大学",
    "北京大学",
    "上海交通大学",
    "西安交通大学",
    "南京大学",
    "浙江大学",
    "复旦大学",
    "哈尔滨工业大学",
    "中国科学技术大学",
    "同济大学",
)

# del c9_list_pro[-1]
# c9_list_pro[-1] = "武汉大学"
# 上述注释语句是不允许的，因为元组不可以删除和修改

# 但是我们可以给表示元组重新赋值，这个操作不同于const 变量
for c9 in c9_list_pro:
    print(c9, end=" ")  # 这个操作让输出不换行，改成空格
print("\n")

c9_list_pro = (
    "清华大学",
    "北京大学",
    "上海交通大学",
    "西安交通大学",
    "南京大学",
    "浙江大学",
    "复旦大学",
    "哈尔滨工业大学",
    "中国科学技术大学",
    "武汉大学",
)

for c9 in c9_list_pro:
    print(c9, end=" ")
print("\n")
