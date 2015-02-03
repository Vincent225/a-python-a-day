#!/usr/bin/python
#encoding=utf-8

import collections
import re
import os

#这些单词在所有文章中都会频繁出现，不能看做最重要的词
useless_words = ('the', 'a', 'an', 'and', 'by', 'of', 'in', 'on', 'is', 'to')

#所有日志所在的路径
def get_file_list(filepath):
    filelist = os.listdir(filepath)
    return filelist

def get_important_word(file):
    f = open(file)
    line = f.readline()
    word_counter = collections.Counter()

    while line:
        words = re.findall('\w+', line.lower())
        word_counter.update(words)
        line = f.readline()

    f.close()
    #按次序取出出现次序最多的词，和useless_words中的单词比较，如果在use_less表中，就取次一个高频的单词
    most_important_word = word_counter.most_common(1)[0][0]
    count = 2
    while (most_important_word in useless_words):
        most_important_word = word_counter.most_common(count)[count-1][0]
        count += 1
    num = word_counter.most_common(count)[count-1][1]
    print 'the most important word in %s is %s, it appears %d times' % (file, most_important_word, num)
    
    
if __name__ == '__main__':
    filepath = 'diary/'
    filelist = get_file_list(filepath)
    for file in filelist:
        abspath = os.path.join(filepath, file)
        if os.path.isfile(abspath):
            get_important_word(abspath)

