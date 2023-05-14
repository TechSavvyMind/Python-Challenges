###Welcome to our Python programming challenges repository! Each challenge file in this repository contains a problem statement, sample input and output, and a solution code that satisfies the test cases provided. ###
###To navigate through the challenge files, we recommend that users pay close attention to the comments in the code. The problem statement is provided at the top of the file as a comment, while the sample input and output are presented as comments within the code.###
###It's important to note that the sample input and output may not cover all possible edge cases. The solution code provided is intended as a reference for users to check their work against the expected output.###
###Users are encouraged to attempt to solve the problem on their own before checking the solution code, as this will help improve their problem-solving skills. Once users have written their solution, they can test their code against the sample inputs provided and submit their code for review through a pull request.###






#FUNDAMENTALS OF PYTHON PROGRAMMING#


1.INPUT&OUTPUT
 
#Hello World
print("Hello World")

#Hello World with tab
print("Hello World\tHello World")

#Hello World with new line
print("Hello World\nHello World")

#Integer Input
a=int(input())
print(a)

#Float Input
a=float(input("enter a number:"))
print("%.2f"%a)

#Character Input
a=input("enter a character:")
print(a)

#String Input
a=input("enter a string:")
print(a)

#Ascii-I
a=input("enter the character:")
print("The ascii value is:",ord(a))

#Ascii-II
a=int(input("enter a ascii value:"))
print(chr(a))


2.OPERATORS

#Sum and Difference
a=int(input('enter a firt number'))
b=int(input('enter a second number'))
print(a+b)
print(a-b)

