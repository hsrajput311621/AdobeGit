w=("Welcome to jungle")
print(w[6])
#output: e
print(w[-2])
#output:l from right
print(w[0:7])
#Welcome
print(w[0:10:2])
#Wloet
print(w[0: :2])
#Wloet uge
print(w[-1::-2])
#egu teolW
print(w[-1:-10:-2])
#egu t
print(w[-1::-1])
#elgnuj ot emocleW

#String Iteration in python

a="I am a Automation Engineer working in Adobe"
t=len(a)
print(t)

for i in range(t):
    print(a[i])

#reverse iteration in python

a="I am a Automation Engineer working in Adobe"
t=len(a)
print(t)
for i in range(t-1,-1,-1):
    print(a[i])

#iteration of string without length keyword

a="I am a Automation Engineer working in Adobe"
for i in range(43):
    print(a[i])

#Other methods for iteration

a="I am a Automation Engineer working in Adobe"
for i in a:
    print(i)

