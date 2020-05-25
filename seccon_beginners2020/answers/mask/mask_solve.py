import subprocess


s="ctf4b"

characters="1234567890wertyuiopasdfghjkl;zxcvbnm,./_:]@[-^\\ZXCVBNM<>?_ASDFGHJKL+*}QWERTYUIOP`{!#$%&()0=~|t"
ans='atd4`qdedtUpetepqeUdaaeUeaqau'
ans2='c`b bk`kj`KbababcaKbacaKiacki'

while True:
  for c in characters:
    x=subprocess.check_output(['./mask',s+c]).decode().split("\n")
    print(x[1],ans[0:len(x[1])],s+c)
    if x[1]==ans[0:len(x[1])] and x[2]==ans2[0:len(x[2])]:
      print(s)
      s+=c

