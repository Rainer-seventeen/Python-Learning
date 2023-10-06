# 第五章 字典

# 1.字典初步使用
print("##########################")
print("1.字典初步使用")
# 用大括号来表示创建一个字典,冒号前后是一对键值对，前键后值
student_info = {"姓名": "张三", "性别": "男", "学号": "2250000"}
# 尤其注意""内的同样地引号要使用''来替代
print(student_info)
message = f"{student_info['姓名']}的学号是{student_info['学号']}"
print(message)

# 2.初步操作字典
print("\n##########################")
print("2.初步操作字典")

# 添加键值对(修改同理，略)
print("添加键值对")
student_info["班级"] = "通信1班"  # 在最后加上这个键值对，顺序添加方式
print(student_info)

# 删除键值对
print("删除键值对")
del student_info["学号"]
print(student_info)

# 3.使用get()来访问值
print("\n##########################")
print("3.使用get()来访问值")
print(student_info.get("分数", "没有找到该学生的分数信息"))
# 第一个是索引值，第二个是如果没有找到则返回，相比直接用[]获取，可以避免error
# 如果没有指定第二个数值，则会返回None，类似于Cpp中的NULL。
print(student_info.get("分数"))

# 4.遍历字典
print("\n##########################")
print("4.遍历字典")
print("***遍历所有的键值对")
for key, value in student_info.items():
    print(f"{key}:{value}")
    # print(f"{key}:{student_info[key]}")   可以用key访问也可以直接用value

print("\n***遍历所有的键")
for key in student_info.keys():  # .keys()可以省略，即缺省遍历键
    print(key, end=" ")  # 这里的key代表键，可以用类似地址的方式访问对应的值
print("\n")

# 表达式 student_for.keys()返回的是包含字典中所有键的列表(这里原理就是遍历列表)
# 你可以使用sorted()函数对列表排序，也就是student_info.keys()

# print("\n***用集合的方式遍历所有的值")
# 同上，用.values()例子略，但值可能有很多个重复，可以用集合来剔除重复项目
# 用set()对列表进行修饰，可以去重
# 可以用一对大括号直接创建一个集合(集合内部没没有排序)
school_c9 = {
    "清华大学",
    "北京大学",
    "上海交通大学",
    "西安交通大学",
    "南京大学",
    "浙江大学",
    "复旦大学",
    "哈尔滨工业大学",
    "中国科学技术大学",
}
print(school_c9)  # 每一次print都是一次惊喜（顺序完全随机）

# 5.字典嵌套于列表中
print("\n##########################")
print("5.字典嵌套于列表中")
# 用元素是字典的一个列表即可

student_list = []  # 创建一个空列表
for student_num in range(1, 31):
    student_list.append(student_info)  # 每个学生都用同一个

# 下面来显示一个列表的前3个学生信息
for students in student_list[:3]:
    print(students)  # 这里的students 就是列表元素，也就是一个dict
print("...")
print(f"总共有{len(student_list)}个学生")


# 5.列表嵌套于字典中
print("\n##########################")
print("5.列表嵌套于字典中")
student_score = {"姓名": "张三", "5次数学成绩": [90, 91, 92, 93, 94]}
print(f"学生{student_score['姓名']}的5次数学成绩分别是", end=" ")
for scores in student_score["5次数学成绩"]:
    print(scores, end=" ")
print("\n")

# 5.字典嵌套于字典中
print("\n##########################")
print("5.字典嵌套于字典中")
# 这个嵌套会让代码迅速变得复杂

# 没那么多数据，随便写俩意思意思
stu1_info = {
    "姓名": "张三",
    "成绩": {
        "数学": [90, 91, 92, 93, 94],
        "英语": [90, 91, 92, 93, 94],
        "语文": [90, 91, 92, 93, 94],
    },
}
# 遍历张三的所有学科成绩
for subjects in stu1_info["成绩"].keys():  # 第一层循环，取出这个学科的的列表 subjects:"数学"
    for times in range(0, len(stu1_info["成绩"][subjects])):  # 第二层循环, 取出字典值中的列表
        print(f"{stu1_info['姓名']}的第{times+1}次{subjects}", end="")
        print(f"成绩是{stu1_info['成绩'][subjects][times]}")
