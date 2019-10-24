#coding:utf-8
'''''
python 对一个函数执行速度控制的演示，原理和 对网速控制比较类似，这里更简单
'''
import time

def RateLimited(maxsec):
    ''''速度控制修饰函数'''
    minInterval = 1.0 // float(maxsec)  # 时间间隔
    def decorate(func):
        #使用数组 记录上一次的时间，利用闭包还是蛮方便的
        lastTimeCalled = [0.0]
        def rateLimitedFunction(*args,**kargs):
            elapsed = time.time() - lastTimeCalled[0]
            #计算剩余时间
            leftToWait = minInterval - elapsed
            if leftToWait>0:
                #时间未到先暂停一会
                time.sleep(leftToWait)
            ret = func(*args,**kargs)
            #更新时间
            lastTimeCalled[0] = time.time()
            return ret
        return rateLimitedFunction
    return decorate
 

@RateLimited(0.5)  # 每秒最多调用几次
def PrintNumber(num):
    print(num)
 
if __name__ == "__main__":
    start = time.time()
    print("打印1,2,3... 每2秒打印一个")
    for i in range(1,10):
        PrintNumber(i)  
    print(time.time()-start)