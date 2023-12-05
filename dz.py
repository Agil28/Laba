a=int(input())
b=int(input())
c=int(input())
d=b**2-4*a*c
if d<0:
    print('Корней нет')
elif d==0:
    print('Уравнение имеет 1 корень', -b/2*a)
else:
    print('1-й корень', (-b+d**0.5)/(2*a))
    print('2-й корень', (-b-d**0.5)/(2*a))
