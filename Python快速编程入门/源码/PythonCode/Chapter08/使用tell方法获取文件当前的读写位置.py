# 打开一个已经存在的文件
f = open("itheima.txt", "r")
str = f.read(4)
print("读取的数据是 : ", str)
# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)
str = f.read(8)
print("读取的数据是 : ", str)
# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)
str = f.read(3)
print("读取的数据是 : ", str)
# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)
f.close()