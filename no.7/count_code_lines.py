#!/usr/bin/python
#encoding=utf-8

import re
import os

total = 0
blank = 0
comment = 0

#要想使用全局变量，必须要用global来申明
def count_code_lines(filename):
    global total
    global blank
    global comment
    f = open(filename)
    lines = f.readlines()
    total += len(lines)  #行数

    pattern_blank = re.compile(r'^\s*$')
    pattern_comment = re.compile(r'^\s*\#+')

    for line in lines:
        if pattern_blank.match(line):
            blank += 1
        elif pattern_comment.match(line):
            comment += 1


def walk_dir(file_path):
    global total
    global blank
    global comment
    #os.walk返回值为3元tupple，第一个是起始路径，第二个是起始下的文件夹，第三个是起始路径下的文件
    for root, dirs, files in os.walk(file_path):
        for file in files: 
            if file.lower().endswith('.py'):
                full_path = os.path.join(root, file)
                count_code_lines(full_path)

#在main函数里不要用global来申明全局变量
if __name__ == '__main__':
    walk_dir('../')
    print 'total line is %d, blank is %d, comment is %d' % (total, blank, comment)
