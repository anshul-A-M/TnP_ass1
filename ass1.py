#Name:Anshul Mahajan
#Enrollment:0103IS231029
#Batch:5
#Batch Time:10:30 to 12:10
# if else problem 
# Q 1

a = int(input("Enter a number "))
if a > 0:
    print(" the number is Positive")
elif a < 0:
    print("the number is Negative")
else:
    print("Zero")

#Q 2
b = int(input(" enter the number ")) 
if b%2==0 :
    print ("the number is even ")
else:
    print("the number is odd ") 
    
# Q3 
c = int(input(" enter the year  ")) 
if c%400==0 :
    print ("The year is leap year ")
else:
    print("The year is not leap year  ")     

# Q4 
num1 = int(input("Enter a number "))    
num2 = int(input("Enter a number "))    
if num1>num2:
    print (" he num1 is greater ")
elif num1<num2:
    print("the num2 is greater ")       
else :
    print("bothe numbers are equal  ")  

# Q5
age = int(input("Enter the age "))
if age >=18:
    print("right to vote ")
else :
    print(" not eligible to vote ")    

#Q6
w = input("Enter the character ").lower()
if w in ['a','e','i','o','u']:
    print (" the character is vowel ")
else :
    print (" the character is consonent ") 

# Q7
num3 = int(input("Enter the number "))
if num3 %5==0 :
    print ("the number is divisible by 5 ")
else :
    print ("not divisible ") 

#Q8 
num4 = int(input("Enter the number "))
if 0<=num4<=9:
    print ("The number is single digit ")
elif 10<=num4<=99:
    print ("The number is double  digit ")    
else :
    print ("more than two digits ")
#Q9 
num5 = float(input(" enter the student number "))
if num5<=40:
    print ("fail  ")
else :
    print("the student is pass")            
       
#Q10 
num6 = int(input("enter the number "))
if num6%3==0 and num6%7==0:
    print (" multiple of both 3 and 7")
else :
    print("ot a multiple ")    
    
#Ladder and  Nested if 
#Q1
a= int (input("Enter the number : "))
b= int (input("Enter the number : "))
c= int (input("Enter the number : "))
if a>=b and b>= c:
    print("a is the grestest ")
elif b>=a and  b>=c:
    print ("b  is the grestest")   
else :
    print("c is the grestest")    
#Q2
age = int (input("enter the age : "))
if  age < 13 :
    print (" the person is child") 
elif 13<= age <=19:
    print(" the person is teenager ")
elif 20<= age <=59:
    print(" the person is Adult  ")   
else :
    print (" the person is senior ")     
#Q3
marks = int (input("enter the marks  : "))
if  marks  < 35:
    print (" fail") 
elif 35<= marks  <=49:
    print(" D grade  ")
elif 50<= marks  <=74:
    print(" C grade  ")   
elif 75<= marks  <=89:
    print(" B grade  ")       
else :
    print (" A grade  ")   
#Q4 
a= input("Enter the side  : ")
b= input("Enter the side  : ")
c= input("Enter the side  : ")
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
#Q5
ch = input("Enter the character :")
if ch.isupper():
    print(" upper case ")
elif ch.islower():
    print(" lower case ")   
elif ch.isdigit():
    print("  Digit  ") 
else :
    print("special symbols ")
#Q6
unit =int( input(" enter the units of electricity "))
if unit <=100 :
    bill = unit*5
elif unit <=200 :
    bill = (100 * 5) + (unit - 100) * 7
else :     
     bill = (100 * 5) + (100 * 7) + (unit - 200) * 10
print( bill )              
#Q7




#Q8
year = int (input("Enter  the year "))
if year % 100 ==0:
   print ("Century year ")
else :
   print ("not a century yeear ")   
if (year % 400 == 0) :
    print("Leap Year")
else:
    print("Not a Leap Year")
#Q9
bmi = float(input("Enter the bmi :"))
if bmi<18.5:
    print("underweight")
elif bmi<25:
    print("normal")
elif bmi<30:
    print("overweight")
else :
    print(" obese")
#Q10
a=int(input("enter the number "))
b=int(input("enter the number "))
c=int(input("enter the number "))
if a<b:
    if a<c :
       smallest= a
    else:
        smallest = c
else:
    if b < c:
        smallest = b
    else:
        smallest = c        
print("smallest number ",smallest )

# For Loop
#Q1


#Q2
n= int(input(" enter n : " ))
count= 0
num = 2
while count < n :
    is_prime=True
    for i in range (2,int(num**0.5)+1) :
        if num%i ==0:
            is_prime=False
            break
    if is_prime:
        print(num, end=" ")
        count+=1
    num+=1    
   # Q3
for a in range (1,500):
   if a%3==0:
      sum =0 
      for d in str(a):
       sum += int(d)
      if sum <=10:
       print(a,end= " ")  
# Q4 
n= int(input("enter the height :"))
for i in range (1,n+1):
    star = "*"* (2*i-1)
    print(star.center(2*n-1))
#Q5
s= input("enter a string :").lower()
alphabets= "abcdefghijklmnopqrstuvwxyz"
for ch in alphabets:
    if ch  not in s: 
        print (" not a pangram ")
        break
else :
    print("pangram ")    
   # Q6
for i in range (2 ,100):
    for j in range (2,i):
       if i%j==0:
           break
    else :
        for k in range (2,i+2):
            if (i+2)%k==0:
                break 
        else :
            print(f"({i},{i+2})")       
#Q7
num = int(input("Enter a number: "))
sum = 0
for d in str(num):
    sum += int(d)
if num%sum==0:
    print("hashad number ")
else :
    print (" not a harshad number ")
#Q8


#Q9
n= int(input("enter n : "))
total=0
for i  in range (1,n+1):
    total+=i*i
print("sum : ",total)    
#Q10
num = int(input(" enter the number :"))
sum=0
for d in str(num):
    fact=1 
    for i in range (1,int(d)+1):
        fact *=i
    sum += fact
if sum == num :
    print("strong number  ")
else:
    print("not a strong number ")

#while loops 
#Q11


#Q12 


#Q13
num = input("Enter a number: ")
i = 0
while i < len(num):
    if num[0] == "0":
        print("Not a Duck Number")
        break
    elif "0" in num:
        print("Duck Number")
        break
    else:
        print("Not a Duck Number")
        break
#Q4
#Q15
num = int(input ("enter the number : "))
i=2 
j=1
while num >1:
    if num %i==0:
        j = i
        num//=i
    else:
        i+=1
print ("largest prime factor ",j)        
#Q16
while True:
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("Palindrome ")
        break
    else:
        print("Not a palindrome")
#Q17 



#Q18 
#Q19
#Q20
balance = 0 
while True :
    print("\n--- ATM menu ---")
    print("1 checkbalance ")
    print("2 deposit money ")
    print("3 withdraw money ")
    print("4 exit  ")
    choice = int(input(" enter choice "))
    if choice ==1:
        print (" balance :",balance  )
    elif choice == 2:
        amt = int(input("Enter amount to deposit: "))
        balance += amt
        print("Deposited:", amt)
    elif choice ==3:
         amt = int(input("Enter amount to withdraw: "))
         if amt <= balance:
            balance -= amt
            print("Withdrawn:", amt)
         else:
            print("Insufficient Balance!")
    elif choice == 4:
       print("Exiting ATM. Goodbye!")
    break
else:
    print("Invalid choice, try again.")
