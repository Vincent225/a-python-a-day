#!/usr/bin/python
#encoding=utf-8
import uuid

def generate_activation_code(count):
    code_list = []
    for i in xrange(count):
        code = str(uuid.uuid4()).replace('-','').upper()
        #uuid4的算法有一定的重复概率，所以下面作了判断
        #if not code in code_list:
        if code not in code_list:
            code_list.append(code)

    return code_list

if __name__ == '__main__':
    code_list = generate_activation_code(200)
    for code in code_list:
        print code
