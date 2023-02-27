#======================variable==========================
a=5
print(3+a)

a,b,c,d,e,f="anis",4,5,3.4,5,6
print(a,b,c,d,e,f,sep="\n")

a=b=c=d="anis"
print(a,b,c,d,sep="\n")

# k=[10,20,30,40]
# k[1:3]=[50]
# print(k)

# x=[-1,0,1][-1]
# print(x)

#1. Input type-keybord
a=input()
print(a)

# 2.prompt-display message
a=input("Enter The Number:")
print(a)

# 3.Get a string from the user
a=str(input("Enter your name: "))
b=int(input("Enter your age: "))
print("name: {}\n Age: {}".format(a,b))

#1.operation----------------------------
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#2 comparison/Relation-------------------
a=10
b=10
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#3 logical operation---------
a=10
b=5
print(a==10 and b==5)
print(a==10 or b==20)
print(not b == 5)

#4 membership operation-------
a="codinglaugh"
print("coding" in a)
print("coding" not in a)

#5 Identity Operators---------
a=5
b=6
print(a is b)
print(a is not b)

