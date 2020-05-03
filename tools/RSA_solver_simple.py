from  RSA.RSA import RSA_simple
print('n,eはソースコードに書き込んでください,n,eを基に素因数分解、p,q,dを求めます')

solver=RSA_simple()
n=0x86E996013E77C41699000E0941D480C046B2F71A4F95B350AC1A4D426372923D8A4561D96FBFB0240595907201AD3225CF6EDED7DE02D91C386FFAC280B72D0F95CAE71F42EBE0D3EDAEACE7CEA3195FA32C1C6080D90EF853D06DD4572C92B9F8310BBC0C635A5E26952511751030A6590816554E763031BCBB31E3F119C65F

e=65537

# please add function when you implement solver
try_functions=[solver.try_factordb,solver.try_WinersAttack,solver.try_fermat,solver.try_factorial_from2]


p,q=0,0
for func in try_functions:
    print('try..')
    try_p,try_q=0,0
    try:
        try_p,try_q=func(n,e)
    except:
        pass
    if try_p*try_q==n:
        print('success')
        p,q=try_p,try_q
        break
    else:
        print('failed..')

if p*q!=n:
    print('sorry factorial failed')
    exit(0)
print("p is ",p,'\n')
print("q is ",q,'\n')


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


d=modinv(e,(p-1)*(q-1))
print('秘密鍵d = ',d,'\n')

