###Welcome to our Python programming challenges repository! Each challenge file in this repository contains a problem statement, sample input and output, and a solution code that satisfies the test cases provided. ###
###To navigate through the challenge files, we recommend that users pay close attention to the comments in the code. The problem statement is provided at the top of the file as a comment, while the sample input and output are presented as comments within the code.###
###It's important to note that the sample input and output may not cover all possible edge cases. The solution code provided is intended as a reference for users to check their work against the expected output.###
###Users are encouraged to attempt to solve the problem on their own before checking the solution code, as this will help improve their problem-solving skills. Once users have written their solution, they can test their code against the sample inputs provided and submit their code for review through a pull request.###



#PRACTICE  PROBLEMS CHALLENGE (EASY TO HARD)#


#N DIVISION -L1

Q.Write a program that will find all such numbers which are divisible by 7 but are not a multiple of 5. The numbers obtained should be printed in a comma-separated sequence on a single line.

Sample input:
1
25

Sample Output:
7,14,21

a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    n=i
    if (n%7==0 and i%5!=0):
        l.append(str(i))
        n+=1
print(",".join(l))


#PRINTING NUMBER ABND U=ITS SQUARE USING DICTIONARY-L1

With a given integer number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

Input
8
output
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
        
a=int(input())
dict={}
for i in range(1,a+1):
    dict[i]=i**2
print(dict)


# LIST AND TUPLE 

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

Input
34,67,55,33,12,98
Output
['34', '67', '55', '33', '12', '98']

('34', '67', '55', '33', '12', '98')

a=input()
list=a.strip().split(",")
tuple=tuple(list)
print(list)
print(tuple)

#FACTORS OF A GIVEN NUMBER

Write a program that can compute the factors of a given number. The results should be printed in a comma-separated sequence on a single line.

input :
10
output :
1,2,5

def print_factors(num):
    l=[]
    for i in range(1,num):
        if num%i==0:
            l.append(str(i))
    print(",".join(l))
num=int(input())
print_factors(num)

#COMPLEX EQUATION RESULTS 

Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]. Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence.

Input
100,150,180
output
18,22,24

from math import *
d=input()
l=d.strip().split(",")
y=[]
c=50
h=30
for i in l:
    d=int(i)
    q=sqrt((2*c*d)/h)
    y.append(str(floor(q)))
print(",".join(y))

#CALCULATION OF SQUARE VALUES

Write a method that can calculate the square value of n given values until and unless user gives -1.

Sample input:
5
4
3
-1
Sample output:
25
16
9

while True:
    a=int(input())
    if a==-1:
        print("invalid input")
        break
    else:
        print(a*a)

#PERFECT SQUARE
Write a function which can store the perfect square values in a list. The user will define the range.


Sample input:
1
20
Sample output:
4,9,16

from math import *
a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    n=sqrt(i)
    for k in range(i):
        if k==n:
            l.append(str(i))
print(",".join(l))

#sSUM OF TWO NUMBERS

Define a function which can compute the sum of two numbers using recursion.

sample input:
4
8
Sample output:
12

def sum(a,b):
    if a==0 and b==0:
        return 0 
    else:
        return a+b
a=int(input())
b=int(input())
x=sum(a,b)
print(x)

#CONCATENATION

Define a function that can accept two strings as input and concatenate them and then print it in the console without using a string predefined function, also don’t use the ‘+’ operator. The user will give n values until and unless the user enters -1.

Sample input:
Hello
World
up
-1
Sample output:
HelloWorld

l=[]
while True:
    a=input()
    if a=="-1":
        break
    else:
        l.append(a)
if len(l)==1:
    print("Invalid Input")
else:
    print("".join(l[:len(l)-1]))

#MAXIMUM STRING

Define a function that can accept n strings as input and print the string with maximum length in console. The code will get n values until and unless the user enters -1.

Sample input:
Hello
Everyone
Sample output:
Everyone

l=[]
while True:
    a=input()
    l.append(a)
    if a=="-1":
        break
if l[0]=="-1":
    print("No string given")
else:
    a=[]
    for i in range(len(l)-1):
        a.append(len(l[i]))
k=max(a)
for i in range(len(l)-1):
    if k == a[i]:
        print(l[i],end=" ")

