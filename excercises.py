#bonus

def salary(year_of_service, bns):
    sal=5000
    if year_of_service >= 5:
        bonus=sal+(sal*bns)/100
        print ("bonus is ",bonus)
    else:
        print ("bonus is ",sal)

#salary(5,10) 


# greatest integer

def greatest(a,b):
    if a>=b:
        print ("a is greatest")
    else:
        print ("b is greatest")

#greatest(100,50)

#discount on purchase
def cost(purchase_quantity):
    if purchase_quantity>=10:
        print ("discount is 10%")
    else:
        print ("discount is 0%")

#cost(15)

#Rules of grading 
def result(marks,atd):
    if marks>=80:
        if atd>90:
            print("grade is A with honours")
        else:
            print("grade is A")
    elif marks>=60:
        print("grade is B")
    elif marks>=50:
        print("grade is C")
    elif marks>=40:
        print("grade is D")
    else:
        print("grade is E")

#result(90,80)


#attendence
def attendence(noa,noh):
    if (noa/noh)*100>=75:
       print("allowed for exams")
    else:
       print("not allowed for exams")

#attendence(40,50)
       
#Leap year
def leapyear(year):
    if year % 4 == 0:
        print("Year is a leap year")
    else:
        print("Not a leap year")

#leapyear(2000) 

#odd even number
def type(num):
    if num%2==0:
        print ("num is even")
    else:
        print ("num is odd")

#type(21)

#Simple interest
def SI(P,R,T):
    Simple_interest=(P*R*T)/100
    print ("Simple_interest:",Simple_interest)

P=200
R=5
T=2
SI(P,R,T)




            




