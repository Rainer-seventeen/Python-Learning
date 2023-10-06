# 第九章 异常处理

# 可以使用try-except来处理这段错误的代码
try:
    print(5/0) # ZeroDivisonError
except ZeroDivisionError:
    print("0不可以作为除数")

# traceback会直接输出，这会导致程序泄露
# 使用else代码块可以避免这样的操作

print ("输入两个整数，可以计算除法")
num_1 = input("输入被除数")
num_2 = input("输入除数")

try:
    answer = int(num_1) / int(num_2) # 输入的字符默认为字符串
except ZeroDivisionError:
    print("0不可以作为除数")
else:
    print (answer) # 如果try的代码没有出现任何错误，执行这句话


from pathlib import Path
path = Path("123.txt") 
try:
    content = path.read_text() #FileNotFoundError
except FileNotFoundError:
    print(f"找不到文件\"{path}\"")


# 静默失败：在发生错误时继续运行，使用关键词pass，下面是个例子
# except FileNotFoundError:
#   pass