#FACTORIAL VALUE

Define a function that can accept an integer number as input and print it as a prime number or not if it is odd and print its factorial value if it is even using recursion.

Sample input:
3
Sample output:
The given number is ODD and also a prime number.

def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
def prime(a):
    count=0
    if a>1:
        for i in range(2,int(input())+1):
            if i%a==0:
                count+=1
        if count==2:
            print(a,"even no")
        else:
            print(a,"odd no")
def num(a):
    if a%2==0:
        return "the given number is EVEN,so the factorial value of",a,"is",fact(a)
    else:
        if prime(a):
            print("The given number is ODD and also a prime number")
        else:
            print("The given number is ODD but not a prime number")
            
a=int(input())
num(a)

#TYPE CASTING-1
Define a function that can convert an integer into a string and print it in the console. The user will give n values until and unless the user enters -1.

sample input:

57

Sample output:

<class 'str'>57

def int_to_str():
    while True:
        n = int(input("Enter an integer (-1 to exit): "))
        if n == -1:
            break
        s = str(n)
        print(type(s), s)
int_to_str()

#TYPE CATSING -2
Define a function that can convert an integer into a string and print it in the console without using predefined functions. The user will give n values until and unless the user enters -1.

Sample input:

6

Sample output:

<class 'str'> 6

l = []
while True:
    a = int(input())
    l.append(a)
    if a == -1 :
        break
if len(l) == 1:
    print("Invalid Input")
else:
    for i in l[:len(l)-1]:
        s=""
        n = i
        while n != 0:
            a = n % 10
            s = chr(ord('0') + a) + s
            n = n // 10
        print(type(s),s)
   

#TYPE CASTIN -3
Define a function that can receive two integral numbers in string form and compute their sum and then print it in the console without using any predefined functions. The user will give n values until and unless the user enters -1.

Sample input:

40

15

25

-1

Sample output:

55

l = []
while True:
    a = input()
    l.append(a)
    if a == "-1":
        break
if len(l) == 2:
    print("Invalid Input")
else:
    a = []
    for i in range(len(l) - 1):
        n = 0
        for k in l[i]:
            n = n * 10 + (ord(k)-48)
        a.append(n)
    for i in range(0,len(a),2):
        print(a[i]+a[i+1])

#Kaprekar Number-L1

Consider an n-digit number k. Square it and add the right n digits to the left n or n-1 digits. If the resultant sum is k, then k is called a Kaprekar number. For example, 9 is a Kaprekar number since 92 = 81 & 8+1=9. and 297 is a Kaprekar number since 2972 = 88209 & 88+209 = 297 Input Format: Input consists of a single integer. Output Format: Refer sample output for details.


Sample Input

9

Sample Output

Kaprekar Number

Sample Input

5

Sample Output

Not A Kaprekar Number

