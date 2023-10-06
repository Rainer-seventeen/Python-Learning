# 第四章 语句的使用

# 1.if语句的语法
print("##########################")
print("1.if语句的语法")

university = "Tongji University"
if university == "Tongji University":
    print("Tongji University")
else:
    print("not Tongji University")
# 可以在变量后增加后缀.lower()的方式忽略大小写

# 使用and或者o可以连接某两个条件，例子略

# 2.检查列表是否包含某个元素
print("\n##########################")
print("2.检查列表是否包含某个元素")
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
if "同济大学" in c9_list:
    print("同济大学是C9")
else:
    print("同济大学不是C9")
# 也可以使用关键词 not in 达到相反的效果

# 3.使用if-elif-else语句
print("\n##########################")
print("3.使用if-elif-else语句")
print("if-elif-...-elif(-else)语句同C++,略")
# 可以有多个elif,可以最后不加上else

# 4.用if语句操作列表
print("\n##########################")
print("4.用if语句操作列表")

print("用if紧跟一个列表可以在列表非空时表示True")
if c9_list:  # 对于数值0，None，空字符串，空列表/元组/字典都会返回False
    print("原来C9里面至少有一个学校啊")


# 5.while语句的使用(基本同cpp)
print("\n##########################")
print("while语句的使用")
# while input("输入wdnmd，不然不给结束") != "wdnmd":
#     continue

# EX 用户输入测试
# TODO：但是这个方法不可以处理错误的用户输入，这是个待解决的问题
age = int(input("输入一个数字"))
print(age)
