#!/usr/bin/python
#encoding=utf-8

import collections
import re

def count_word(file_name):
    f = open(file_name)
    
    word_counter = collections.Counter()

    #文件对象使用迭代器
    for line in f:
        words = re.findall('\w+', line.lower())
        word_counter.update(words)

    #迭代器对象只能遍历一次，欲再次遍历需要重现构建迭代器对象
    f = open(file_name)
    #计算单词总数 p206
    word_sum = len([word for line in f for word in line.split()])


    #最长行
    f = open(file_name)
    longest = max(len(line.split()) for line in f)

    print "the longest line's length is %d" % longest
    f.close()

    return word_counter, word_sum

if __name__ == '__main__':
    world_counter, word_sum = count_word('test.txt')
    print 'there are %d words in this article' % word_sum
    #most_common打印出现次数最多的单词，这里most_common(3)表示出现次数最多的3个单词
    for key,count in world_counter.most_common(3):
        print '%s: %d' % (key, count)
