import subprocess

def execute(s):
  s=(s+"\n").encode()
  x=subprocess.Popen(['gs','chall.gs'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
  y=x.communicate(s)[0].decode()
  return y.split('\n')[-2]

arr = {}
ans = ""

with open('output.txt') as f:
  l = f.read()
  l = l.split(" ")

for j in range(50):
  for i in range(0x20,0x80):
    add = execute(str(ans)+str(chr(i)))
    arr[str(ans)+str(chr(i))] = str(add)[:-1]
  if len(ans) == len(l):
    print(ans)
    exit()
  if len(ans) > 0:
    for x,y in arr.items():
      if str(l[len(ans)]) == str(y).split(" ")[-1]:
        ans = str(x)
        print(ans)
        break
  else:
    for x,y in arr.items():
      if l[0] == str(y):
        ans = str(x)
        print(ans)
  arr = {}