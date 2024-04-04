#Print first 10 natural numbers
def num():
    for num in range(0, 10):
        print(num)

#num()


#To calculate sum of numbers
def calculate_sum():
    sum=0
    for i in range(1,50):
      sum+=i
    print(sum)

#calculate_sum()

#To calculate sum of even numbers from 10 to 20

def calculate_sum():
    sum=0
    for i in range(10,20,2):
        sum=sum+i
        print(sum)

#calculate_sum()

#To calculate square of each number in the list

def num_square():
    numbers= [1,2,3,4,5]
    for i in numbers:
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

num_div()         


        

