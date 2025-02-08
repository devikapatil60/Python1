a=5
b=2
print( a!=b)
print(not(a>b))


st="wlcm top greek"
print("to" in st)

st1="wlcm top greek"
print("to" not in st1)

m=10
n='10'
print(a is b)

value=(1+1)*2**4//3+4-1
print(value) #13

#paranthesis
#exponential
#multipplication
#division
#addition and then subtraction

#implicit conversion-not manually convert
a=5   
b=2
value= a/b
print(value)
print(type(value))

#explicit cover-manually convert
a=5   
b=2
value= a/b
print(value)
print(type(value))
int_value=int(value)
print(type(int_value))

q=20
u='10'
print(type(u))
r=q+int(u)
print(r)

data=[10,20,-30,'greek']
print(data)

print("wlcm",end=" ")
print("to",end=" ")

name=input("what is your name")
print(name)
print(type(name))

roll=int(input("Enter your roll no"))
print(roll)
print("roll nos is",roll)

#\n new line
#\t tab
# \'whatevee\' used for to add in double or single code
# \"watever\"

print("hey \'ok\'")


#ways for if statement
if 5>2:
    print("Greater")
    
    
if 5>2: print("Greater")

if 5>2:
    print("Greater")
print("rest of code")

if 5>2:
    print("greater")
    print("5 is greater than 2")
    if(6>2):
        print()
print()

if 5>2 and 4<3:
    print()
    

a=int(input("enter no greater than 2"))
if(a>2):
    print()
else:
    print()
    

a=int(input("Enter no greater than 2:"))
b=100000
if(a<=b):
    print("Correct!! You have entereed",a)
else:
    print("Wrong!! Your balance is insufficient",a)
    print("Your balance is:",b)
    
a=10
b=20
if a>b :
    print("a is greater than b")
elif a==b:
    print()
elif a<b:
    print()
else:
    print()
    
#while-jab tak
a=2
while a<=20:
    print(a)
    a+=2 #increment by 2
print("rest of code")

i=0
while True:
    i+=1
    print(i)
    if(i==5):
        break
print("rest")

#nested while loop
i=1
while i<=3:
    print("outer loop",i)
    i+=1
    j=1
    while j<=5:
        print("inner  loop",j)
        j+=1
        
print("rest of code")

#range function
a= range(5)
print(a[0])
print(a[4])

b=range(1,5)   #start,end it will be till 4
b=range(1,10,2) #start,stop,step till 9 
a=range(-10,-1,2) #-10,-8,-6,-4,-2
range(5,0,-1) # 5,4,3,2,1

st="GeekyShows"
y=len(st)
print(y)
for ch in range(y):
    print(ch,"=",st[ch])
    
    

i = 0
j = "Devika"
z = len(j)

while i < z: 
    print(i, "=", j[i])
    i += 1  

#break statement
for i in range(10):
    if(i==5):         #it will print from 0 to 4
        break
    print(i)
print("rest of code")


#continue statement 
for i in range(10):
    if(i==5):          #it will skip 5 and print till 9
       continue
    print(i)
print("rest of code")

#pass statement -kuch nhi karna
if(5>2):
    pass
else:
    print("else part do something")
    
    
#memory allocation
str1="AC"
str2="PO"
str3="WR"
str4=str3

print("str2=",str2,id(str2))    #str2= PO 1497562393264
print("str3=",str3,id(str3))   #str3= WR 1497562393584
print("str4=",str4,id(str4))   #it will give same location id as str3  str4= WR 1497562393584


#stringlenght
str1="Devika"
y=len(str1)
print(y)

#slicing
print(str1[1:3])

#repetition operation
print(str1*5)
print(str1[0:3]*3)


#fstring
a=10
b=20
print(f"{a} {b}")


a="Devika"
b=a[::-1]
print(b)

#reverse string and compare to find palindrome
str1="racecar"
str2= str1[::-1]
if(str1==str2):
    print("palindrome")
else:
    print("not palindrome")
    

#
name="devika"
str1=name.upper()  #swapcase(),lower(),title()-har ek word ka 1st letter capital hoga,capitalize() -sent ka 1st word ka 1st letter
print(name)#isupper()-checks itis and give TorF,islower(),istitle(),isdigit(),isalpha(),isalnum(),isspace()
print(str1)
#lstrip(),rstrip()-spaces remove from left and rig ,strip()-from both

name="abc"
old="kk"
new="Ner"
str1=old.replace(old,new)
print(str1)

