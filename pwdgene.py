import random

pwd= input("Enter your password: ")
a= len(pwd)

if a<12:
    print("Length of password must be atleast 12.")
else:
    l= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","~","!","@","#","$","%","^","&","*","_","-","|"]
    b= random.choice(l)

    for i in range(0,a-1):
        c= random.choice(l)
        b = b+c
    print("Regenerated Password is",b)