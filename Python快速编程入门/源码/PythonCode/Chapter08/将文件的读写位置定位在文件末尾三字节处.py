# 打开一个已经存在的文件
f = open("itheima.txt", "rb+")
str = f.read(15)
print("读取的数据是 : ", str)
# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)
# 重新设置位置
f.seek(-4,2)
# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)
f.close()