
# coding: utf-8

# # Functions 

# In[20]:


def thing():   # function header {def, function name, function argumets  } 
    print ('Hello ', end='')   # function body 
    print ('World')
    


thing() # function calling 


# In[13]:


def print_Sms():
    print ("Welcome to Python PD session")
    print ("Jan 2017\n")

print ("\nPD Session on HCT Dubai")
print_Sms()


# In[18]:


def sumvalues(x,y):
    print ('The summation of ',x,'+',y,'= ', end='')
    return x+y

a=5
b=a+2
print (sumvalues(a,b) ) # Function calling


# In[3]:


def Details(name, mark):
    if mark>60:
        print ("Congratulation ",name," you pass the course")
    else:        
        print ("Unfortunately ",name," you didn’t pass the course")


# In[4]:


Details("Ossama", 90)


# In[5]:


Details( 90,"Ossama")


# In[6]:


Details( mark=90, name="Ossama")


# In[7]:





# In[9]:


def Details(name, mark):
    if mark>60:
        print ("Congratulation ",name," you pass the course")
    else:        
        print ("Unfortunately ",name," you didn’t pass the course")


# In[10]:


Details( "Ossama")


# In[11]:


def Details(name, mark=0):
    if mark>60:
        print ("Congratulation ",name," you pass the course")
    else:        
        print ("Unfortunately ",name," you didn’t pass the course")


# In[12]:


Details( "Ossama")


# In[1]:


max('Welcome to Egypt')


# In[2]:


min(3,5,8,9,100,2)


# In[3]:


len('Welcome to Egypt')


# In[8]:


mark=input("Enter your exam mark: ")
mark=float(mark)
if (mark>59.5):
    print ("Pass")
else:
    print ("Fail")


# # Convert Celsius to Fahrenheit 
# ## F = 1.8 C + 32

# In[9]:


value = input("Enter the Celsius value: ")
c = int(value)
f = 1.8 * (c) + 32
print (c , " Celsius = ", f ,   "Fahrenheit")


# In[2]:


import random
for i in range(5):
    x = random.random()
    print (x)


# In[4]:


import random
for i in range(5):
    x = random.random()
    print (round(x,3))


# In[5]:


random.randint(5, 10)


# In[9]:


random.randint(5, 10)


# In[7]:


random.randint(5, 10)


# In[12]:


random.randint(5, 10)


# In[16]:


t = [30, "Omar", 7, 10]
random.choice(t)


# In[17]:


random.choice(t)


# In[18]:


random.choice(t)


# In[23]:


import math
value = 120
decibels = 10 * math.log10(value)
print (decibels)


# In[24]:


degrees = 45
radians = degrees / 360.0 * 2 * math.pi
val= math.sin(radians)
print (val)


# In[30]:


print (math.sqrt(16))


# In[34]:


# Anonymous Function  Definiton  
summation=lambda val1, val2: val1 + val2
      
#Calling summation as a function  
print ("The summation of 7 + 10 = ", summation(7,10)  )


# In[35]:


quiz = 50
def readgrade():
    quiz = input("Enter your quiz mark: ")
    quiz = int(quiz)
    print ("Your quiz score is ", quiz)

readgrade()
print ("Your quiz score is ", quiz)


# In[ ]:


print ("\n******** Greeting ***********")
def greeting(lang):
    if lang=='es':
        print ('Hola')
    elif lang=='fr':
        print ('Bonjour')
    else:
        print ('Hello')

greeting('en')
greeting('es')
greeting('fr')


# In[1]:


def computepay(hours, rate):
    if hours>40:
        pay= 40 * rate + (rate*1.5) * (hours-40)
    else:
        pay= hours * rate
    return pay


hours = input ('Enter Hours: ')
try: 
    hours = int(hours)
except:
    print ("Incorrect hours number !!!!")
    
try: 
    rate = input ("Enter Rate: ")
    rate=float(rate)
except:
    print ("Incorrect rate !!")

fullpay =computepay(hours, rate)

print ("Gross Pay: ", fullpay)


# ## Exrcises 
# ### find the Highest Common Factor of two values.    

# In[5]:


def HCF(x, y):  
    if x > y:  
        smaller = y  
    else:  
        smaller = x  
    for i in range(1,smaller + 1):  
        if((x % i == 0) and (y % i == 0)):  
            HCF = i  
    return HCF  
      
Number1 = int(input("Enter first number: "))  
Number2 = int(input("Enter second number: "))  
print("The Highest Common Factor of", Number1,"and", Number2,"is", HCF(Number1, Number2))  


# In[6]:


#Find Factorial of Number Using Recursion


# In[9]:


def RecurFactorial(n):  
    if n == 1:  
        return n  
    else:  
        return n*RecurFactorial(n-1)  
    
# read the value from the user  
Number = int(input("Enter a number: "))  

# check is the number is negative  
if Number < 0:  
    print("Sorry, factorial does not exist for negative numbers")  
elif Number == 0:  
    print("The factorial of 0 is 1")  
else:  
    print("The factorial of",Number,"is",RecurFactorial(Number)) 


# In[12]:


def RecurFibo(n):  
    if n <= 1:  
        return n  
    else:  
        return(RecurFibo(n-1) + RecurFibo(n-2)) 
    
# read input from the user  
nlength = int(input("Enter your length? "))  
# check if the number of terms is valid  
if nlength <= 0:  
    print("Plese enter a positive integer")  
else:  
    print("Fibonacci sequence:")  
    for i in range(nlength):  
        print(RecurFibo(i), end=' , ')  


# ## 4.6	CREATE PYTHON MODULES

# In[6]:


import addition  
addition.add(10,20)  
addition.add(30,40)  


# In[7]:


"{1} {0}".format(x, "The")
"{first} {second}".format(first="The", second=x)

