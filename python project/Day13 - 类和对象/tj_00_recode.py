
"""
1.json: a.只有一个数据
        b.数据类型是json支持的类型

2.json数据转python
json.load(文件对象)
json.loads(字符串)


3.python数据转json
json.dump(数据，文件对象)
json.dumps(数据) -> 字符串

"""

import json

json.dumps("abc")   # -> '"abc"'
json.dumps([1, "abc", True])  # -> '[1, "abc", true]'

