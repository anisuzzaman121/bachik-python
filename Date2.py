#print function use...............................
print("I love Bangladesh")

#1. value -object
print("Bangladesh",11,3.5)

#2. sep-sepace
print("Bangladesh",11,3.5,sep="-")

#3. End
print("Bangladesh",end="*")
print("Bangladesh",end="\n\n")
print("Bangladesh")

#print multipule arguments..........................
#1. pass valu as a parameters
a="I"
b="love"
c="you"
print("Hey,",a,b,c)

#2 use string formatting
        #2.1 sequential formatting pass value:
a="I"
b="Love"
c="You"
print("Anis {} {} {}".format(a,b,c))
print("Do {} {} me".format(c,b))
print("{} love {}".format(a,c))

        #2.2 formating number:
a="I"
b="you"
c="me"
print("{1} love {0}".format(c,b))

        #2.3 formating with explicit number:
a="I"
b="you"
c="me"
print("{name} love {name2}".format(name=a,name2=b))

#3 pass valu as a tuple
a="I"
b="you"
c="me"
print("%s love %s" %(a,b))

#4 pass valu as a dectionary
a="I"
b="you"
c="me"
print("%(hey)s love %(hello)s" %{"hey":a,"hello":b})

