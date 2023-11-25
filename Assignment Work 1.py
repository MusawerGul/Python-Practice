#Exercise:1

num=int(input("Enter a number:"))
if num%2==0:
    print("Given Number is Even")
else:
    print("Given number is odd")

#Exercise: 2

year=int(input("Enter a Year To check:"))
if(year%4==0 and year%10!=0):
    print("This Year is a leap Year")
else:
    print("This is not a Leap Year")

#Exercise: 3

age=int(input("Enter your age:"))
if age>=18:
   print("You are an Adult")
else:
    print("You are a minor")

#Exercise: 4

username="Musawer Gul"
password="1214"

input_username=input("Enter Username:")
input_password=input("Enter password:")
if input_username==username and input_password==password:
    print("Logged In successfully")
else:
    print("Login failed")

#Exercise: 5

num=int(input("Enter a Number:"))
if num>0:
    print("Given Number Is Possitive")
elif num<0:
    print("Given Number is Negative")
else:
    print("Given number is zero")

#Exercise: 6
 
num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
num3=int(input("Enter num3"))
if num1<num2 and num2<num3:
    print(num3)
elif num1<num2 and num2>num3:
    print(num2)
elif num1>num2 and num2>num3 or num1>num3:
    print(num1)

#Exercise: 7

score=float(input("Enter Your Marks:"))
if score>=90:
    print("Your Grade Is A")
elif score>=80:
    print("Your Grade is B")
elif score>=70:
    print("Your Grade is C")
elif score>=60:
    print("Your Grade is D")
else:
    print("You are Fail")

#Exercise: 8

num=int(input("Enter a Number:"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print("Given number isnot a prime number.")
            break
    else:
        print("Given Number is a Prime NUmber")
else:
    print("Given Number isnot a Prime Number")    

#Exercise: 9 and Exercise: 2 are same.

#Exercise:10

num1=int(input("Enter a Num1:"))
num2=int(input("Enter a Num2:"))
if num1>num2:
    print(num1, "is greater")
elif num1<num2:
    print(num2, "is greater")
elif num1==num2:
    print("Both Numbers are Equal")