# 数据处理（初步）

#可以使用json模块将Python数据结构转化为JSON格式字符串

from pathlib import Path
import json


# json.dump写入数据
numbers = [1,2,3,5,6,7]
path = Path("test_data/number.json") # 第一个不要有斜杠，如果没有这个文件会自动创建一个
contents = json.dumps(numbers) # 将numbers列表转成json形式的字符串给contents
path.write_text(contents) # 写入contents

# json.loads()加载数据  load后面有个s别忘了
# path就用上边定义过了
contents = path.read_text()
numbers = json.loads(contents) # 加载read出来的数据，并存入numbers列表
print(numbers)

#这个数据方式帮助程序之间存取读取数据（用json格式写入，后用json格式读取）