# 让我们开始愉快的Python之旅吧
# 第一章 字符串处理

# 1.Hello World!
print("\n##########################")
print("1.输出Hello World!")
Message01 = "Hello World!!"
print(Message01)

# 2. 对字符串操作
print("\n##########################")
print("2. 对字符串操作")
Message02 = "\t  Python is t"
Message03 = "he best language!  "
Message02 = f"{Message02},{Message03}"  # f设置格式，按照大括号内调整格式

print(".title() :", Message02.title())  # 首字母大写
print(".upper() :", Message02.upper())  # 全部大写
print(".lower() :", Message02.lower())  # 全部小写
print(".lstrip():", Message02.lstrip())  # 清除左侧空格（不可见字符）
print(".rstrip():", Message02.rstrip())  # 清除右侧空格（不可见字符）
print(".strip   :", Message02.strip())  # 清除两侧所有空格
