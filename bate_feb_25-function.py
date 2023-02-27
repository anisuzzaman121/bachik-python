#-------------Function-----------
def anis():
    print("Function")
anis()
anis()
#-------------
def summation():
    print(1+2)
def subtraction():
    print(3-1)
summation()
subtraction()
#------------
def summation():
    return 1+1
def subtraction():
    return 11-1
print(subtraction())
print(summation())

# 1. Return---------------
def anis():
    return "Apple"
print(anis())

# 2. Arguments--- 3. parameters-----------
def bazar(item1,item2):
    print(item1,item2)
bazar("mango", "Egg")

#-----------------
def bazar(a1,a2):
    print(a1+a2)
bazar("apple","banana")

#-----------------
def bazar(age,old):
    return age,old
print(bazar("age =",27))

# 4. * args--------------------------
def bazar(* world):
    print(world)
bazar("mango","apple","egg")


#-----------------
def bazar(* anis):
    print(anis[1])
bazar("apple","egg","mango")


# for loop---------------
def bazar(* world):
    for i in world:
        print(i)
bazar("egg","anis","Babu")


# 5. Keyword arguments-----------------------
def bazar(item1,item2,item3):
    print(item1,item2,item3)
bazar(item1="Apple",item2="Egg",item3="Banana")

#----------------
def bazar(item,item1,item2):
    print(item,item1,item2)
bazar("anis",item1="egg",item2="shakil")

# 6. ** kwargs--------------
def bazar(** world):
    print(world)
bazar(item1="Anis",item2="Shakil",item3="Sonjoy")

#------------------------------
def bazar(** ar):
    print(ar["item3"])
bazar(item1="Egg",item2="mango",item3="Apple")

#--------Key print----------
def bazar(** world):
    for i in world:
        print(i)
bazar(item1="Egg",item2="mango",item3="Apple")


#--------Value prient---------
def bazar(** world):
    for i in world.values():
        print(i)
bazar(item1="Egg",item2="mango",item3="Apple")

#----------key and Value prient------
def bazar(** world):
    for i,j in world.items():
        print(i,"=",j)
bazar(item1="Egg",item2="mango",item3="Apple")


# 7. Default parameter------------------
def info(name,subtitle="coding"):
    print(name,subtitle)
info("Anis","student")
info("shakil")

#_____________
def hello(name,age=29):
    print(name,age)
hello("anis",34)
hello("shakil")


# 8. pass-----------------
def hey():
    pass
hey()

# 9.Instead of return------------
def hey():
    yield 1
    yield "Anis"
    yield ("HI","hi")
for i in hey():
    print(i)

#--------------
j=int(input("enter number:"))
def hello():
    for i in range(1,j+1):
        yield i
for i in hello():
    print(i)
    
#---------------
def hey():
    for i in range(1,6):
        yield i
for i in hey():
    print(i)

#-----------------
def hi():
    for i in range(0,5):
        yield i
for i in hi():
    print(i)
    
# 10. Recursion-------------
# def count(no):
#     if no==3:
#         return no
#     else:
#         return (no+1)+1
# print(count(1))


# ======================Nested Function=======================
def hey():
    x=10
    def hello():
        print(x)
    hello()
    print(x)
hey()

#-----------------------------
x=10
def hi():
    def hey():
        x=12
        print(x)
    hey()
    print(x)
hi()


# 2. Global Variable----------------
# 3. local Variable-----------------
# 4. Nonlocal Variable--------------

def china():
    z=12
    print("china",x,y,z)
def bangladesh():
    print("Bangladesh",x,y,z)
china()
bangladesh()
x=10
y=11
z=0
print(x,y,z)
china()


#---------------------------
def hi():
    global z
    z=12
    print("hi",x,y,z)
def hello():
    print("hello",x,y,z)
x=10
y=11
z=0
hello()
print("fast",x,y,z)
hi()
hello()
hi()
print("last",x,y,z)

#---------------------
def hi():
    global z
    z=12
    print("hi",x,y,z)
def hello():
    print("hello",x,y,z)
x=10
y=11
z=0
hi()
hello()
print("fast",x,y,z)
hi()

#---------------Nonlocal------------
def china():
    z=12
    def bangla():
        nonlocal z
        z=17
        print("bangla",z)
    bangla()
    print("china",z)
china()

#------lambda(anonymous function)----------------------
hi=lambda b,c:print(b+c)
hi(100,200)

#-----------------
def hey(a,b):
    print(a+b)
hi=lambda a,b:print(a+b)
hey(5,6)
hi(6,7)

#------------------
def hi(a,b):
    return a+b
hello=lambda a,b:print(a+b)
print(hi(10,20))
hello(20,20)

#-------------------
def anis(a,b):
    return a+b
shakil=lambda a,b:a-b
print(anis(30, 20))
print(shakil(30,20))

#-------------------
def hey(a):
    return lambda b:a*b
anis=hey(5)
print(anis(6))
print(anis(7))
print(anis(8))