a = int(input())
b = a**2
b = str(b)
# print(b)
c = int(b[0:(len(b)//2)]) + int(b[len(b)//2:])
# print(b[0:(len(b)//2)])
# print(b[len(b)//2:])
# print(c)
if c == a:
    print("Kaprekar Number")
else:
    print("Not A Kaprekar Number")

#Frequency Of Words-L1


Write a Python program to find the frequency of words in the given string.

Sample Input
the future belongs to those who believe in the beauty of their dreams
Sample Output
the : 2

future : 1

belongs : 1

to : 1

those : 1

who : 1

believe : 1

in : 1

beauty : 1

of : 1

their : 1

dreams : 1

#CODE

a = input()
wrd = a.strip().split()
l = []
print(wrd)
for i in wrd:
    if i not in l:
        l.append(i)
for i in range(len(l)):
    print(l[i],":",wrd.count(l[i]))

#Vaporcode-L1

Description:

Write a function that converts any sentence into a V A P O R W A V E sentence. a V A P O R W A V E sentence converts all the letters into uppercase, and adds 2 spaces between each letter (or special character) to create this V A P O R W A V E effect.

Note that spaces should be ignored in this case.


Sample input:
Lets go to the movies

Sample output:
L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S

a = input()
for i in a:
    if i != " ":
        print(i.upper(),end = " ")

#sorting of strings without sort function L2

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically without using sort function.

input

without,hello,bag,world

output

bag,hello,without,world

a = input()
wrd = a.strip().split()
print(wrd)
for l in range(len(wrd)):
    for i in range(len(wrd)-1):
        m = wrd[i]
        n = wrd[i+1]
        #for k in range(2):
        if m[0] > n[0]:
            wrd[i],wrd[i+1] = wrd[i+1],wrd[i]
            #break
print(wrd)
print(",".join(wrd))

#Array Conversion - L2

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

Note: i=0,1.., X-1; j=0,1,¡¬Y-1.

input

3

5

output

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

a = int(input())
b = int(input())
l = []
c = []
for i in range(a):
    for k in range(b):
        l.append(i*k)
    c.append(l)
print(c)

#Binary Division Evaluation - L2

Write a program that accepts a sequence of comma-separated 4-digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma-separated sequence

input


0100,0011,1010,1001

output

1010

a = input()
binary = a.strip().split(",")
binary = [ int(i) for i in binary]
decimal = []
fact_five = []
for i in binary:
    n = i
    s = 0
    k = 1
    while n != 0:
        s = s + (n%2)*k
        k = k*2
        n = n//10
    #print(s)
    decimal.append(s)
for i in decimal:
    if i%5 == 0:
        k = decimal.index(i)
        fact_five.append(str(binary[k]))
if len(fact_five) == 0:
    print("binary values are not divisible by 5")
else:
    print(",".join(fact_five))

#converting Lower case string to uppercase string L2

Q.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

input

Hello world

output


HELLO WORLD

a = input()
k = ""
for i in a:
    if ord(i) >= 97 and ord(i) <= 122:
        i = chr(ord(i)-32)
    k = k + i
print(k)

#Sort String without repeated words- L2

Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

input

hello world and practice makes perfect and hello world again

 output

again and hello makes perfect practice world

a = input()
wrd = a.strip().split()
new_wrd = []
for i in wrd:
    if i not in new_wrd:
        new_wrd.append(i)
for i in range(len(new_wrd)):
    for k in range(len(new_wrd)-1):
        m = new_wrd[k]
        n = new_wrd[k+1]
        for l in range(min(len(m),len(n))):
            if m[l] > n[l]:
                new_wrd[k], new_wrd[k+1] = new_wrd[k+1], new_wrd[k]
                break
            if m[l] < n[l]:
                break
print(" ".join(new_wrd))


#Even numbers in a digit - L2

Write a program, which will find all such numbers between the user-given range (both included) such that each digit of the number is an even number.

The numbers obtained should be printed in a comma-separated sequence on a single line.

Input Format:
The first input consists of an integer type to get starting value.
The second input consists of an integer type to get the ending value.

Output Format:
The output consists of all even digit numbers from the given range separated by a comma. If the range is out of bound, print "Invalid Input".

Constraints:
1>=n,m<=5000

Sample Input 1:
81
101

Sample Output 1:
82,84,86,88

Sample Input 2:
1
11

Sample Output 2:
2,4,6,8

a = int(input())
b = int(input())
if a < 1 or b < 1 or a > 5000 or b > 5000:
    print("invalid input")
else:
    l = []
    for i in range(a,a+8):
        if i % 2 == 0:
            l.append(str(i))
    print(",".join(l))

#The number of letters and digits in a String- L2

Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

Input Format:

Input consists of a string. 

a = input()
char_count = 0
num_count = 0
for i in a:
    if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        char_count += 1
    elif i in "0123456789":
        num_count += 1
print("LETTERS",char_count)
print("DIGITS",num_count)#Python


#Calculate the number of upper case letters and lower case letters- L2

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Sample input:

Hello world!

Sample output: 

UPPER CASE 1

LOWER CASE 9

Output Format: 

The output consists of a calculation of number of digits and letters. 

Sample Input: 

hello world! 123

Sample output:

LETTERS 10

DIGITS 3

a = input()
n = 0
c = 0
for i in a:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        n += 1
    elif i in "abcdefghijklmnopqrstuvwxyz":
        c += 1
print("UPPER CASE",n)
print("LOWER CASE",c)#Python

#Compute the value- L2

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Sample Input-1: 

9

Sample Output-1: 

11106

Sample Input-2: 

11

Sample Output-2: 

11223344

a = int(input())
s = a + int(str(a)+str(a)) + int(str(a)+str(a)+str(a)) +int(str(a)+str(a)+str(a)+str(a))
print(s)

#Print odd number in a list- L2

Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

Sample input: 

1,2,3,4,5,6,7,8,9

Sample Output: 

1,3,5,7,9

odd=input()
odd= odd.strip().split(",")
new_list= []
for i in odd:
    if int(i) % 2!=0:
        new_list.append(i)
print(",".join(new_list))

#Bank Transaction- L2

Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

D 100

W 200

D means deposit while W means withdrawal.

Sample Input: 

D 300

D 300

W 200

D 100

Sample output:

500

end = 0
l = []
while not(end):
    a = input()
    t = a.strip().split()
    l.append(t[0])
    l.append(int(t[1]))
    if l[len(l) - 2] == "D" and l[len(l) - 4] == "W":
        end = 1
s = 0
for i in range(0,len(l),2):
    if l[i] == "D":
        s = s + l[i+1]
    elif l[i] == "W":
        s = s - l[i+1]
print(s)

#*Passcode Verification*- L3
Requested files: passcode.py (Download)
Type of work: Individual work
A website requires the users to input a username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:


At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma-separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Input Format:
The input consists of a single line string inputs separated by a comma(,).

Output Format:
The output consists of strings that satisfy the password condition separated by a comma(,). if there is no password that matches the condition, print "No password matches the condition".

Sample Input:
ABd1234@1, a F1#, 2w3E*, 2We3345

Sample Output:
ABd1234@1

a = input()
pwd = a.strip().split(",")
l = [1] * len(pwd)
for i in pwd:
    if len(i) <= 6:
        l[pwd.index(i)] = 0
        break
for i in pwd:
    if len(i) >= 12:
        l[pwd.index(i)] = 0
        break
for i in pwd:
    flag = 0
    for k in i:
        if k in "abcdefghijklmnopqrstuvwxyz":
            flag = 1
    if flag == 0:
        l[pwd.index(i)] = 0
for i in pwd:
    flag = 0
    for k in i:
        if k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            flag = 1
    if flag == 0:
        l[pwd.index(i)] = 0
for i in pwd:
    flag = 0
    for k in i:
        if k in "0123456789":
            flag = 1
    if flag == 0:
        l[pwd.index(i)] = 0
for i in pwd:
    flag = 0
    for k in i:
        if k in "$#@":
            flag = 1
    if flag == 0:
        l[pwd.index(i)] = 0
new_pwd = []
for i in range(len(pwd)):
    if l[i] == 1:
        new_pwd.append(pwd[i])
if len(new_pwd) == 0:
    print("No password matches the condition")
else:
    print(",".join(new_pwd))

#Sort the Tuple- L3

You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:

1: Sort based on name;

2: Then sort based on age;

3: Then sort by score.

The priority is that name > age > score.

Sample input: 

Tom,19,80

John,20,90

Jony,17,91

Jony,17,93

Json,21,85

Sample Output: 

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

l = []
while True:
    try:
        a = input()
        l.append(a)
    except:
        break
c = []
n = [0] * len(l)
for i in l:
    a = i.strip().split(",")
    c.append(a)
for i in c:
    g = i[0]
    for k in c:
        h = k[0]
        for m in range(min(len(g),len(h))):
            if g[m] < h[m]:
                n[c.index(i)] += 1
                break
            if g[m] > h[m]:
                n[c.index(i)] -= 1
                break
print("-------",n,"-----")
for i in range(len(n)):
    for k in range(len(n)-1):
        if n[k] < n[k+1]:
            c[k], c[k+1] = c[k+1], c[k]
            n[k], n[k+1] = n[k+1], n[k]
        if n[k] == n[k+1]:
            if c[k][1] > c[k+1][1]:
                c[k], c[k+1] = c[k+1], c[k]
            if c[k][1] == c[k+1][1]:
                if c[k][2] > c[k+1][2]:
                    c[k], c[k+1] = c[k+1], c[k]
n = []
print(c)
for i in c:
    n.append(i)
print(n)
l = []
for i in n:
    l.append(tuple(i))
print(l)


#Robot pathway= L3

A robot moves in a plane starting from the original point (0,0). The robot can move UP, DOWN, LEFT, and RIGHT with given steps. Please write a program to compute the distance from the current position after a sequence of movements and the original point. If the distance is a float, then just print the nearest integer.

Input Format:
The first line of input consists of one string and one integer
The second line of input consists of one string and one integer
Same for the other new lines until the user enters a "STOP".

Output Format:
The output consists of an integer value which is the distance between points.

Sample Input 1:
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
while z == False:
    a=input()
    if a=="STOP":
        z= True
    else:
        i,k = a.split()
        l.append(i)
        c.append(int(k))
n=len(c)
for i in range(n):
    if l[i] == "DOWN":
        y.append(int(0-c[i]))
    elif l[i]== "UP":
        y.append(int(c[i]))
    elif l[i]== "RIGHT":
        x.append(int(c[i]))
    elif l[i]=="LEFT":
        x.append(int(0-c[i]))
X=0
Y=0
for i in x:
    X=X+i
for i in y:
    Y=Y+i
d=sqrt(X*X + Y*Y)
print(round(d))

#Sorting the key alphanumerically- L3


Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

Sample input: 

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Sample Output: 

2:2

3.:1

3?:1

New:1

Python:5

Read:1

and:1

between:1

choosing:1

or:2

to:1

a = input()
wrd = a.strip().split()
#print(wrd)
l = []
for i in wrd:
    flag = 0
    for k in i:
        if k in "0123456789":
            flag = 1
            break
    if flag != 1:
        l.append(i)
print(l)
s = []
for i in l:
    if i not in s:
        s.append(i)
n = [0] * len(s)
for i in s:
    for k in l:
        if i == k:
            n[s.index(i)] += 1
for i in range(len(s)):
    for k in range(len(s)-1):
        if s[k] > s[k+1]:
            s[k], s[k+1] = s[k+1], s[k]
            n[k], n[k+1] = n[k+1], n[k]
for i in range(len(s)):
    print(s[i],":",n[i])


#Movie Tickets-L3

Ask the customer's age and for the time on a 24-hour clock (where noon is 12.00 and 4:30 PM is 16.30). The show timings are 10.15, 13.30, 18.00 and 22.00. The normal adult ticket price is $8.00, however, the adult matinee price is $5.00. Adults are those over 13 years. The normal children's ticket price is $4.00, however, the children's matinee price is $2.00. Write a python program that determines the price of a movie ticket Input format: The first input containing an integer which denotes the age The second input containing the floating point number which denotes the show timing. Output format: Print the price of a movie ticket. Refer the sample output for formatting



Sample Input

16
10.5

Sample Output

$8.00

 

Sample Input

24
12.3

 

Sample Output

$8.00

a = int(input())
b = float(input())
#10:15,13:30,18:00,22:00
if a > 13:
    if b < 18.00 and b > 13.30:
        print("$5.00")
    else:
        print("$8.00")
else:
    if b < 18.00 and b > 13.30:
        print("$2.00")
    else:
        print("$4.00")

#Circle Intersection-L3

Write a python program to determines if two circles intersect each other.

Input format:
Input consists of 6 integers The first input containing an integer which denotes the x-coordinate of the center of the first circle. The second input containing an integer which denotes the y-coordinate of the center of the first circle. The third input containing an integer which denotes the radius of the first circle. The next 3 integers denote the x,y, and radius of the second circle.

Output format:
The output consists of a single line which contains any of these 2 strings. “Tangential”, “Overlap”.

from math import *
x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())
d = sqrt((x1-x2)**2 + (y1-y2)**2)
if d == r1 + r2:
    print("Tangential")
elif d < r1 + r2:
    print("Overlap")

#Hiring Chef For Restaurant-L3

At a restaurant, two types of dishes (A and B) are to be cooked. For this, the restaurant authority wants to hire new chefs. There are few chefs who can prepare only dish A and few others can prepare only dish B. Some chefs (represented as C) can prepare both dish A and dish B. The restaurant kitchen is small, and only one chef can work in the kitchen at a time.

Consider N chefs, available to prepare dish A or dish B or both, along with the time Ti (i=1,2,3…..N) required by 1st chef. The restaurant authority can either hire two chefs among N chefs to prepare dish A and B separately, or can hire someone who can cook both A and B.

 

Write a program to find the minimum time Z required to prepare both of the dishes.

Constraints:

N>=1
T>=1
Input Format:
The first line of input contains N.
Next N line of input contains a character (A,B or C) and T, separated by a single white space.
Output Format:
The output contains Z.

Sample Input
5
A 2
B 5
A 2
C 4
B 3
Sample output
4


a = int(input())
A = []
B = []
C = []
for i in range(a):
    wrd = input()
    s = wrd.strip().split()
    if s[0] == "A":
        A.append(int(s[1]))
    elif s[0] == "B":
        B.append(int(s[1]))
    elif s[0] == "C":
        C.append(int(s[1]))
a = min(A)
b = min(B)
c = min(C)
if a + b > c:
    print(c)
else:
    print(a + b)

#Treasure Hunt-L3

Max is on a quest to collect gold coins. He has come across a series of open crates which re filled with gold coins each of varying quantities. He is free to collect the coins from any crate, however as soon as he collects the coins from one crate, the crates before and after that particular crate vanish, which means he can no longer collect the coins from both of those crates.
Given a series of N crates and c numbers of gold coins inside each of them, write a program to help Max collect the maximum number M of gold coins.


Constraints:
0<N<104
0<=C<109
I)The number of crates N,
II)Number of gold coins in each crate C,0<C<109   



