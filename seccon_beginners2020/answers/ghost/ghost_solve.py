import subprocess




def execute(s):
  with subprocess.Popen(["gs","chall.gs"],stdout=subprocess.PIPE,stdin=subprocess.PIPE) as p:
    x=p.communicate(input=(s+"\n").encode())
  x=x[0].decode().split('\n')[-2].split()
  return x





f=open('output.txt')
ans=f.read()
f.close()
ans=ans.split(' ')







x=execute("ctf4b")
print(x)
print(ans)

characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-^\\[]_@:/.,!#$%&'()0=~|{}_?>`*<"

s="ctf"
while x!=ans:
  for ch in characters:
    x=execute(s+ch)
    print(s+ch)
    if x==ans[:len(x)]:
      s+=ch
      print(s)

print(x)
