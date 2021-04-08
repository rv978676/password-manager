from encoder import encoder as en
from filewriter import fileviewer
import filewriter 

def options():
    options=int(input("enter the option which you want to choose (1/2):-"))
    return options

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
print()
print("choose the platform for which you want to save the password")
print("1. See passwords")
print("2. Add passwords")
print()
try:
    options=options()
except:
    print("only enter the number")
    options=options()

if options==1:
      fileviewer()
if options==2:
      filewriter(website,userName,password)

print(en())





