# phyton program for a fibonacci numbers
n = int(input("enter the length "))
def fib(n):

  #first two terms
    a,b = 0,1
     
    if n == 1:
        print(a)
        
    else:
            print(a)
            print(b)
            
            for i in range(2,n):
                c = a+b
                a = b
                b = c
                print(c)
fib(n)