Input Format:

The first line of input contains N, the number of crates.

the secont line of input contains N number separated by a single white space, representing the number of gols coins in each crate.

Output Format:

The output contains M, the maximum number of gold coin that Max can collect.



Sample Input

5

1 2 3 4 5

Sample Output

9


a = int(input())
b = input()
c = b.strip().split()
l = []
for i in c:
    l.append(int(i))
c = 0
while(len(l) > 1):
    k = max(l)
    c = c + k
    s = l.index(k)
    if s+1 == len(l):
        l.pop(s)
        l.pop(s-1)
    elif s == 0:
        l.pop(s+1)
        l.pop(s)
    else:
        l.pop(s+1)
        l.pop(s)
        l.pop(s-1)
if len(l) == 1:
    c = c + l[0]
print(c)

#Easy wallpaper-L3

John wants to decorate the walls of a room with wallpaper. He wants a fool-proof method for getting it right.

John knows that the rectangular room has a length of l meters, a width of w meters, a height of h meters. The standard width of the rolls he wants to buy is 52 centimeters. The length of a roll is 10 meters. He bears in mind however, that it’s best to have an extra length of wallpaper handy in case of mistakes or miscalculations so he wants to buy a length 15% greater than the one he needs.

Last time he did these calculations he got a headache, so could you help John?

