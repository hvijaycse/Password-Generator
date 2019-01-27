import random
pas=open("Data.txt","a")

StrH="QWERTYUIOPASDFGHJKLZXCVBNM"
StrL="qwertyuiopasdfghjklzxcvbnm"
Num="1234567890"
Special="@#&"

def Passw(Length):
    nu=random.randint(4,Length-4)
    password=""
    password=password + ''.join(random.choice(StrH) for i in range(nu-2))
    password=password + ''.join(random.choice(StrL) for i in range(Length-nu-2))
    password=password + ''.join(random.choice(Special))
    password=password + ''.join(random.choice(Num) for i in range(3))
    return password

print("")
print("Enter name of website")
web=input()
print("")
print("Enter length of password min 8")
print("")
n=int(input())
if n < 8:
    print("Password cant be less than 8 ")
    exit("Error")
while True:
    y=''.join(random.sample(Passw(n),n))
    print("Password generated is " +y )
    print("ok ? y/n")
    if input()=="y":
        break
    else:
        continue

pas.write("\n\nWebsite  : "+web + "\n" + "Pass \t : "+ y )
pas.close()
