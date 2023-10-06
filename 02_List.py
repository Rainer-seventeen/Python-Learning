# 第二章 列表的简单使用

# 1.列表引入(类似于Cpp数组)
print("\n##########################")
print("1.列表引入(类似于Cpp数组)")
list01 = ["A", "B", "C", "D"]  # 创建一个列表
print(list01)  # 输出['A', 'B', 'C', 'D']
print(list01[0].lower())  # 输出a


# 2.列表的使用与访问
print("\n##########################")
print("2.列表的使用")
list02 = ["同济", "复旦", "交通", "南京", "浙江", "清华", "北京"]
message02 = f"中国最好的大学是{list02[0]}大学。"  # 用f操作列表的和字符串
print(message02)
print("list02中最后一个元素是", list02[-1])  # 可以用索引-1访问最后一个元素


# 3.修改列表元素
print("\n##########################")
print("3.修改列表元素")
list02[0] = "黄渡理工"  # 修改列表元素
print(list02)


# 4.添加列表元素
print("\n##########################")
print("4.添加列表元素")
list02.append("中国科学技术")  # 在列表末尾追加元素
print(list02)

list02.insert(2, "武汉")  # 在列表中间位置添加元素，将某个元素插到list02[2]这个地址（索引）
print(list02)  # 注意到原来的list02[2]向后移动了一位


# 5.删除列表元素
print("\n##########################")
print("5.删除列表元素")
print(list02)
print("删除了一个大学")
del list02[0]  # 删除已知索引位置的元素
print(list02)

# 使用pop可以将栈顶元素弹出，即取出某个元素，并将其从列表删除
popped_school = list02.pop()  # 取出最后一个元素，存储在popped_school中
print("被弹出的学校是", popped_school, "大学")
print(list02)

# pop也可以添加参数索引，弹出任意一个位置的元素
popped_school = list02.pop(1)  # 取出最后一个元素，存储在popped_school中
print("被弹出的学校是", popped_school, "大学")
print(list02)

# remove可以根据数值来删除特定的一个列表元素
print("remove一个指定的学校")
list02.remove("北京")
print(list02)
print("remove一个指定的学校")
remove_school = "清华"
list02.remove(remove_school)  # 用变量也可以remove
print(list02)
# remove只会删除第一个找到的值，后续仍然删除需要用到循环语句


# 6.管理列表
print("\n##########################")
print("6.管理列表")
print("使用sort可以对列表进行排序，更改后无法复位")
print(list02)
list02.sort()
print(list02)
# 根据GBK：交BDBB，南C4CF，复B8B4，浙D5E3
# 根据Unicode：交4EA4，南5357，复590D，浙6D59
print("可以发现sort是按照Unicode方式排列的")

print("\n可以用sort添加参数reverse来反向排序")
print(list01)
list01.sort(reverse=True)
print(list01)

print("\n使用sorted可以对列表进行临时排序")
print("list01 = ", list01)
print("list01_sorted = ", sorted(list01))  # 使用方法类似于函数
print("list01 = ", list01)
print("list01_REsorted = ", sorted(list01, reverse=True))  # 使用方法类似于函数


# 7.反向打印列表列表
print("\n##########################")
print("7.反向打印列表列表")
print("reverse可以反转列表的顺序，注意不是反向排序")
print(list02)
list02.reverse()  # 永久改变列表的顺序，需要返回直接再使用一次reverse即可
print(list02)

# 8.确定列表的长度
print("\n##########################")
print("8.确定列表的长度")
print("list02的长度是", len(list02))