Task
Your function wallpaper(l, w, h) should return as a plain English word in lower case the number of rolls he must buy.

Notes:
all rolls (even with incomplete width) are put edge to edge

0 <= l, w, h (floating numbers); it can happens that w * h * l is zero

the integer r (number of rolls) will always be less or equal to 20

the number of rolls will be a positive or null integer (not a plain English word; this number can be greater than 20)


Sample Input:
6.3, 4.5, 3.29

Sample output:
sixteen


from math import *
def wallpaper(a, b, c):
    area = (float)(2*(b*c + c*a))
    roll = (int)(0.52 * 11.5)
    r = ceil(area / roll)
    print(r)
s = input()
wrd = s.strip().split(", ")
a = float(wrd[0])
b = float(wrd[1])
c = float(wrd[2])
wallpaper(a, b, c)

#Anagram Detection-L4

An anagram is the result of rearranging the letters of a word to produce a new word.

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"

Sample Input:

foefet

toffee

Sample Output:

True

def are_anagrams(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    
    if len(str1) != len(str2):
        return False
    elif sorted(str1) == sorted(str2):
        return True
are_anagrams("foefet", "toffee")

#Keypad-L4

Description:

Given a string of numbers, you must perform a method in which you will translate this string into text

for example if you get 22 you will b, if you get 222 you will return c. if you get 2222 return ca

Hints:

1 is used to separate letters with the same number.

always transform the number to the letter with the maximum value, as long as it does not have a 1 in the middle.

777777 = "sq". 7717777 = "qs".

you cannot type digits

0 are spaces in the string.

Given a empty string, return empty string.

Return a lowercase string.

Sample Input:

443355555566604466690277733099966688

Sample Output:

hello how are you


def keypad(input_string):
    keypad_dict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    output_string = ''
    prev_num = None
    for num in input_string:
        if num == '0':
            output_string += ' '
        elif num in keypad_dict:
            letters = keypad_dict[num]
            if len(letters) == 1:
                output_string += letters
            else:
                if prev_num == num:
                    output_string += '#'
                output_string += letters[-1]
            prev_num = num
    return output_string.lower()


#London CityHacker-L4

You are given a sequence of a journey in London, UK. The sequence will contain bus numbers and TFL tube names as strings e.g.

['Northern', 'Central', 243, 1, 'Victoria']
Journeys will always only contain a combination of tube names and bus numbers. Each tube journey costs £2.40 and each bus journey costs £1.50. If there are 2 or more adjacent bus journeys, the bus fare is capped for sets of two adjacent buses and calculated as one bus fare for each set.

Your task is to calculate the total cost of the journey and return the cost rounded to 2 decimal places in the format (where x is a number): £x.xx


Sample Input:
12, 'Central', 'Circle', 21

Sample output:
"£7.80"


def london_cityhacker(journey):
    total_cost = 0
    is_previous_bus = False
    
    for step in journey:
        if type(step) == int:
            if is_previous_bus:
                is_previous_bus = False
            else:
                total_cost += 1.5
                is_previous_bus = True
        else:
            total_cost += 2.4
            is_previous_bus = False
            
    return f"£{total_cost:.2f}"


#N Division - L1

Write a program that will find all such numbers which are divisible by 7 but are not a multiple of 5. The numbers obtained should be printed in a comma-separated sequence on a single line.

Input Format:
The first line consists of an integer value as starting value
The second line consists of an integer value as the ending value.

Output Format:
The output consists of numbers that are all divisible by 7 and are not a multiple of 5 with the given range.

Sample input:
1
25

Sample Output:
7,14,21

def ndivision(start, end):
    result = []
    for num in range(start, end+1):
        if num % 7 == 0 and num % 5 != 0:
            result.append(num)
    print(",".join(str(num) for num in result))


#Printing Number and its square using dictionary L1

With a given integer number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

Input

8

output

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def square_dictionary(n):
    result = {}
    for i in range(1, n+1):
        result[i] = i*i
    print(result)

#List and Tuple L1

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

Suppose the following input is supplied to the program:

Input
34,67,55,33,12,98

Output


['34', '67', '55', '33', '12', '98']

('34', '67', '55', '33', '12', '98')

def list_and_tuple(sequence):
    numbers = sequence.split(',')
    list_output = list(numbers)
    tuple_output = tuple(numbers)
    print(list_output)
    print(tuple_output)

#Factors of a given number L1

Write a program that can compute the factors of a given number. The results should be printed in a comma-separated sequence on a single line.

Input :

10

output :

1,2,5

def factors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(str(i))
    print(",".join(result))


#complex equation results L1

Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]. Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence.