#Product and Division
a=int(input())
b=int(input())
print(a*b)
print(a//b)
print(a%b)

#Swapping of two numbers
a=int(input())
b=int(input())
a,b=b,a
print('after swapping',a)
print('after swapping',b)

#Swapping without third variable
a=int(input())
b=int(input())
temp=a
a=b
b=temp
print(a)
print(b)

#Average Calculation
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=(a+b+c+d+e)/5
print("%.2f"%f)

#Alice in Wonderland
#SAMPLE INPUT  :
23
SAMPLE OUTPUT:
5


def sum_of_digit(n):
    if n<10:
        return n
    else:
        return n%10 + sum_of_digit(n//10)
number=int(input("Enter number: "))
print("Sum of digit is",sum_of_digit(number))

#Area Calculation
#Sample Input: 
5
5
4
2.0
Sample Output: 
25
20
12.56

a=int(input())
b=int(input())
c=int(input())
d=float(input())
e=a*a
f=b*c
g=3.14*d*d
print(e)
print(f)
print("%.2f"%g)

#Fencing the ground
#SAMPLE  INPUT:
50
20
SAMPLE OUTPUT:
Required length is 140 m
Required quantity of carpet is 1000 sqm.

a=int(input())
b=int(input())
c=2*(a+b)
d=a*b
print(" required length is %d m"%c)
print("Required quantity of carpet is %d sqm"%d)

#Power of a Number
a=int(input())
b=int(input())
c=pow(a,b)
print(c)

#Simple Interest
#Sample Input:
p=15000
t=2
r=2.8
Sample Output:
840.00

p=int(input("Enter the principal amount:"))
t=int(input("Enter the time period:"))
r=float(input("Enter the rate of interest:"))
simpleinterest=p*t*r/100
print("%.2f"%simpleinterest)

#Splitting into Teams
#Sample Input :
total=60 
no of members in team=8
SAMPLE OUTPUT:
The number of students in each team is 7 and left out is 4

a=int(input())
b=int(input())
c=a//b
d=a%b
print("The number of students in each team is %d and left out is %d"%(c,d))

#Three Idiots
#Sample Input:
x1=2
x2=4
y1=10
y2=15
Sample Output:
Binoy's house is located at (6.0,9.5)#Midpoint

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
m1=(x1+x2)/2
m2=(y1+y2)/2
print("Binoy's house is located at (%.1f,%.1f)"%(m1,m2))

3.DECISION MAKING

#Greatest of two numbers

a=int(input())
b=int(input())
if a>b:
      print("%d is greater than %d"%(a,b))
elif a<b:
      print("%d is less than %d"%(a,b))
else:
      print("%d is equal to %d"%(a,b))

#Vowel Or Consonants

char=input()
if char in "aeiouAEIOU":
     print("Vowel")
elif char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
     print("Consonant")
else:
     print("Not an alphabet")

#Grading System
#
Marks Scored   Grade
100                            S
(90,100)                    A
(80,90)                      B
(70,80)                      C
(60,70)                      D
(50,60)                      E
<50                             F

grade=int(input())
if grade==100:
 print("S")
elif grade>=91 and grade<=100:
 print("A")
elif grade>=81 and grade<=90:
 print("B")
elif grade>=71 and grade<=80:
 print("C")
elif grade>=61 and grade<=70:
 print("D")
elif grade>=51 and grade<=60:
 print("E")
else:
 print("Invalid Input")

#Profit or Loss
# Sample Input1:
60.0
4
Sample Output1:
Enter the price of a dozen mangoes
Enter the price at which 1 mango is being sold
Loss : Rs.12.00

cp=float(input("Enter the price of a dozen mangoes:"))
sp=float(input("Enter the price at which 1 mango is being sold:"))
tp=sp*12
if cp>tp:
    print("\nLoss: Rs.%.2f"%(cp-tp))
elif cp<tp:
    print("\nProfit: Rs.%.2f"%(tp-cp))
else:
    print("\nNo profit nor loss")

#Fee Collection
# Table

Student type                            studenttype denoted as                 fee details
merit seat days scholar           MSDS                                              tution fee+bus fee
merit fee hosteller                      MSH                                                 tution fee+hostel fee
management seat days scholarMGSDS                                        150% of tution fee+bus fee
management seat hosteller         MGSH                                           150% of tution fee+hostel fee

Sample Input and Output:

Enter the student type

MSH

Enter tuition fee

40000

Enter hostel fee

50000

The fees to be paid by the student is Rs.90000.00

print("Enter the student type")
a=input()
if a=="MSDS":
 print("Enter tuition fee")
 tutionfee=int(input())
 print("Enter bus fee")
 busfee=int(input())
 print("The fees to be paid by the student is Rs.%.2f"%(tutionfee+busfee))
elif a=="MSH":
 print("Enter tuition fee")
 tutionfee=int(input())
 print("Enter hostel fee")
 hostelfee=int(input())
 print("The fees to be paid by the student is Rs.%.2f"%(tutionfee+hostelfee))
elif a=="MGSDS":
 print("Enter tuition fee")
 tutionfee=int(input())
 print("Enter busfee")
 busfee=int(input())
 print("The fees to be paid by the student is Rs.%.2f"%(1.5*tutionfee+busfee))
elif a=="MGSH":
 print("Enter tuition fee")
 tutionfee=int(input())
 print("Enter hostel fee")
 hostelfee=int(input())
 print("The fees to be paid by the student is Rs.%.2f"%(1.5*tutionfee+hostelfee))
else:
 print("invalid")

#Y2K Problem Detector
#Sample Input and Output:

Enter Year of Birth

62

Enter Current year

99

Your age is 37

print("Enter Year of Birth")
yb=int(input())
print("Enter Current year")
cy=int(input())
if cy<yb:
    print("Your age is %d"%((100-yb)+cy))
elif yb==cy:
    print("Your age is 0")
else:
    print("Your age is %d"%(cy-yb))
    
#Lab Allocation
#Sample Input and Output 1:
Enter x
30
Enter y
40
Enter z
20
L3 has the minimal seating capacity

print("Enter x")
x=int(input())
print("Enter Y")
y=int(input())
print("Enter z")
z=int(input())
if x<y and x<z:
    print("L1 has the minimal seating capacity")
elif y<x and y<z:
    print("L2 has the minimal seating capacity")
else:
    print("L3 has the minimal seating capacity")

#Gardening I
#Dora is interested so much in gardening and she plants more trees in her garden.
 She plants trees in a rectangular fashion with the order of rows and columns and numbered the trees in row-wise order.
 She planted the mango tree only in a ""1st row, 1st column and last column. ""
So given the tree number, your task is to find whether the given tree is a mango tree or not?
#Sample Input:

5

5

11  

Sample Output:

Yes

a=int(input())
b=int(input())
c=int(input())
if c<b:
    print("Yes")
elif c%b==0:
    print("Yes")
elif c%b==1:
    print("Yes")
else:
    print("NO")

#Hotel Tariff Calculator
#The room rent is 20% high during peak seasons [April-June, November-December] .

month=int(input())
rent=float(input())
numberofdays=int(input())
if  month==1 or month==2 or month==3 or month==7 or month==8 or month==9 or month==10:
    print("Hotel Tariff: Rs.%.2f"%(rent*numberofdays))
elif month==4 or month==5 or month==6 or month==11 or month==12:
    print("Hotel Tariff: Rs.%.2f"%(1.2*rent*numberofdays))
else:
    print("Invalid Input")

#RGY Lights
#Write a program that takes the following floating point numbers as input:

our current speed in meter per seconds (s)
the distance to the light in meters (d)
the time until it turns red in seconds (t)
displays a message indicating whether we will beat the light. 
You may assume that the input won't be such that we reach the light at exactly the same time it turns red
#Sample Input 1:

59.99

1.0

60.0 

Sample Output 1:

no

a=float(input())
b=float(input())
c=float(input())
s=c/b
if s>a:
    print("no")
else:
    print("yes")

#Budget
#budget limit =15000$
 Blast rifle                  rs.350.34
 Visual sensors        rs.230.90
 auditory sensors    rs.190.55
 arms                         rs.125.30
 legs                            rs.180.90
#Sample Input:

20 10 14 3 9

Sample Output:

yes

a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
t=(a*350.34+b*230.90+c*190.55+d*125.30+e*180.90)
if t<=15000:
    print("yes")
else:
    print("no")

#Sece Dining
#Input Format:

The first line of the input is a string. The input may be “front” or “rear”.

The second line of the input is an integer. The input may be 1 or 2.

Output Format:

Output consists of the string “Left Handed” or “Right Handed”.

a=input()
b=int(input())
if a=="front":
    if b==1:
        print("Left Handed")
    else:
        print("Right Handed")
else:
    if b==1:
        print("Right Handed")
    else:
        print("Left Handed")

#Intersection of a Circle
#output=="circles tangential”, “The circles overlap”, “The circles do not overlap”

import math
x1=int(input())
y1=int(input())
r1=int(input())
x2=int(input())
y2=int(input())
r2=int(input())
i=math.sqrt((x1-x2)**2+(y1-y2)**2)
if i==(r1+r2):
    print("The circles are tangential")
elif i>(r1+r2):
    print("The circles do not overlap")
else:
    print("The circles overlap")

#Microwave Oven
#A microwave oven manufacturer recommends that when heating two items, 
add 50% to the heating time, and when heating three items double the heating time. 
Heating more than three items at once is not recommended. 
Write a program that asks the user for the number of items and the single-item heating time.

print("Enter the number of items")
a=int(input())
print("Enter the single item heating time")
b=float(input())
if a==4:
  print("Number of items is more")
elif a==3:
  print("The recommended heating time is %.2f"%(2*b))
elif a==2:
  print("The recommended heating time is %.2f"%(1.5*b))
else:
  print("The recommended heating time is %.2f"%(b)) 

#control structures
#Amoeba Multiplication
# The size of the amoeba on month 1, 2, 3, 4, 5, 6,7 ..will be 0, 1, 1, 2, 3, 5, 8 respectively.

s=0
b=0
c=1
print("Enter the number of Months:")
a=int(input())
if a==1:
    print("The amoeba size is 0")
elif a==2:
    print("The amoeba size is 1")
else:
    for i in range(a-2):
         s=b+c
         b=c
         c=s
    print("The amoeba size is %d"%s)

#Factorial
a=int(input())
s=1
temp=0
for i in range(1,a+1):
    s=s*i
    if a==s:
        temp=1
        break
if temp==1:
    print("yes")
else:
    print("no")

#Sum of digits
#Sample Input:
719
Sample Output:
17
a=input()
b=len(a)
a=int(a)
s=0
for i in range(b):
    s=s+a%10
    a=a//10
print(s)

#Freindly pair
#For example,6 and 28 are Friendly Pair.
(Sum of divisors of 6)/6 = (Sum of divisors of 28)/28.
a=int(input())
b=int(input())
s1=0
s2=0
for i in range(1,a+1):
    if a%i==0:
        s1=s1+i
s1=s1/a
for i in range(1,b+1):
    if b%i==0:
        s2=s2+i
s2=s2/b
if s1==s2:
    print("Friendly pair")
else:
    print("Not Friendly pair")

#Harshad Number
#number divisible by sum of digits
a=input()
b=len(a)
a=int(a)
c=a
s=0
for i in range(1,a+1):
    s=s+a%10
    a=a//10
if (c%s)==0:
    print("Harshad Number")
else:
    print("Not Harshad Number")

#LCM of 2 numbers
a=int(input())
b=int(input())
c=a*b
for i in range(1,c+1):
    if((i%a)==0)and((i%b)==0):
        break
print("LCM of %d and %d is %d"%(a,b,i))

#Palindrome of a number
n=int(input())
rev=0
temp=n
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if temp==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Perfect Number
#For example, 6 is a perfect number.
The divisors of 6 are 1, 2 and 3.
1 + 2 + 3 = 6.
a=int(input())
sum=0
for i in range(1,a+1):
    if a%i==0:
        while a>0:
            res=a%10
            sum=sum+res
            a=a//10
if a==sum:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

#Prime Number
a=int(input())
count=0
for i in range(2,a//2):
    if a%i==0:
        count+=1
if count==0:
    print("Prime Number")
else:
    print("Not a Prime")

#Prime numbers in  a range
a=int(input())
b=int(input())
for i in range(a,b+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)

#Reverse of  a Number
a=int(input())
s=0
while a!=0:
    b=a%10
    s=s*10+b
    a=a//10
print(s)

#Strong Number
a=int(input())
s=1
c=0
t=a
while a!=0:
    b=a%10
    for i in range(1,b+1):
        s=s*i
    c=c+s
    s=1
    a=a//10
if c == t:
    print("Strong Number")
else:
    print("Not a Strong Number")
    
#Sum of n natural numbers
n=int(input())
s=0
for i in range(1,n+1):
    s=s+i
print(s)

#Sum of numbers in range
n1=int(input())
n2=int(input())
s=0
for i in range(n1,n2+1):
    s+=int(i)
print(s)

#SERIES

#series=1,4,9,16,25,....
n=int(input())
s=1
for i in range(1,n+1):
    s=i**2
    print(s,end=' ')

#series  6,11,21,36,56,..
n=int(input())
s=6
for i in range(1,n+1):
    print(s,end=' ')
    b=5*(i)
    s=s+b

# series --- 3, 9, 27, 81,...,... 
n=int(input())
s=3
for i in range(n):
    print(s,end=' ')
    s=s*3

#series --- 0.5,1.5,4.5,13.5,...
n=int(input())
s=0.5
for i in range(0,n):
    print(s,end=' ')
    b=3**i
    s+=b

#series --- 121,225,361,... 
n=int(input())
s=11
for i in range(1,n+1):
    print(s**2,end=' ')
    s+=4

#series --- 0,2,8,14,...,34 
n=int(input())
a=0
b=2
c=2
print(a, b,end=' ')
for i in range(0,n):
    if i%2==0:
        c+=4
    b+=c
    print(b,end=' ')

# series --- 1, 2.0, 3.0, 6.0, 9.0, 18.0, 27.0,... 
a=1
print(a,end=' ')
k=0
for i in range(n):
    a+=3**k
    if i%2==1:
        k=k+1
    print("%.1f"%a,end=' ')
        
#series 4, 5, 9, 18, 34,...
n=int(input())
a=4
for i in range(1,n+1):
    print(a,end=' ')
    b=i**2
    a+=b

#series 2, 3, 8, 63, 3968
n=int(input())
a=2
print(a,end=' ')
for i in range(n-1):
    a=(a**2)-1
    print(a,end=' ')

#series 95.0, 115.5, 138.0,..., 189.0 
n=int(input())
a=95.0
b=20.5
print(a,end=' ')
for i in range(n):
    a+=b
    print(a,end=' ')
    b=b+2

#FUNCTIONS

#Arthimetic operators
def artopr(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a//b)
    print(a%b)
b=int(input())
c=int(input())
artopr(b,c)

#Square root
def sqroot(a):
    print(a**2)
b=int(input())
sqroot(b)

#cuberoot
def cuberoot(a):
    print(a**3)
b=int(input())
cuberoot(b)

#RECURSION

#Binary equivalent using recursion
def binrecur(n):
    if n==0:
        return 0
    else:
        return (n%2+10*(binrecur(int(n//2))))
n=int(input())
print(binrecur(n))

#Fibonacci series
def fibonacci(a,b,c,d):
    s=a+b
    a=b
    b=s
    print(b,end=" ")
    d+=1
    if d==c:
        return
    else:
        return fibonacci(a,b,c,d)
c=int(input())
d=0
fibonacci(-1,1,c,d)

#Odd or Even
def num(n):
    if n%2==0:
        return "Even!"
    else:
        return "Odd!"
n=int(input())
print(num(n))

#Factorial
def factorial(a):
    if a==1 or a==0:
        return 1
    else:
        return (a*factorial(a-1))
a=int(input())
print(factorial(a))

#LCM of 2 numbers
def lcm(a,b,s):
    if((s%a==0) and(s%b==0)):
        return print(s)
    elif s<a*b:
        lcm(a,b,s+1)
    else:
        return a*b
a=int(input())
b=int(input())
s=1
print(lcm(a,b,s))

#decimal to binary 
def binary(a):
    if a==0:
        return 0
    else:
        return (a%2+10*(binary(int(a//2))))
a=int(input())
print(binary(a))

#LIST

#create a list
a=int(input())
l=[]
for i in range(a):
    b=input()
    l.append(b)
for i in range(a):
    print(l[i])

#Largest number in list
a=int(input())
l=[]
for i in range(a):
    b=int(input())
    l.append(b)
print(max(l))

#Odd or Even
n=int(input())
l=[]
e=[]
o=[]
for i in range(n):
    b=int(input())
    l.append(b)
for i in range(n):
    if l[i]%2==0:
        e.append(l[i])
    else:
        o.append(l[i])
print("The even list",e)
print("The odd list",o)

#Array mean
n=int(input())
l=[]
for i in range(n):
    b=int(input())
    l.append(b)
sum=0
for i in range(n):
    sum=sum+l[i]
print("%.1f"%(sum/n))

#sort the list
a=int(input())
l=[]
for i in range(a):
    temp=int(input())
    l.append(temp)
b=int(input())
for i in range(b):
    temp=int(input())
    l.append(temp)
for i in range(a+b):
    for k in range(a+b-1):
        if l[k]>=l[k+1]:
            l[k],l[k+1]=l[k+1],l[k]
print("Sorted list is:",l)

#Remove Duplicates
n=int(input())
l=[]
for i in range(0,n):
    temp=int(input())
    l.append(temp)
a=[]
for i in l:
    if i not in a:
        a.append(i)
print(a)

#second largest number
n=int(input())
l=[]
for i in range(n):
    temp=int(input())
    l.append(temp)
for i in range(n):
    for k in range(n-1):
        if l[k]>=l[k+1]:
            l[k],l[k+1]=l[k+1],l[k]
print(l[-2])

#swap the numbers
n=int(input())
l=[]
for i in range(n):
    temp=int(input())
    l.append(temp)
for i in range(0,n//2,2):
    l[i],l[-i-1]=l[-i-1],l[i]
print(l)

#DICTIONARY

#check key exist
dict={'A':1,'B':2,'C':3}
n=input()
print("Enter key to check:")
if n in dict.keys():
    print("Key is present and value of the key is:",dict[n])
else:
    print("Key isn't present")

#concatenate
d1={'A':1,'B':2}
d2={'C':3}
d1.update(d2)
print("Concatenated dictionary is:",d1)

#Expression in (x,x*x) format
dict={}
n=int(input())
for i in range(1,n+1):
    dict[i]=i*i
print(dict)

#key and values get paired
dict={}
a=int(input())
b=int(input())
dict[a]=b
print("Enter the key(int) to be added:")
print("Enter the value for the key to be added:")
print("Updated dictionary is:",dict)

#sum of all values in dictionary
dict={'A':100,'B':540,'C':239}
s=0
for i in dict.keys():
    s+=dict[i]
print("Total sum of values in the dictionary:")
print(s)

#Map a dictionary
n=int(input())
l1=[]
l2=[]
print("Enter number of elements for dictionary:")
for i in range(n):
    temp=int(input())
    l1.append(temp)
for i in range(n):
    temp=int(input())
    l2.append(temp)
dict={}
for i in range(n):
    dict[l1[i]]=l2[i]
print("For keys:")
print("For values:")
print("The dictionary is:")
print(dict)

#TUPLE

#add an item
#Sample input:
(4, 6, 2, 8, 3, 1)                                             
(4, 6, 2, 8, 3, 1, 9)                                            
(4, 6, 2, 8, 3, 15, 20, 25, 4, 6, 2, 8, 3)   
Sample output:                           
 (4, 6, 2, 8, 3, 15, 20, 25, 4, 6, 2, 8, 3, 30)

a=(4, 6, 2, 8, 3, 1)
print(a)
b=(9,)
print(a+b)
c=a[:5]+(15,20,25)+a[:5]
print(c)
c=list(c)
c.append(30)
print(tuple(c))

#length of tuple
a=input()
l=[]
for i in a:
    l.append(i)
print(l)
print(len(l))

#reverse of a  tuple
a=input()
l=[]
for i in a:
    l.append(i)
print(tuple(l[::-1]))

#repeated elements in tuple
t=(2,4,5,6,2,3,4,4,7)
a=int(input())
print(t)
if a in t:
    print(t.count(a))

#STRINGS

#upper and lower case in tuple
n=input()
uc=0
lc=0
for i in n:
    if i>='A' and i<='Z':
        uc=uc+1
    elif i>='a' and i<='z':
        lc=lc+1
print(uc)
print(lc)

#count the word and character
n=input()
count=0
word=len(n.strip().split())
print(word)
for i in n:
    if(i!=''):
        count+=1
print(count)
    
#number of digits and letters in string
n=input()
count1=0
count2=0
for i in n:
    if (i>='a' and i<='z') or(i>='A' and i<='Z'):
        count1+=1
    if(i.isdigit()):
        count2+=1
print("Characters=",count1)
print("Digits=",count2)

#characters in ascending order
n=input()
a=[]
for i in n:
    a.append(i)
for i in range(len(a)):
    for k in range(len(a)-1):
        if a[k]>a[k+1]:
            a[k],a[k+1]=a[k+1],a[k]
k=""
for i in range(len(a)):
    k+=a[i]
print(k)
    
#form a new string made default
n=input()
print(n[0]+n[1]+n[-2]+n[-1])

#remove specified nth index
a=input()
b=int(input())
l=[]
for i in a:
    l.append(i)
l.pop(b)
k=""
for i in l:
    k+=i
print(k)

#replace all occurences
#Sample Input:
Cyfuno
y
%
Sample Output:
Modified string:
C%funo

a=input()
b=input()
c=input()
l=[]
for i in a:
    l.append(i)
d=l.index(b)
l.pop(d)
l.insert(d,c)
k=""
for i in l:
    k+=i
print("Modified string:")
print(k)

#remove nth index character
a=input()
b=int(input())
l=[]
for i in a:
    l.append(i)
l.pop(b)
k=""
for i in l:
    k+=i
print(k)

#PATTERNS

#Sample Input 1:
5
Sample Output 1:
*****
*****
*****
*****
*****
n=int(input())
for i in range(0,n):
    for j in range(n):
        print("*",end="")
    print()

#Sample Input 1:
5
Sample Output 1:
11111
22222
33333
44444
55555
n=int(input())
for i in range(0,n):
    for j in range(n):
        print(i+1,end="")
    print()

#Sample input 1:
5
Sample output 1:
*
**
***
****
***** 
n=int(input())
for i in range(0,n):
    for j in range(i+1):
        print("*",end="")
    print()

#Sample input 1:
5
Sample output 1:
*****
****
***
**
*
rows=int(input())
for i in range(rows+1,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print()

#Sample input 1:
5
Sample output 1:
    *
   **
  ***
 ****
*****
rows=int(input())
for i in range(rows):
    for k in range(rows-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()

#Sample Input 1:
5
Sample output 1:
*****
 ****
  ***
   **
    * 
n=int(input())
for i in range(n):
    for k in range(n):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()

#Sample input 1:
5
Sample output 1:
*****
*     *
*     *
*     *
***** 
n=int(input())
for i in range(n):
    for k in range(n):
        if(i==0 or i==n-1 or k==0 or k==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()


#Sample input 1:
5
Sample output 1:
    *
   ***
  *****
 *******
********* 
n=int(input())
for i in range(0,n):
    for k in range(n-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    for k in range(i):
        print("*",end="")
    print()

#Sample input 1:     
5
Sample output 1:
*********
  *******
    *****
      ***
        *
n=int(input())
for i in range(n):
    for k in range(i+1):
        print(" ",end="")
    for k in range(i,n-1):
        print("*",end="")
    for k in range(i,n):
        print("*",end="")
    print()

#Sample input 1:
5
Sample output 1:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    * 
n=int(input())
for i in range(n-1):
    for k in range(i,n):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    for k in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for k in range(i+1):
        print(" ",end="")
    for k in range(i,n-1):
        print("*",end="")
    for k in range(i,n):
        print("*",end="")
    print()

#LOGIC QUESTIONS

#Robot pathway directions and ending point
#Sample Input 1:
UP 5
DOWN 3
LEFT 3
RIGHT 2
STOP

Sample Output 1:
2

from math import *
l=[]
c=[]
x=[]
y=[]
z=False
while z==False:
    a=input()
    if a=="STOP":
        z=True
    else:
        i,k=a.split()
        l.append(i)
        c.append(int(k))
n=len(c)
for i in range(n):
    if l[i]=="DOWN":
        y.append(int(0-c[i]))
    elif l[i]=="UP":
        y.append(int(c[i]))
    elif l[i]=="RIGHT":
        x.append(int(c[i]))
    elif l[i]=="LEFT":
        x.append(int(0-c[i]))
X=0
Y=0
for i in x:
    X=X+i
for i in y:
    Y+=i
d=sqrt(X*X+Y*Y)
print(round(d))    


#Heart Pattern
Sample Input 1:
5

Sample Output 1:
 **   **
**** ****
*********
 *******
  *****
   ***
    *

#Password Verification
#conditions are::

1.At least 1 letter between [a-z]
2.At least 1 number between [0-9]
3.At least 1 letter between [A-Z]
4.At least 1 character from [$#@]
5.Minimum length of transaction password: 6
6.Maximum length of transaction password: 12

a=input()
pwd=a.split(",")
l=[]
for i in range(len(pwd)):
    l.append(1)
for i in range(len(pwd)):
    if len(pwd[i])<6 or len(pwd[i])>=12:
        l[i]=0
        break
for i in range(len(pwd)):
    flag=0
    for k in pwd[i]:
        if k>='a' and k<='z':
            flag=1
            break
    if flag==0:
        l[i]=0
for i in range(len(pwd)):
    flag=0
    for k in pwd[i]:
        if k>='A' and k<='Z':
            flag=1
            break
    if flag==0:
        l[i]=0
for i in range(len(pwd)):
    flag=0
    for k in pwd[i]:
        if k>='0' and k<='9':
            flag=1
            break
    if flag==0:
        l[i]=0
for i in range(len(pwd)):
    flag=0
    for k in pwd[i]:
        if k in "$#@":
            flag=1
            break
    if flag==0:
        l[i]=0
valid_pwd=[]
for i in range(len(pwd)):
    if l[i]!=0:
        valid_pwd.append(pwd[i])
if len(valid_pwd)==0:
    print("No password matches the condition")
else:
    print(",".join(valid_pwd))

#SPIRAL PATTERN
#Sample Input:
5

Sample Output:
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555

a=int(input())
for i in range(1,a+1):
    for k in range(i):
        print(a-k,end="")
    for k in range(a-i):
        print(a-i+1,end="")
    for k in range(a-i):
        print(a-i+1,end="")
    for k in range(i-1,0,-1):
        print(a-k+1,end="")
    print()
for i in range(2,a+1):
    for k in range(a-i+1):
        print(a-k,end="")
    for k in range(i-1):
        print(i,end="")
    for k in range(i-1):
        print(i,end="")
    for k in range(a-i,0,-1):
        print(a-k+1,end="")
    print()

#CRYPTOGRAPHY
#Input Format:
The first line of input consists of n messages
The next n lines of string input separated by space

Output Format:
The output consists of n lines of decoded messages with a new line. if n value is less than or equal to zero, print nothing.

Constraints:
1>=n>=50

Sample Input 1:
2
hsggthbuwvf
epdf

Sample Output 1:
codeshastra
code

Sample Input 2:
3
zov
brf
iaeflmgqx

Sample Output 2:
you
are
excellent

Sample Input 3:
-2

Sample Output 3: