'''
Description: 批量修改文件名
Author: xxHaonan
'''
import os

# 定义目录路径
directory = r"C:\Users\user\Desktop\test"

# 定义要替换的旧字符串和新字符串
old_string = "cornell"
new_string = "plgp"

# 遍历目录中的文件
for filename in os.listdir(directory):
    # 如果旧字符串在文件名中
    if old_string in filename:
        # 构造新文件名
        new_filename = filename.replace(old_string, new_string)
        # 构造完整的文件路径
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        # 重命名文件
        os.rename(old_file, new_file)

print("Renaming completed.")