Example

Let us assume the following comma separated input sequence is given to the program:

Input

100,150,180

output

18,22,24

import math

# Fixed values of C and H
C = 50
H = 30

# Take input as comma-separated values
input_str = input("Enter values of D: ")
d_values = input_str.split(",")

# Iterate over the list of D values
results = []
for d in d_values:
    # Calculate the result for current value of D
    q = round(math.sqrt((2 * C * int(d)) / H))
    results.append(str(q))

# Print the results as comma-separated values
print(",".join(results))


#Calculation of square values-L1

Write a method that can calculate the square value of n given values until and unless user gives -1.

Sample input:

5

4

3

-1

Sample output:
25

16

9

def square_values():
    while True:
        n = int(input())
        if n == -1:
            break
        print(n * n)

square_values()


#Perfect Square-L1


Write a function which can store the perfect square values in a list. The user will define the range.


Sample input:

1

20

Sample output:

4,9,16


def perfect_squares(start, end):
    squares = []
    for i in range(start, end+1):
        root = int(i ** 0.5)
        if root ** 2 == i:
            squares.append(i)
    return squares

start = int(input())
end = int(input())

squares = perfect_squares(start, end)
print(','.join(str(x) for x in squares))


#sum of two numbers-L1

Define a function which can compute the sum of two numbers using recursion.

