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

first_step("javad")


#RIGHTROTATES

def rightrotate_7(a):
    global rr_7

    rr_7 = a[25:32] + a[0:25]


def rightrotate_18(a):
    global rr_18

    rr_18 = a[14:32] + a[0:14]


def rightrotate_17(a):
    global rr_17

    rr_17 = a[15:32] + a[0:15]
    

def rightrotate_19(a):
    global rr_19

    rr_19 = a[13:32] + a[0:13]

#RIGHTSHIFTS

def rightshift_3(a):
    global rs_3

    rs_3 = [0, 0, 0] + a[0:29]
    

def rightshift_10(a):
    global rs_10

    rs_10 = rs_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] + a[0:22]
    

#STEP TWO
w1 = lst[32:64]

rightrotate_7(w1)
rightrotate_18(w1)
rightshift_3(w1)

#XOR




#HASH values 2, 3, 5, 7, 11, 13, 17, 19
h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

