# 第七章 类


# 创建一个类：
class Student:  # 类的首字母要大写,并且不应该掺杂下划线（大驼峰命名）
    """存储一个学生的信息"""  # 每一个类后面建议紧跟一个字符串，用于说明

    # 定义方法，__init__()方法两侧必须 [双]下划线 ，用于初始化属性，每次创建实例时都会调用一次的函数
    def __init__(self, name="NULL", age=18, score=0):  # 所有方法的 self 形参是必不可少的，且必须放置在第一位
        # self的实参 会自动传入到self形参
        self.name = name  # 用传入的实参 name 赋值  (是不是有点像Cpp的this?)
        self.age = age
        self.score = score

    def passed(self):
        print(f"恭喜{self.name}通过了考试")
        if self.score < 60:
            self.score = 60

    def score_write(self, in_score):
        print(f"{self.name}的成绩写入完成")
        self.score = in_score


Zhang_san = Student("张三", 18, 40)  # 按照类的方式创建一个 实例
print(f"{Zhang_san.name} 目前的成绩是 {Zhang_san.score}")  # 访问一个 实例 中的 属性
Zhang_san.passed()  # 调用实例中的一个 方法
# 一般来说，如果想要更改一个实例里某个属性的数值，应该设定一个方法来改，而不是直接访问


# 继承(inheritance),用于编写一个现有类的特殊版本，新的类成为子类
# 子类的父类必须在同一个文件当中
class ExcellentStudent(Student):
    """让我们看看优等生的独特之处"""

    def __init__(self, name, age, score):
        super().__init__(name, age, score)  #  输出化父类的属性，这段代码是自动生成的
        # super()是一个特殊函数，允许子类调用父类的方法
        # 既然是调用，那这里传的就是实参，也就不需要self

        # 调用完父类的初始化后，可以来进行子类独特的方法
        self.prize = 0

    def get_prize(self):  # 所有定义方法都需要一个self在最前面
        print(f"让我们恭喜{self.name}同学又得了一个奖状！")
        self.prize += 1

    def show_prize(self):
        print(f"{self.name}同学目前有{self.prize}个奖状")

    def passed(self):
        # 如果父类的方法不适用于子类，可以在定义一个同名的子类方法，在子类中会覆盖
        if self.score >= 90:
            print(f"{self.name}的成绩是{self.score}，常规发挥而已！")


Li_si = ExcellentStudent("李四", 18, 95)
Li_si.passed()
Li_si.show_prize()
Li_si.get_prize()
Li_si.show_prize()


# 嵌套类，作用是将某一个类的某一方面属性再一次整合起来，便于修改，防止大类过于混乱
class People:
    """存储一个公民的信息"""

    def __init__(self, name, ID, sex):
        self.ID = ID
        self.sex = sex

        # 创建一个实例 作为People类的属性
        self.student_info = Student(name)  # 把People 的 name属性 给到Student这个类内


Wang_wu = People("王五", 123, "Male")
Wang_wu.student_info.passed()  # 如果没有设定初值数值就是18岁0分


# 跟函数相同，类也是可以导入的
# 导入单个类 ： import 类 from 模块名  (仅导入子类不会因为父类没导入而报错？待考证)
# 导入多个类 ： from 模块名 import 类1, 类2, ...
# 导入整个模块： import 模块名 (后续访问类需要加模块名前缀)
# 还有导入模块所有类的方式，不推荐使用
# （类）使用别名： from 模块 import 类 as 别名   （别名类似引用，不用加模块名前缀）
# （模块）用别名： import 模块 as 别名


# Python中多个模块构成一个库(library)，Python已经配备了一个标准库
# 例如可以 import random 访问随机变量模块