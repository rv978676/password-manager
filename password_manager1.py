from encoder import encoder as en

def options():
    options=int(input("enter the option which you want to choose (between 1-4:-"))

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

print("choose the platform for which you want to save the password")
print("1.Facebook")
print("2.Twitter")
print("3.Google")
print("4.")
try:
    options()
except:
    print("only enter the number")
    options=int(input("enter the option which you want to choose (between 1-4):-"))

print(encoder)





print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using loops) is : ",end="") 
print (reverse(s)) 