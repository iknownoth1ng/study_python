from threading import Timer
import random

class Code:
    def __init__(self):
        self.make_cached()
    
    def make_cached(self,interval=10):
        self.cache=self.make_code()
        print(self.cache)
        self.t=Timer(interval,self.make_cached)
        self.t.start()
    
    def make_code(self,n=4):
        res=''
        for _ in range(n):
            s1=str(random.randint(0,9))
            s2=chr(random.randint(65,90))
            res+=random.choice([s1,s2])
        return res
    
    def check(self):
        while True:
            code=input("请输入验证码==>: ").strip()
            if code.upper()==self.cache:
                print('密码输入正确！')
                self.t.cancel()
                break
            
    
if __name__ == "__main__":
    c=Code()
    c.check()
