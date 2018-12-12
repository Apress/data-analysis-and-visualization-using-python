
# coding: utf-8

# # Chapter 1 Control Statements

# ## Control Statements

# ## 1) If Statements

# In[13]:


# Comparison operators 
x=5
if x==5:
    print ('Equal 5')
elif x>5:
    print ('Greater than 5')
elif x<5:
    print ('Less than 5')


# In[12]:


# Identation 
x=5 
if x<2:
    print ("Bigger than 2")
    print (" X Value bigger than 2")

print ("Now we are out of if block\n")


# In[14]:


year=2000  
if year%4==0:  
    print("Year(", year ,")is Leap")    
else:  
    print (year , "Year is not Leap" ) 
    


# In[2]:


a=10  
if a>=20:  
    print ("Condition is True" ) 
else:  
    if a>=15:  
        print ("Checking second value"  )
    else:  
        print ("All Conditions are false" )    


# In[23]:


# use the range statement  
for a in range (1,4):  
        print  ( a ) 


# In[24]:


# use the range statement  
for a in range (4):  
        print  ( a ) 


# In[32]:


ticket=4  
while ticket>0:  
    print ("Your ticket number is ",ticket) 
    ticket -=1  


# ### use break, continue and pass statements 

# In[44]:


for letter in 'Python3':  
    if letter == 'o':  
        break  
    print (letter)  


# In[45]:


a=0  
while a<=5:  
    a=a+1  
    if a%2==0:  
        continue  
    print (a)  
print ("End of Loop"  )


# In[46]:


for i in [1,2,3,4,5]:  
    if i==3:  
        pass 
        print ("Pass when value is",i  )
    print (i),  


# ## Excercise , using try and except
# Write a program to prompt the user for hours and
# rate per hour to compute gross pay, the program 
# should gives employee 1.5 time the hourse worked 
# above 30 hours
# Enter Hours: 50
# Enter Rate: 10
# Pay: 550.0
# 

# In[6]:


Hflage=True
Rflage=True
while Hflage & Rflage :
    hours = input ('Enter Hours:') 
    try: 
        hours = int(hours)
        Hflage=False
    except:
        print ("Incorrect hours number !!!!")
    try: 
        rate = input ('Enter Rate:')
        rate=float(rate)
        Rflage=False
    except:
        print ("Incorrect rate !!")

    if hours>40:
        pay= 40 * rate + (rate*1.5) * (hours-40)
    else:
        pay= hours * rate

    print ('Pay:',pay)


# In[14]:


# Try and Except
astr='Fujairah'
errosms=''
try:
    istr=int(astr)   # error 
except:
    istr=-1
    errosms="\nIncorrect entery"

print ("Firs Try:", istr , errosms)


# In[15]:


# Try and Except
astr='12'
errosms=''
try:
    istr=int(astr)   # error 
except:
    istr=-1
    errosms="\nIncorrect entery"

print ("Firs Try:", istr , errosms)


# ### Python Program to check if a Number is Positive, Negative or Zero

# In[1]:


Val = float(input("Enter a number: "))  
  
if Val > 0:  
    print("{0} is a positive number".format(Val))  
elif Val == 0:  
    print("{0} is zero".format(Val))   
else:  
    print("{0} is negative number".format(Val)) 


# In[4]:


# Check if a Number is Odd or Even 
val = int(input("Enter a number: "))  
if (val % 2) == 0:  
    print("{0} is an Even number".format(val))  
else:  
    print("{0} is an Odd number".format(val))  


# In[5]:


# Write a python program that displays specific messages using the IF Statement: 
#It should ask the user to enter the age of a person, and then using a conditional statement, 
#it should print one of the following messages: 


# In[6]:


age = int(input("Enter age of a person"))
if(age < 13):
    print("This is a child")
elif(age >= 13 and age <=17):
    print("This is a teenager")
elif(age >= 18 and age <=59):
    print("This is an adult")
else:
    print("This is a senior")


# In[7]:


Speed = int(input("Enter your car speed"))
if(Speed < 80):
    print("No Fines")
elif(Speed >= 81 and Speed <=99):
    print("200 AE Fine ")
elif(Speed >= 100 and Speed <=109):
    print("350 AE Fine ")
else:
    print("500 AE Fine ")


# In[11]:


year = int(input("Enter a year: "))  
if (year % 4) == 0:  
    if (year % 100) == 0:  
        if (year % 400) == 0:  
               print("{0} is a leap year".format(year))  
        else:  
               print("{0} is not a leap year".format(year))  
    else:  
           print("{0} is a leap year".format(year))  
else:  
    print("{0} is not a leap year".format(year))  


# ## Print the Fibonacci sequence

# In[14]:


nterms = int(input("How many terms you want? "))  
# first two terms  
n1 = 0  
n2 = 1  
count = 2  
# check if the number of terms is valid  
if nterms <= 0:  
    print("Plese enter a positive integer")  
elif nterms == 1:  
    print("Fibonacci sequence:")  
    print(n1)  
else:  
    print("Fibonacci sequence:")  
    print(n1,",",n2,end=', ')  
    while count < nterms:  
        nth = n1 + n2  
        print(nth,end=' , ')  
        # update values  
        n1 = n2  
        n2 = nth  
        count += 1  


# In[2]:


largest = None 
print ('Before:', largest)
for val in [30, 45, 12, 90, 74, 15]:
    if largest is None or val>largest:
        largest = val
        print ("Loop", val, largest)
print ("Largest", largest)

