#Print first 10 natural numbers
def num():
    for num in range(1,10,2):
        print(num)

#num()


#To calculate sum of numbers
def calculate_sum():
    sum=0
    for i in range(1,50):
      sum=sum+i
    print(sum)

#calculate_sum()

#To calculate sum of even numbers from 10 to 20

def calculate_sum1():
    sum=0
    for i in range(10,20,2):
        sum=sum+i
        print(i)
    print(sum)

#calculate_sum1()

#To calculate square of each number in the list

def num_square():
    #numbers= [1,2,3,4,5]
    for i in range(1,5):
        square=i**2
        print(square)


#num_square()

#To calculate average of list of numbers
def average():
    numbers=[1,2,3,4,5,6]
    total=sum(numbers)
    length=len(numbers)
    avg=total/length
    print(avg)

#average()

#To print all even or odd numbers

def even_num():
    for i in range(1,10):
        if i%2==0:
            print('even number:',i)
        else:
            print('odd number:',i)

#even_num()

#For loop to generate a list of numbers from 9 to 50 divisible by 2
def num_div():
    for i in range (9,50):
        if i%2==0:
            print('numbers divisible by 2:',i)
        else:
            print('numbers not divisible by 2:',i)

#num_div()     

# Print numbers less than 5
def num1():
    print("I am here")
    n=1
    while n<=5:
        print (n)
        n=n+1
#num1()

#Check how many times a given number can be divided by 3 before it is less than or equal to 10
def n():
    num = 90
    while num >= 10:
        num = num / 3
        print(int(num))

#n()
            
# Print even and odd numbers between 1 to 10
            
def n1():
    n=1
    while n<10:
        if n%2==0:
            print(n,"even number")
        else:
            print(n,"odd number")
        n=n+1

#n1()

def num():
    for x in range (1500,2701):
        if (x%7==0) and (x%5==0):
            print(x)

#num



#temp()

def numb():
    for x in range (0,6):
        if (x==3) or (x==6):
            continue
    print (x)
#numb()
def fib():
    a, b = 0, 1
    for i in range(10):
        c = a + b
        if c>100:
            break
        print(c, end=' ')
        a = b
        b = c
#fib()

def dogage():
    hage= int(input("Dod age in human age:"))
    if hage<0:
        print("Age should be apositive number.")
        exit()
    elif hage<=2:
        dogage=hage*10.5
        print("dogage", dogage)
    else:
        dogage=21+(hage-2)*4
        print("dogage", dogage)
#dogage()

def letter():
    letter=input("enter key")
    if letter in ("a,e,i,o,u"):
        print("alphabet is vowel")
    else:
        print("alphabet is consonent")
#letter()

def numbers():
    numbers=(40,50)
    a,b=numbers
    sum=a+b
    product=a*b
    if a*b>=100:
        print("product of numbers is",product)
    else:
        print("sum of numbers",sum)
numbers()


  
 

    

    

        



    


    




        



        

