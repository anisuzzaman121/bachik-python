fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#fansion.............
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#----------------
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#---------------
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#Assignment operatars----------------
# 1.Assigns Value(=)
# 2.add equal(+=)
# 3.subtract equal(-=)
# 4.Multiply equal(*=)
# 5.Divide equal(/=)
# 6.Floor Division equal(//=)
# 7.Modulus equal(%=)
# 8.Exponent equal(**=)

# 9.Bitwise and equal(&=)
# 10.Bitwise or equal(|=)
# 11.Bitwise xor equal(^=)
# 12.Bitwise right shift equal(>>=)
# 13.Bitwise left shift equal(>>=)

# 2.add equal(+=)
a=10
a+=20
print(a)

# 3.subtract equal(-=)
a=10
a-=20
print(a)

#4.Multiply equal(*=)
a=10
a*=5
print(a)

# 5.Divide equal(/=)
a=10
a/=5
print(a)

# 6.Floor Division equal(//=)
a=10
a//=5
print(a)


# 7.Modulus equal(%=)
a=10
a%=5
print(a)

# 8.Exponent equal(**=)
a=10
a**=10
print(a)


#Flow control/Decision making============================
# 1.if
# 2.else
# 3.elif
# 4.Nested if
# 5.while loop
# 6.for loop
# 7.continue
# 8.break
# 9.pass

# 1.if 2.else-------------
a=10
if a==11:
    print("This is true")
else:
    print("This is false")
    
    
# 3.elif-----------------
a="Anis"
b="Husnara"
if a=="anis":
    print("I love anis")
elif b=="Husnara":
    print("I love Husnara")
else:
    print("I do not love")
    
# 4.Nested if-------------------
a="chocolate"
b="cadbury"
c="shinchan"
if a=="chocolate":
    print("Home worke done")
    if c=="doraemon":
        print("Eat food")
    else:
        print("Not Eating")
elif b=="cake":
    print("Go to Home")
else:
    print("Do not go to home")
print("End")

# 5.while loop------------
i=1
while i<=10:
    print(i,":ok")
    i+=1
#---------------------------
i=1
while i<=10:
    print(i)
    i+=1
#---------------------------    
while True:
    print("oky")
#---------------------------    
i=1
j=1
while i<=10:
    while j<=10:
        k=i*j
        print(i,"*",j,"=",k)
        j+=1       
    i+=1
    print("End")
    j=1
#---------------------------
    
i=1
j=1
while i<=5:
    while j<=5:
        print("i=",i,"j=",j,sep=" ")
        j+=1
    i+=1
    print("End")
    j=1
#---------------------------    
i=1
j=1
while i<=5:
    while j<=5:
        print("i=",i,"j=",j,sep=" ")
        j+=1
    else:
        print("J is End")
    i+=1
    j=1
#=============================for-loop==============================
for i in range(1,5+1):
    print(i)
#---------------------------------
for i in range(1,10+1,2):
    print(i)
#---------------------------------
for i in range(2,10+1,2):
    print(i)

#Nested loop----------------------
for i in range(1,10+1):
    for j in range(1,5+1):
        print("i=",i,"j=",j,sep=" ")
    print("         j is End")

#-----------------
for i in range(1,10+1):
    for j in range(1,5+1):
        print("i=",i,"j=",j,sep=" ")
    print("         j is End")
    break


#=================Break/Continue/Pass====================
#break--------------
for i in range(1,10):
    if i==3:
        break
    print(i)
#---------------
i=1
while i<=9:
    if i==4:
        break
    print(i)
    i+=1

# continue-------------
for i in range(1,10):
    if i==3:
        continue
    print(i)

#---------------
i=1
while i<=9:
    if i==4:
        continue
    print(i)
    i+=1
#pass--------------------
for i in range(1,10):
    if i==3:
        pass
    print(i)
#-------------------
i=1
while i<6:
    if i==3:
        pass
    print(i)
    i+=1