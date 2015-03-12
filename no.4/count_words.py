#!/usr/bin/python
#encoding=utf-8

import collections
import re

def count_word(file_name):
    f = open(file_name)
    
    line = f.readline()
    word_counter = collections.Counter()

    while line:
        #找出所有单词，保存为数组，lower表示将整句话变为小写
        words = re.findall('\w+', line.lower())

        word_counter.update(words)

        #读取下一行
        line = f.readline()

    f.close()

    return word_counter

if __name__ == '__main__':
    result = count_word('test.txt')
    #most_common打印出现次数最多的单词，这里most_common(3)表示出现次数最多的3个单词
    for key,count in result.most_common(30):
        print '%s: %d' % (key, count)
