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

#w(n)
def w(n):
    global wn
    x = (n + 1) * 32
    wn = lst[x-32:x]
    #print(wn)


#RIGHTROTATES

def rightrotate_7(a):
    global rr_7
    global str_rr_7

    str_rr_7 = ''
    rr_7 = a[25:32] + a[0:25]
    for i in rr_7:
        str_rr_7 = str_rr_7+str(i)


def rightrotate_18(a):
    global rr_18
    global str_rr_18

    str_rr_18 = ''
    rr_18 = a[14:32] + a[0:14]
    for i in rr_18:
        str_rr_18 = str_rr_18+str(i)


def rightrotate_17(a):
    global rr_17
    global str_rr_17

    str_rr_17 = ''
    rr_17 = a[15:32] + a[0:15]
    for i in rr_17:
        str_rr_17 = str_rr_17+str(i)   

def rightrotate_19(a):
    global rr_19
    global str_rr_19

    str_rr_19 = ''
    rr_19 = a[13:32] + a[0:13]
    for i in rr_19:
        str_rr_19 = str_rr_19+str(i)

#RIGHTSHIFTS

def rightshift_3(a):
    global rs_3
    global str_rs_3

    str_rs_3 = ''
    rs_3 = [0, 0, 0] + a[0:29]
    for i in rs_3:
        str_rs_3 = str_rs_3+str(i)
    

def rightshift_10(a):
    global rs_10
    global str_rs_10

    str_rs_10 = ''
    rs_10 = rs_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] + a[0:22]
    for i in rs_10:
        str_rs_10 = str_rs_10+str(i)
    


#STEP TWO


#XOR
#a and b must be string and executed from rr_* and rs_* functions
def XOR(a, b):
    global c
    y=int(a,2) ^ int(b,2)
    c = '{0:0{1}b}'.format(y,len(a))
    #print(c)


#CALCULATING W16
#w16 = w0 + σ0 + σ1 + W9



w1 = lst[32:64]

w0 = lst[0:32]
#print(w0)

#CALCULAT SIGMA0
def sigma0():
    w(1)
    global sigma0_list
    global c0
    rightrotate_7(wn)
    rightrotate_18(wn)
    rightshift_3(wn)
    XOR(str_rr_7, str_rr_18)
    XOR(c, str_rs_3)
    c0 = c
    #print("sigma0: "+c)
    sigma0_list = []
    for i in c:
        sigma0_list.append(int(i))
    #print(sigma0_list)

#sigma0()

#CALCULATING SIGMA1
def sigma1():
    w(14)
    global sigma1_list
    global c1
    rightrotate_17(wn)
    rightrotate_19(wn)
    rightshift_10(wn)
    XOR(str_rr_17, str_rr_19)
    XOR(c, str_rs_10)
    c1 = c
    #print("simga1: "+c)
    sigma1_list = []
    for i in c:
        sigma1_list.append(int(i))
    #print(sigma1_list)

sigma0()

#print(c0)

sigma1()

#print(c1)

result1 = int(c0, 2) + int(c1, 2)
#binary_result = bin(result1)[2:]


w(0)
w0 = wn
w0 = ''.join(str(x) for x in w0)
#print(w0)


w(9)
w9 = wn
w9 = ''.join(str(x) for x in w9)
#print(w9)

result2 = int(w0, 2) + int(w9, 2)
#binary_result = bin(result2)[2:]

result = result1 + result2

#result1 = int(c0, 2) + int(c1, 2)
binary_result = bin(result)[2:]
if len(binary_result) < 32:
    binary_result = "0" + binary_result
#print(binary_result)
w16 = binary_result
for i in w16:
    lst.append(i)
w(16)
print(len(wn))

#HASH values 2, 3, 5, 7, 11, 13, 17, 19
h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19




