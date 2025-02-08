def issubsequence(string,sunbstring):
    i=0
    j=0
    while i<len(substring) and j<len(string):
        if substring[i]==string[j]:
            i+=1
        j+=1
    return i==len(substring)

string="Devika"
substring="Dia"
result=issubsequence(string,substring)
print(result)


#vowels and consanant
text="Devika123"

if not text:
    print("Empty string")

else:
    for char in text.lower():
        if char in("a","e","i","o","u"):
            print(f"{char} is a vowel")
        elif not char.isalpha():
            print(f"{char} not a letter")
        else:
            print(f"{char} is not a consanant")
            
#Find no of days in a month
month="February"
month_31_days=("January","March","May","July","August","October","December")
month_30_days=("April","June","September","November")

if month in month_31_days:
    print(f"{month} has 31 days")
elif month in month_30_days:
    print(f"{month} has 30 days ")
else:
    print(f"{month} has 28 dayys")
    

#comapre 3 nos
a=10
b=20
c=30

if a>b>c:
    print("Increasing order")
elif a<b<c:
    print("decreasing order")
else:
    print("None")
    
    
#display second lowest marks nd name from nested list
names_scores=[['Anmol',10],['julie',20],['marc',10],
              ['Sita',50],['Vas',40],['marchie',20]]
    
scores=[]
for student in names_scores:
    scores.append(student[1])
    
sorted_scores=sorted(set(scores))
print("sorted scores: " ,sorted_scores)
second_lowest=sorted_scores[1]

names_second_lowest=[]
for student in names_scores:
    if student[1]==sorted_scores[1]:   #fpr second highest [-2]
        names_second_lowest.append(student)
        
print("Seond lowes tmarks:",names_second_lowest)

#dictionary problem
#Add a key-value pair only if key is not in dict
my_dict = {"January":45 , "February" : 56}

new_key = "April"
new_value = 12

if new_key not in my_dict:
  my_dict[new_key] = new_value
  
print(my_dict) #{'January': 45, 'February': 56, 'April': 12}

#check if values are all equal 
my_dict = {'A' : 4, 'B' :4 ,'C' : 4}

new_value = len(set(my_dict.values())) #set is used to remove duplicatenvalues

if new_value == 0:
    print("Empty")
elif new_value == 1:
    print(True)
else:
    print(False)
    
#make frequency dict for characters in string
string = "Hello, World"
my_dict = {}

for char in string.lower(): #saglya char la lower
    
    if char.isalpha():   #isalpha is used to avoid space and commas
        if char in my_dict:
            my_dict[char] +=1
        else:
            my_dict[char] = 1
print(my_dict)  #{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}


string = "Hello, World"
my_dict = {}

for char in string.lower(): #saglya char la lower
    
    if char.isalpha():   #isalpha is used to avoid space and commas
        if char not in my_dict:
            my_dict[char] =1
        else:
            my_dict[char] += 1
print(my_dict)


#sort list in asscending order
my_dict = {
    "a":[4,3,2],
    "b":[5,3,7],
    "c":[6,2,3]
}

for list_value in my_dict.values():
    list_value.sort()
print(my_dict)  #{'a': [2, 3, 4], 'b': [3, 5, 7], 'c': [2, 3, 6]}

#find maximum values in dict
my_dict={"a":5,"b":3,"c":7}

if my_dict:
    max_value = max(set(my_dict.values()))
    print(max_value)  #7
    
else:
    print(None)
    
def find_max_value(list):
    max_value = list[0]
    for num in list:
        if num >max_value:
            max_value = num
    return max_value

numbers = [3,7,2,9,5]
print(find_max_value(numbers))  #9

#print 1 to 10 without using any loop 
#Recursion- func la repeatedly call karne
def print_numbers(n):
  if n>20:
      return 
  print(n)
  print_numbers(n+1)
  
print_numbers(1)

#5 ka factorial with recursion 

def numbers(n):
    if n == 0:
        return 1
    else:
        return n * numbers(n - 1)
result = numbers(5)
print(result)

