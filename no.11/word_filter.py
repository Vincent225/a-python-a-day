#!/usr/bin/python
#encoding=utf-8

def get_sensitive_word(filepath):
    f = open(filepath, 'r')
    #data = f.read()
    #filt = data.split('\n') 这个方法得到的序列中最后有一个空的字符串，导致匹配一直成功
    words = []
    for word in f:
        #strip删除字符序列，这里是删除word中的'\n'
        words.append(word.strip('\n'))
    f.close()
    print words
    return words
 
def filter_word(words):
    flag = False
    text = raw_input('please input: ')
    for word in words:
        if text.find(word) != -1:
            flag = True

    if flag:
        print 'freedom'
    else:
        print 'human rights'

if __name__ == '__main__':
    filepath = 'filtered_words.txt'
    words = get_sensitive_word(filepath)
    filter_word(words)
    