str1=name.split('-')  #split function-list
str1=" ".join(name)  #joinn function it is used with string only
str1=name.startswith('HI') #will give T or F ,endswith('bye')

#day2

#list - mutable
#insert-element wont be deleted
#modify via indexing-element will be replaced

a=[10,20,-50,21.3,'geek']
print(a[0])
a[0]=90  #list modify 
print(a[0])
print(a[2:4])

a=[10,20,-50,21.3,'geek']
print('Accessing link using while loop')
n=len(a)
i=0
while i<n:
    print(i,"=",a[i])
    i+=1
    
    
#deletion function 
a=[10,20,-50,21.3,'geek']   
del a[1]# delete single element
del a #delete entire list

#append method
a=[10,20,-50,21.3,'geek']
for element in a:
    print(element)
    
a.append(100)#last mai add hoga

#append()-adds single element as a whole in list
#extend()-add multiple element individually in list

l1=[10,20]
l1.append([30])

#empty list by appending
a = [] 
n = int(input("Enter the number of elements: "))  

for i in range(n):  
    a.append(int(input("Enter element: ")))  
print(a)  


#dir adds all methods of list and then it conatins underscore method so delete 
for elements in dir(list):
    if "_" in elements:
        pass
    else:
        print(elements)
    

#insert method
a=[10,20,-50,21.3,'geek']
print(a) #[10, 20, -50, 21.3, 'geek']
a.insert(3,'Subscribe')
print(a) #[10, 20, -50, 'Subscribe', 21.3, 'geek']
  
#pop
a=[10,20,-50,21.3,'geek']
print(a)  #[10, 20, -50, 21.3, 'geek']
a.pop(3)
print(a)  #[10, 20, -50, 'geek']
a.pop()


#remove-1st wala occurence remove karta hai
a=[10,20,-50,20,21.3,'geek']
a.remove(20)
print(a) #[10, -50, 20, 21.3, 'geek']


#take a list remove 1st 5 and then convert to no ,then take 2nd list store converted no and the compare which is greater
list1=[9,5,4,3,8,5,7]
print("list1 :",list1)
list1.remove(5) 
number = int("".join(map(str, list1)))  #convert list to number using join & map
print("Number:", number)

list2=list1
print("list2 : " ,list2)
list2.remove(5)
print("hey",list2)

number1 = int("".join(map(str, list2)))  
print("Number1:", number1)

if number>number1:
    print(f"{number}Number  is greater")
else:
    print(f"{number1}Number 2 is greater")


#map function

no=int("".join(map(str, list1))) #map converts list1 to string and then join then convert join to int
no=int("".join(map(int, list1)))
list(map(int,l1)) #this will give in list
map(str,list1) #will provide only map object

#Eg string to list
l1=['9','3','4','6']
np=list(map(int,l1))
print(np)

#index method -it will give 1st occurence or index of any
a=[10,20,-50,21.3,10,'geek']
num= a.index(10)
print(num)

#reverse metghod
a.reverse() #list will reverse

#extend method
a=[10,20]
b=[30,40]
a.extend(b)
print(a) #[10, 20, 30, 40]

#count method
a=[10,20,-50,10,21.3,10,'geek',10]
num=a.count(10) #it wil tell how much cunt of 10 is 4
print(num)

#sort method -it will short
a=[5,42,10]
a.sort() #from decreasing to increasing order

#clear method-it will delete all elements from list only struct will remain
a.clear()

#listslicing
x=[101,102,103,104,105,106,107,108]
a=x[0:] #frome 0yh pos to last [101, 102, 103, 104, 105, 106, 107, 108]
print(a)
a=x[-4:-1] #last 4 elements  [104,105,106]


#how to index list inside list
x = [101, 102, 103, 104, 105, [1, 2, 3, [1,11,9]]] #0123....-7 tp -1
a = x[-1][-1][-1]  # 9    for negative indexing
b  =  x[5][3][1]  #11
print(a)
print(b)

#listConcate
a=[]
b=[]
c=[]

result=a+b+c
print(result)

#list repetition it will multiply list
result=a*3 

#listAliasing - memory add same so changes will reflect in both
a=[10,20,30,40,50]
b=a
print(a) #[10, 20, 30, 40, 50]
print(b) #[10, 20, 30, 40, 50]

a[1]=55 # or b[2]=66 can be madde in both changes
print(a) #[10, 55, 30, 40, 50]
print(b) #[10, 55, 30, 40, 50]

#CopyList -memory add diff changs will reflect only to particuale
b=a.copy()

#modify
a[1]=2

#sort-modifies original list
#sorted -creates new list