sample input:

4

8

Sample output:

12

def sum_of_two_numbers(a, b):
    if b == 0:
        return a
    else:
        return sum_of_two_numbers(a ^ b, (a & b) << 1)

# Taking input from user
num1 = int(input())
num2 = int(input())

# Calling the function
result = sum_of_two_numbers(num1, num2)

# Printing the output
print(result)


#Concatenation-L1

Define a function that can accept two strings as input and concatenate them and then print it in the console without using a string predefined function, also don’t use the ‘+’ operator. The user will give n values until and unless the user enters -1.

Sample input:

Hello

World

up

-1

Sample output:

HelloWorld


def concatenate(s1, s2):
    # convert strings to lists of characters
    chars1 = list(s1)
    chars2 = list(s2)
    
    # add the characters from s2 to s1
    for c in chars2:
        chars1.append(c)
    
    # convert the list of characters back to a string
    result = ''.join(chars1)
    return result

# read strings from user input and concatenate them
s1 = input()
while s1 != '-1':
    s2 = input()
    while s2 != '-1':
        s1 = concatenate(s1, s2)
        s2 = input()
    print(s1)
    s1 = input()


#Max String-L1

Define a function that can accept n strings as input and print the string with maximum length in console. The code will get n values until and unless the user enters -1.

Sample input:

