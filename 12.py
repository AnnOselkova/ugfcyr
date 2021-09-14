print( 'a*x**2+b*x+c=0')
a= float(input('a='))
b= float(input('b='))
c= float(input('c='))

dis= b**2-4*a*c
print(dis)

if dis <0:
    print('no roots')
elif dis == 0:
    x= -b/(2*a)
    print(x)
else:
    x1=(-b + dis**0.5)/(2*a)
    x2=(-b - dis**0.5)/(2*a)
    print(x1,x2)
