import os
from chardet import detect

fileSuffix = 'txt'
fns = []

# 存放文件目录的绝对路径
filedir = "C:/download/1"

# os.listdir() 用于返回一个由文件名和目录名组成的列表，即返回当前路径（文件夹）下所有文件的绝对路径列表
file_name = os.listdir(filedir)

for fn in file_name:
    if fn.endswith(fileSuffix):
        # endswith() 判断字符串是否以指定后缀结尾
        fns.append(os.path.join(filedir, fn))
for fn in fns:
    with open(fn, 'rb+') as fp:
        content = fp.read()
        if len(content)==0:
            continue
        else:
            codeType = detect(content)['encoding']
            content = content.decode(codeType, "ignore").encode("utf8")
            fp.seek(0)
            fp.write(content)
            print(fn, "：已修改为utf8编码")