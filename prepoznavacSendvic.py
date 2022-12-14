import random

def append_hex(a, b):
    sizeof_b = 0

    # get size of b in bits
    while((b >> sizeof_b) > 0):
        sizeof_b += 1

    # align answer to nearest 4 bits (hex digit)
    sizeof_b += sizeof_b % 4

    return (a << sizeof_b) | b


key_a        = 0x9900aabbccddeeff1122334455667788
delta_key_ab = 0x00008000000000000000000000000000
delta_key_ac = 0x00000000000000000000000080000000
key_b = key_a ^ delta_key_ab
key_c = key_a ^ delta_key_ac
key_d = key_c ^ delta_key_ab

delta = 0x0000000000100000
nabla = 0x0010000000000000

C_a = [None] * 2**24   #2**24
C_b = [None] * 2**24   #2**24
C_c = [None] * 2**24   #2**24
C_d = [None] * 2**24   #2**24
P_a = [None] * 2**24   #2**24
P_b = [None] * 2**24   #2**24
P_c = [None] * 2**24   #2**24
P_d = [None] * 2**24   #2**24

A = 0x2950412b
Kasumi_P_a = Kasumi()
Kasumi_P_a.KeySchedule(key_a)
Kasumi_P_b = Kasumi()
Kasumi_P_b.KeySchedule(key_b)
Kasumi_P_c = Kasumi()
Kasumi_P_c.KeySchedule(key_c)
Kasumi_P_d = Kasumi()
Kasumi_P_d.KeySchedule(key_d)

dict = {}
quartets = {}

for i in range(0, 2**24):  #2**24
    #print("****************")
    X_a = random.getrandbits(32)
    C_a[i] = hex(append_hex(X_a, A)) #f'0x{A:x}{X_a:x}'
    
    P_a[i] = hex(Kasumi_P_a.decription(int(C_a[i], base = 16)))
   
    P_b[i] = int(P_a[i], base = 16) ^ delta
    C_b[i] = Kasumi_P_b.encription(P_b[i])
   
    #stavljam u hes tabelu
    dict[hex(C_b[i] & 0xFFFFFFFF)] = (C_a[i], hex(C_b[i])) 
    
    
for i in range(0, 2**24):  
    #print("-------------------")
    Y_c = random.getrandbits(32)
    C_c[i] = hex(append_hex(Y_c, A ^ 0x00100000))
    
    P_c[i] = hex(Kasumi_P_c.decription(int(C_c[i], base = 16)))
  
    P_d[i] = int(P_c[i], base = 16) ^ delta
    C_d[i] = Kasumi_P_d.encription(P_d[i])
        
    if hex((C_d[i] & 0xFFFFFFFF) ^ nabla) in dict:
        quartets[hex(int(hex(C_a)[:10], base = 16) ^ int(hex(C_c)[:10], base = 16))] = \
            ( dict[hex((C_d[i] & 0xFFFFFFFF) ^ nabla)][0], \
              dict[hex((C_d[i] & 0xFFFFFFFF) ^ nabla)][1], \
              hex(C_c), \
              hex(C_d)\
            )
    
    
        
print(quartets) 