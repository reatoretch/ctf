# CTF用に使いそうなコマンドのセットアップを済ませたDockerfileを作る
CTF汎用ubuntu環境を作ろうと思います。


# imageのビルドとrun,login
```bash
docker build -t ctf-env .
docker run -i -t --cap-add=SYS_PTRACE --security-opt="seccomp=unconfined" --name ctf ctf-env /bin/bash
docker exec -it  ctf bash
```


## pwn,reversingでとりあえずやること(commandという実行ファイルがある想定)
```bash
file command
strings command
strace command
ltrace command
objdump -S -d command
```


