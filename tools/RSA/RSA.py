from fractions import Fraction
import requests
from urllib import request
from lxml import html


class RSA_simple:   

    def try_factordb(self,n,e):
        base_URL="http://factordb.com/"
        html_tag=self.get_html_tag(base_URL+'index.php?query='+str(n))
        prime1=html_tag.xpath("/html/body/table[2]/tr[3]/td[3]/a[2]")
        prime2=html_tag.xpath("/html/body/table[2]/tr[3]/td[3]/a[3]")
        html_tag=self.get_html_tag(base_URL+prime1[0].attrib['href'])
        num1=html_tag.xpath('/html/body/form/center/input[1]')[0].value
        html_tag=self.get_html_tag(base_URL+prime2[0].attrib['href'])
        num2=html_tag.xpath('/html/body/form/center/input[1]')[0].value
        return int(num1),int(num2) 
       
    def try_fermat(self,n,e):
        return self.fernmat(n)

    def try_factorial_from2(self,n,e):
        return self.small_prime(n)

    def try_WinersAttack(self,n,e):
        return self.wiener(n, e)


    def get_html_tag(self,url):
        data = request.urlopen(url)
        raw_html = data.read()
        html_tag = html.fromstring(str(raw_html.decode()))
        return html_tag

    
    def is_prime(self,q):
        q = abs(q)
        if q == 2:
            return True
        if q < 2 or q & 1 == 0:
            return False
        return pow(2, q-1, q)

    def small_prime(self,modulus):
        for i in range(100000):
            if self.is_prime(i):
                if modulus % i == 0:
                    return i, modulus / i
            else:
                pass
            i += 1
        return 0,0


    def isqrt(self,n):
        x = n
        y = ( x + n // x ) // 2
        while y < x:
            x = y
            y = ( x + n // x ) // 2
        return x

    def fernmat(self,n):
        x = self.isqrt(n) + 1
        y = self.isqrt( x * x -n )
        ret=0,0
        for i in range(100000):
            w = x * x -n -y * y
            if w == 0:
                ret=x+y,x-y
            elif w > 0:
                y += 1
            else:
                x += 1
        return ret
    

    def continued_fractions(self,n, e):
        cf = [0]
        while e != 0:
            cf.append(int( n / e ))
            N = n
            n = e
            e = N % e
        return cf

    def calkKD(self,cf):
        kd = list()
        for i in range(1, len(cf) + 1):
            tmp = Fraction(0)
            for j in cf[1:i][::-1]:
                tmp = 1 / (tmp + j)
            kd.append((tmp.numerator, tmp.denominator))
        return kd
    
    def int_sqrt(self,n):
        def f(prev):
            while True:
                m = (prev + n // prev) // 2
                if m >= prev:
                    return prev
                prev = m
        return f(n)

    def calcPQ(self,a, b):
        if a * a < 4 * b or a < 0:
            return None
        c = self.int_sqrt(a * a - 4 * b)
        p = (a + c) // 2
        q = (a - c) // 2
        if p + q == a and p * q == b:
            return (p, q)
        else:
            return None

    def wiener(self,n, e):
        kd = self.calkKD(self.continued_fractions(n, e))
        for (k, d) in kd:
            if k == 0:
                continue
            if (e * d -1) % k != 0:
                continue
            phin = (e * d -1) // k
            if phin >= n:
                continue
            ans = self.calcPQ(n - phin + 1, n)
            if ans is None:
                continue
            return (ans[0], ans[1])


    
    
