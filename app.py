#!/usr/bin/python3

def first_step(in_str):
    global lst
    binary = ''.join(format(i, '08b') for i in bytearray(in_str, encoding ='utf-8'))
    b = []
    for j in binary:
        b.append(int(j))
    #print(b)
    

    #zeros_array = np.zeros((16, 32))
    
    i = 0
    
    lst = []
    while i < 512:
        i += 1
        lst.append(int(0))
    #print(lst)

    
    lst[0:len(binary)] = b

    lst[len(binary)] = 1
    
    #64-bit big-endian integer
    big_endian = format(len(binary), 'b')
    
    lst[-int(len(big_endian)):0] = big_endian
    
    lst = lst[0:512]
    #print(lst)

def message_schedule():
    v = 0
    w = []
    while v < 1536:
        v += 1
        w.append(int(0))
    s_msg = lst + w
    #print(len(s_msg))

def 

first_step("javad")
message_schedule()

#HASH values 2, 3, 5, 7, 11, 13, 17, 19
h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

