import numpy as np

def first_step(in_str):
    binary = ''.join(format(i, '08b') for i in bytearray(in_str, encoding ='utf-8'))
    b = []
    for j in binary:
        b.append(int(j))
    #print(b)
    

    zeros_array = np.zeros((16, 32))
    
    i = 0
    lst = []
    while i < 512:
        i += 1
        lst.append(int(0))
    #print(lst)
    

    #print(zeros_array)
    
    lst[0:len(binary)] = b

    lst[len(binary)] = 1
    
    #64-bit big-endian integer
    big_endian = format(len(binary), 'b')
    
    lst[-int(len(big_endian)):0] = big_endian
    lst = lst[0:512]
    #print(lst)

first_step("javad")