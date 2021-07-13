'''from functools import reduce
def square(a):
    return a*a
res = square(5)
print(res)
f= lambda a,b : a+a
result = f(5,5)
print(result)
#map filter reduce
def is_even(n):
    return n%2==0
hums = [13,4,2,34,32,56,684,34,562,34,365,6,67,843,23,43]
evens = list(filter(is_even,hums))
print(evens)
evenn = list(filter(lambda n :n%2==0,hums))
print(evenn)
def update(n):
    return(n+2)
doubles =list( map (lambda n:n*2,evenn))
print(doubles)
def add_all(a,b):
    return a+b
sum = reduce(add_all,doubles)
print(sum)
summ = reduce(lambda a,b :a+b,doubles)
print(summ)'''
#added a comment

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart_div(div)
div1(2,4)