a=[5,4,3,5,3,9,8,7,6,7]

l1=[]
for i in a:
    if a.count(i)==1:
        l1.append(i)

print(l1) #[4, 9, 8, 6]

#nested list modification
a=[[10,20,30],[60,50,70]]
a[0][1]=5
a[1][2]=9
print(a) #[[10, 5, 30], [60, 50, 9]]

#set-duplicates element remove hota hai

#dictionary 
#indexing is not possible in dictionary
#dic:key-value pair
d={} #empty dictionary

stu = {101:'Rahul' , 102:'raj'}
fees = {'Rahul':2000,'raj':3000}

print(stu) #{101: 'Rahul', 102: 'raj'}
print(stu[101]) #Rahul 

#modify dictionary
stu[102] = 'Python'

#adding new
stu[104]='css'

#deletion of dictionary
del stu[102] #specific
del stu #whole

#testng keys
dict={}
print(101 in dict)
print(101 not in dict)

#clear() dictionary
stu.clear() #{}

#copy() dict
stu ={}
new_stu =stu.copy()
print(new_stu)

#fromkeys() Method
key = (101,102,103)
value = 'Geek'
d = dict.fromkeys(key,value)
print(d) #{101: 'Geek', 102: 'Geek', 103: 'Geek'}

#get() method - give value
print(stu.get[101])

#items() method key and value dono ayega
stu = {101:'Rahul' , 102:'raj'}
it = stu.items()
print(it) #dict_items([(101, 'Rahul'), (102, 'raj')])

#keys() method only give keys
stu={}
all_keys=stu.keys()

#values() - only give values
all_keys=stu.values()

#update() method
stu.update({105:'Python'})

#pop method -key is given to pop both key-value
stu.pop(101)

#popitem() method - last value nikaltahai

#gettingg input
a={}
n=int(input("Number of elements"))
for i in range(n):
   k=input("Enter keys")
   v=input("Enter value")
   a.update({k:v})
print(a)

#Functions oriented progra are reusable
#defining function one at time
def disp():
    name = 'geek'
    print(name)
    
#calling function as many as times we need
disp()

#separate func for addition ,subtraction
def add():
    x=10
    y=20
    c = x+y #c=x-y
    print(c)
add()


def add(y): #funct with  parameter
    x=10
    c = x+y
    print(c)
add(20)  #func with argument

#Return statement
def add():
    x=10
    y=20
    c = x+y 
    return c
sum = add() #here it will return c to where funct is call and store in sum
print(sum)
     #or
print(add())

#return state with multiple values
def add(y):
    x=10
    c = x+y
    d = x -y
    return c,d,50

sum,sub,a = add(20)
print(sum)
print(sub)
print(a)

#nested func
def disp():
    def show():
        print("show fun")
    print("disp func")                #disp func
    show()                            # show func
disp()

#with return state and parameter
def disp(st):
    def show():
        return "show func"
    result = show()+st + "disp fun"
    return result
print(disp("Geek"))

#positional Argument
def pw(x,y):
    z = x ** y
    print(z) #25
pw(5 , 2) 

#keyword argument -value is assigned with keyword in argument 
def show(name , age):
    print (f"Name:{name} Age:{age}")
show(age = 62,name = "Geek")

#Default argument -default parameteer it will take default value
def show(name , age=22):
    print (f"Name:{name} Age:{age}") #Name:Geek Age:22
show(name = "Geek")

def show(name , age=22):
    print (f"Name:{name} Age:{age}") #Name:Geek Age:62
show(name = "Geek", age=62)

#variable length argument-(* ) or *args we dont now how many arguments will come
def add(*num):
    z = num[0] + num[1] + num[2]
    print("ADDittion is",z , num[3])  #ADDittion is 10 zing
add(5,2,3,'zing')

#positional argument with variable argument
def add(x , *num):
    z = x +num[0]+num[1]
    print("Addition is " , z) #ddition is  11
add(5,2,4)

#keyword arg with var  **kaargs
def add(**num):
    z = num ['a'] +num ['b']
    print(z)  #8
add(a=5,b=3,c=2)

#local variable-accessing inside function , outside fun cannot be acceses
def show():
    x=10     #local variable
    print(x)
show()

#global variable -inside and outside both accessible
a = 50        #global varibale
def show():
    x = 10
    print(x)
    print(a)   #inside fun
show()
print("Nos",a)   #outside fun

#Recursion- func la repeatedly call karne
def print_numbers(n):
  if n>20:
      return 
  print(n)
  print_numbers(n+1)
  
print_numbers(1)
