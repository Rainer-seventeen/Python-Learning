# 第六章 函数

# 感觉没啥好讲的，和cpp蛮像的


def f0(num_1, num_2):  # 定义记得加冒号来区分
    if num_1 > num_2:
        return num_1  # 返回一个更大的数
    else:
        return num_2


# 如果输入的是A和b这类，返回的是ascii更大的一个
# 如果输入字符串（英文难），则一个个对比，经过实验发现字符串末尾使用'\0'来进行比较
# 中文也可以比较，原理同列表中的sort排序（Unicode）



def f1(好的大学, 差的大学,):  # 你甚至可以用中文来设置形参  后面多加个逗号都是允许的
    print(f"{好的大学}薄纱{差的大学}")


f1("同济大学", "武汉大学")  # 顺序形参列表，一一对应
f1(差的大学="武汉大学", 好的大学="同济大学")  # 可以制定实参对应形参的顺序，成为关键字实参


def 拉踩(差的大学, 好的大学="同济大学"):  # 同Cpp避免二义性，可以制定默认参数，但必须放在最后一个
    print(f"{差的大学}？，感觉不如{好的大学}")


拉踩("西安交大")

# 返回值的设定：可以返回字典，列表，字符串等等，例子略

# 传参之列表的传递
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


def 同济不能被轻视(好大学列表):
    if "同济大学" not in 好大学列表:
        print("你这个肯定是野榜，应该是这样的")
        好大学列表.insert(0, "同济大学")
    return 好大学列表


print(同济不能被轻视(c9_list))
print(c9_list)  # 可以发现原来的列表已经被改变了，类似于cpp数组传递

# 所以我们可以禁止函数对列表进行修改


def 同济算什么东西(好大学列表):
    if "同济大学" in 好大学列表:
        print("同济肯定是买过榜了，应该是这样的")
        好大学列表.remove("同济大学")
        print(好大学列表)


同济算什么东西(c9_list[:])  # 传递一个切片给函数让他自娱自乐去
print(c9_list)


# 不定量的形参，如果可以形参前面加上*，函数会自动创建元组来接受所有的参数
def 报菜名(*菜名):  # 同样由于二义性考虑，有且只有最后一个才可以使用*
    print(菜名)


报菜名("番茄炒蛋", "西红柿炒蛋", "西红柿炒鸡蛋", "番茄炒鸡蛋")

# 两个**会创建一个字典，可以输入键值对

from Tools import *   # 从Tools中导入所有的函数，此类方法不需要加前缀
# 将函数导入到模块中使用，类似于cpp的头文件用法
# import 文件名     (似乎不可以使用  以数字开头的  含有下划线的文件名？)
# 在调用的时候类似于cpp中的“类”: 文件名.函数名()
# 也可以只导入特定的函数 ， from 模块名称 import 函数1, 函数2, 函数3, ...

cct_cls()
# 使用as给 导入的 函数/模块指定别名
# from 模块 import 函数1 as 别名   ，可以用别名调用该函数
# import 模块 as 别名  ， 同理
