# 第八章 文件处理

# 读取文件
from pathlib import Path

path = Path("files_to_opperate/pi_digits.txt")  # Windows系统使用反斜杠的转义符(单一个/也行)，但py会自动匹配合适的路径名称
contents = path.read_text()
print(f"{contents}#")  # 井号用于检测是否有多余文字 (实际上没有)


# 路径问题
# 上面展示的是相对路径,如果使用绝对路径可以这样
# E:\PythonLab\files_to_read
print("##########################")
path = Path("E:/PythonLab/files_to_opperate/pi_digits.txt")
contents = path.read_text()
print(f"{contents}#")  # 井号用于检测是否有多余文字 (实际上没有)


# 处理文件中的行
# 使用splitlines()将返回一个列表，列表包含每一个行
print("\n##########################")
lines = contents.splitlines()  # lines现在是一个个字符串构成的列表
for line in lines:
    print(line,end="") # 每一个换行符号都是print自动加上去的，列表元素不包含换行
# 或者可以用+=来连缀字符串

# 写入文件
print("\n##########################")
path = Path("files_to_opperate/write_message.txt") # 获取目标文件
path.write_text("同济大学nb",encoding="utf-8") # Python只支持写入string变量，其他类型用str()转
#如果要写入多行文件需要自行添加\n转义符
#用UTF8打开文件会乱码，使用GBK方式写入的，增加一个参数控制写入的格式
#并且多次运行发现每一次都是重新写入（覆盖原文件内容）
