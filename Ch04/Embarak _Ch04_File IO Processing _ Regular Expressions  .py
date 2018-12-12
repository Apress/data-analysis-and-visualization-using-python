
# coding: utf-8

# # Ch04 File processing and Regular expressions

# # File processing

# In[2]:


Name = input ("Enter your name: ")
Name


# In[3]:


Mark = input("Enter your mark: ")
Mark = float(Mark)


# In[4]:


print ("Welcome to Grading System \nHCT 2018")
print ("\nCampus\t Name\t\tMark\tGrade")
if (Mark>=85):
    Grade="B+"
print ("FMC\t", Name,"\t",Mark,"\t", Grade)


# ### Files attributes

# In[41]:


# Open a file and find its attributes 
Filehndl = open("Egypt.txt", "r")
print ("Name of the file: ", Filehndl.name)
print ("Closed or not : ", Filehndl.closed)
print ("Opening mode : ", Filehndl.mode)


# ### Open and close files 

# In[40]:


Filehndl = open("Egypt.txt", "r")
print ("Closed or not : ", Filehndl.closed)
Filehndl.close()
print ("Closed or not : ", Filehndl.closed)


# In[39]:


Filehndl = open("Egypt.txt", "w+")
Filehndl.write( "Python Processing Files\nMay 2018!!\n")

# Close opend file
Filehndl.close()


# ### Rename and delete files 

# In[34]:


import os
os.rename( "Egypt.txt", "test2.txt" )
os.remove( "test2.txt" )


# ## Directories in Python

# In[ ]:


import os
os.mkdir("Data 1")   # create a directory 
os.mkdir("Data_2")           
os.chdir("Data_2")    # create a childe directory 
os.getcwd()          # Get the current working directory 

os.rmdir('Data 1')   # remove a directory
os.rmdir('Data_2')   # remove a directory


# In[44]:


import os
os.getcwd()   # Get the current working directory 


# In[43]:


os.chdir('/home/nbuser/library')


# ## open and process files 

# In[45]:


print("\nSearching Through a File\n")
fhand = open('Emails.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print (line)


# In[46]:


print ("\nUsing in to select lines  // only print lines which has specific string ")
fhand = open('Emails.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line :
        continue
    print (line)


# In[47]:


print("\nSearching Through a File\n")
fhand = open('Emails.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        line = line.split()
        print (line[1])


# ## Regular Expressions

# In[48]:


import re
print ("\nRegular Expressions\n'^X.*:' \n")
hand = open('Data.txt')
for line in hand:
    line = line.rstrip()
    y = re.findall('^X.*:',line)
    print (y)


# In[49]:


print ("\nRegular Expressions\nWild-Card Characters  '^X-\S+:'\n")
hand = open('Data.txt')
for line in hand:
    line = line.rstrip()
    y = re.findall('^X-\S+:',line) # match any non white space characters
    print (y)
   


# In[50]:


print ("\n Matching and Extracting Data \n")
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print (y)


# In[51]:


y = re.findall('[AEsOUn]+',x)  # find any of these characters in string
print (y)


# In[52]:


print ("\nGreedy Matching \n")
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print (y)


# In[53]:


print ("\nNon-Greedy Matching \n")
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print (y)


# In[54]:


import re
print ("\nFine-Tuning String Extraction \n")
mystr="From ossama.embarak@hct.ac.ae Sat Jun 5 08:14:16 2018"
Extract  = re.findall('\S+@\S+',mystr)
print (Extract)
E_xtracted = re.findall('^From.*? (\S+@\S+)',mystr) # non greedy white space
print (E_xtracted)
print (E_xtracted[0])


# In[57]:


mystr="From ossama.embarak@hct.ac.ae Sat Jun 5 08:14:16 2018"
atpos = mystr.find('@')
sppos = mystr.find(' ',atpos) # find white space starting from atpos
host = mystr[atpos+1 : sppos]
print (host)
usernamepos =mystr.find(' ')
username = mystr[usernamepos+1 : atpos]
print (username)


# In[58]:


print ("\n The Regex Version\n")
import re
mystr="From ossama.embarak@hct.ac.ae Sat Jun 5 08:14:16 2018"
Extract = re.findall('@([^ ]*)',mystr)
print (Extract)
Extract = re.findall('^From .*@([^ ]*)',mystr)
print (Extract)


# In[59]:


print ("\nScape character \n")
mystr = 'We just received $10.00 for cookies and $20.23 for juice'
Extract = re.findall('\$[0-9.]+',mystr)
print (Extract)


# ## Exercises 

# In[60]:


import re  
CoursesData = """101   COM   Computers
205   MAT   Mathematics
189   ENG    English"""  


# In[61]:


# Extract all course numbers
Course_numbers = re.findall('[0-9]+', CoursesData)
print (Course_numbers)

# Extract all course codes
Course_codes = re.findall('[A-Z]{3}', CoursesData)
print (Course_codes)

# Extract all course names
Course_names = re.findall('[A-Za-z]{4,}', CoursesData)
print (Course_names)


# In[62]:


# compile the regex and search the pattern
regex_num = re.compile('\d+')
s = regex_num.search(CoursesData)

print('Starting Position: ', s.start())
print('Ending Position: ', s.end())
print(CoursesData[s.start():s.end()])


# In[63]:


# define the course text pattern groups and extract
course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
re.findall(course_pattern, CoursesData)


# In[64]:


print(re.findall('[a-zA-Z]+', CoursesData))  # [] Matches any character inside


# In[65]:


print(re.findall('[0-9]+', CoursesData))  # [] Matches any character inside


# In[66]:


import re
CoursesData = """10   COM   Computers
205   MAT   Mathematics
1899   ENG    English"""  
print(re.findall('\d{4}', CoursesData))  # {n} Matches repeat n times.
print(re.findall('\d{2,4}', CoursesData))