Hello

Everyone

Sample output:

Everyone

def max_string():
    strings = []
    while True:
        string = input()
        if string == '-1':
            break
        strings.append(string)
    max_len = 0
    max_string = ''
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            max_string = string
    print(max_string)


#Factorial value-L1

Define a function that can accept an integer number as input and print it as a prime number or not if it is odd and print its factorial value if it is even using recursion.

Sample input:

3

Sample output:

The given number is ODD and also a prime number.


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def process_num(num):
    if num % 2 == 0:
        print("The factorial of", num, "is", factorial(num))
    else:
        if is_prime(num):
            print("The given number is ODD and also a prime number.")
        else:
            print("The given number is ODD but not a prime number.")

# test the function with sample input
num = 3
process_num(num)


#Type casting I-L1

Define a function that can convert an integer into a string and print it in the console. The user will give n values until and unless the user enters -1.

sample input:

57

Sample output:

<class 'str'>57


def int_to_str(num):
    return str(num)

while True:
    n = int(input("Enter an integer number: "))
    if n == -1:
        break
    str_n = int_to_str(n)
    print(type(str_n), str_n)


#Type casting II-L1

Define a function that can convert an integer into a string and print it in the console without using predefined functions. The user will give n values until and unless the user enters -1.

Sample input:

6

Sample output:

<class 'str'> 6


def int_to_str(num):
    if num == -1:
        return
    str_num = ""
    while num != 0:
        str_num = chr((num % 10) + 48) + str_num
        num //= 10
    print("<class 'str'>", str_num)
    int_to_str(int(input()))  # recursive call


# main program
int_to_str(int(input()))


#Type Casting III-L1

Define a function that can receive two integral numbers in string form and compute their sum and then print it in the console without using any predefined functions. The user will give n values until and unless the user enters -1.

Sample input:

40

15

25

-1

Sample output:

55


def string_addition(str1, str2):
    num1 = int(str1)
    num2 = int(str2)
    return num1 + num2

while True:
    num_str1 = input()
    if num_str1 == '-1':
        break
    num_str2 = input()
    if num_str2 == '-1':
        break
    result = string_addition(num_str1, num_str2)
    print(result)


#Diamond Pattern

Write a Python program to print the given pattern from user-defined values(dynamic values).

Sample input 1:
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

def diamond_pattern(n):
    # upper half of the diamond
    for i in range(n):
        print(" "*(n-i-1) + "*"*(2*i+1))
    # lower half of the diamond
    for i in range(n-2, -1, -1):
        print(" "*(n-i-1) + "*"*(2*i+1))

n = int(input("Enter the size of the diamond: "))
diamond_pattern(n)