from Crypto.Util.number import *

def ROR(bits, N, length):
    for _ in range(N):
        bits = (bits >> 1) | (bits & 1) << (length - 1)
    return bits

def decrypt(key, cipher, length):
    for i in range(32):
        cipher ^= key
        key = ROR(key, pow(cipher, 3, length), length)

    flag = long_to_bytes(cipher ^ key)
    return flag

key    = 364765105385226228888267246885507128079813677318333502635464281930855331056070734926401965510936356014326979260977790597194503012948
cipher = 92499232109251162138344223189844914420326826743556872876639400853892198641955596900058352490329330224967987380962193017044830636379

for length in range(15,1000):
    flag = decrypt(key, cipher, length)
    try:
        if "ctf" in flag.decode():
            print("flag =", flag)
            break
        else:
            print(flag)
    except:
        print(flag)