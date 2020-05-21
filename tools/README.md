# ctf tools
floursがctf toolを気ままに作ります。

### RSA.py
ソースコード中のnとeを指定して実行します
factordb,fermat法,愚直な因数分解,Wiener's Attackを実装しています。
大体10000回くらいループすると諦めるのでもっと試したいならRSA/RSA.pyの中のループ回数をよしなに設定してください 

### BruteForceIfKnowRelationship.py
数値を求めるときに数値が目的の値より高いか低いかがわかるときに使う
そんなことはほぼないけどもksnctfq17とかでは使える(というかそのために作った)
最初に1,10,100と桁を上げていってその後上の桁から数字を合わせていく



