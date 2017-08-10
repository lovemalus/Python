# list1.py

import os


# 获取当前工作目录的文件和文件夹

def list_cwd():
    return os.listdir(os.getcwd())

# 列表解析返回当前文件和文件夹

def files_cwd():
    return [p for p in list_cwd()
            if os.path.isfile(p)]

# 返回当前工作目录中所有文件大小总和

def size_in_bytes(fname):
    return os.stat(fname).st_size

def cwd_size_in_bytes():
    total = 0
    for name in files_cwd():
        total = total +size_in_bytes(name)
    return total

fi = cwd_size_in_bytes()

print fi
