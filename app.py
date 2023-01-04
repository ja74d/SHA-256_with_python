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
w1 = lst[32:64]

rightrotate_7(w1)
rightrotate_18(w1)
rightshift_3(w1)



#XOR
a = str_rr_18
b = str_rr_7
y=int(a,2) ^ int(b,2)

c = '{0:0{1}b}'.format(y,len(a))
#print(c)
d = str_rs_3
e = int(c,2) ^ int(d,2)
z = print('{0:0{1}b}'.format(e,len(a)))

print(str_rr_7)
print(str_rr_18)
print(str_rs_3)


#HASH values 2, 3, 5, 7, 11, 13, 17, 19
h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

