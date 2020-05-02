from  RSA.RSA import RSA_simple
print('n,eはソースコードに書き込んでください,factordbが帰ってきたらそれが一番信用できる気がします')

solver=RSA_simple()
n=0x86E996013E77C41699000E0941D480C046B2F71A4F95B350AC1A4D426372923D8A4561D96FBFB0240595907201AD3225CF6EDED7DE02D91C386FFAC280B72D0F95CAE71F42EBE0D3EDAEACE7CEA3195FA32C1C6080D90EF853D06DD4572C92B9F8310BBC0C635A5E26952511751030A6590816554E763031BCBB31E3F119C65F
e = 0x0285f8d4fe29ce11605edf221868937c1b70ae376e34d67f9bb78c29a2d79ca46a60ea02a70fdb40e805b5d854255968b2b1f043963dcd61714ce4fc5c70ecc4d756ad1685d661db39d15a801d1c382ed97a048f0f85d909c811691d3ffe262eb70ccd1fa7dba1aa79139f21c14b3dfe95340491cff3a5a6ae9604329578db9f5bcc192e16aa62f687a8038e60c01518f8ccaa0befe569dadae8e49310a7a3c3bddcf637fc82e5340bef4105b533b6a531895650b2efa337d94c7a76447767b5129a04bcf3cd95bb60f6bfd1a12658530124ad8c6fd71652b8e0eb482fcc475043b410dfc4fe5fbc6bda08ca61244284a4ab5b311bc669df0c753526a79c1a57

p,q=0,0
try:
    p,q=solver.try_factordb(n,e)
except e:
    print(e)
print('factordb result is')
print(p,q)

p,q=0,0
try:
    p,q=solver.try_WinersAttack(n,e)
except:
    pass
print('WinersAttack result is')
print(p,q)

p,q=solver.try_fermat(n,e)
print('fermat result is')
print(p,q)

p,q=solver.try_factorial_from2(n,e)
print('simple factorial result is')
print(p,q)

