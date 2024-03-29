import time 

print(time.perf_counter())  # 返回系统运行时间
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
	a = '*' * i
	b = '.' * (scale - i)
	c = (i/scale)*100
	dur = time.perf_counter() - start
	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
	time.sleep(0.2)
print("\n"+"执行结果".center(scale//2, '-'))
