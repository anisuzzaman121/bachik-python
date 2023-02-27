a=10
print(type(a))

#boolean----
print(10>20)
print(type(10>20))
#----------------------------
if 10>20:
    print("10 is small")
else:
    print("20 is big")
#----------------------------
a= 10<20
if a==True:
    print("10 is small")
else:
    print("20 is Big")

#Number:---------------------
#1.int
#2.float
#3.complex

a=10
print(type(a))

a=10.2354
print(type(a))

b=2.347585874
print("{:.2f}".format(b))

#complex---------
c=10+12j
print(c,type(c))

#string---------------
c='My name is "Anis"'
print(c)

#1 Multiline String---------
a=""" Bangladesh
 Indea
 Japan
 USA
"""
print(a)

#2 Positive index-----------
a="Codinglaugh"
print(a[3])

#3. negative index---------------
a="Codinglaugh"
print(a[-3])

#4. Range/slice----------
a="Codinglaugh"
print(a[2:5])

# 5. Change--------
a="Codinglaugh"
a=a[:3]+"M"+a[4:]
print(a)

b="amar sonar bangla"
b=b[:3]+"M"+b[4:]
print(b)

b="amar sonar bangla"
b=b[:3],"M",b[4:]
print(b)

#6delete----------
b="amar sonar bangla"
b=b[:3]+""+b[4:]
print(b)

#Loop-------------
b="amar sonar bangla"
for i in b:
    print(i)


b="amar sonar bangla"
for i in b:
    print(i, end="")
    
#8. lengh--------
b="amar sonar bangla"
length=0
for i in a:
    print(i,end="")
    length+=1
print()
print(length)


a="good Boy"
b=0
for i in a:
    print(i,"=",b+1,",",end="  ")
    b+=1
print()
print(b)

# or len-----
a="good Boy"
print(len(a))

# 9. Membership:-----------------
e="Bangladesh"
print("d" in e)

a="amar sonar bangla"
print("x" in a)

# 10.Concatenation:--------------
a="anis "
b="Husnara " 
c="I "
d="Love "
print(a+"+ "+b+c+d+"You")

#11. Repetition-----------------
a="anis "
print(a*5)

#12 Relation Operators------------
h="coding"
if "codinga" == h:
    print("matched")
else:
    print("something wrong")

a="abc"
b="ABC"
print(a<b)

#13. String Format-----
a="anis"
b=10
c=5.645
d=a+" {} {}".format(b,c)
print(d)


a="anis"
b=10
c=4.67859
d=a+" {0} {1}".format(b,c)
print(d)


a="anis"
b=10
c=4.67859
d=a+" {0} {1:.2f}".format(b,c)
print(d)

a="Anisuzzaman"
d="{:<30} Manik".format(a)
print(d)


c="Anisuzzaman"
d="{:^30} Manik".format(c)
print(d)

c="Anisuzzaman"
d="{0:^30}{1}".format(c,"Anis")
print(d)

c="Anisuzzaman"
d="{0:*>20}{1}".format(c,"Anis")
print(d)


c="Anisuzzaman"
d="{0:*<20}{1}".format(c,"Anis")
print(d)