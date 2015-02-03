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

#filtered_word表示敏感词汇
#text是输入的待检测的句子
def replace_word(filtered_words):
    flag = False
    text = raw_input('please input: ')
    for filtered_word in filtered_words:
        if filtered_word in text:
            text = text.replace(filtered_word, '*'*len(filtered_word))

    print text

if __name__ == '__main__':
    filepath = 'filtered_words.txt'
    filtered_words = get_sensitive_word(filepath)
    replace_word(filtered_words)
    
