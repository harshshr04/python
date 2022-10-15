print(20%10) 
print(15//2)


x=2
y=3
print(x**y)



a=20


a+=5
print(a)

a*=5# same as a=a*5

a/=5 # same as a=a/5


a%=5 # same as  a= a % 5
print (a)

a//=3# a=a//3
print(a)

a **=2 # a=a**2 i.e. 20 * 20
#print(a)




print(3==4) # Equal to print whether it is true or false


print(3!=4) # not equal 


print(3>4)#greater than
print(3<4)#less than

print(3>=4)#greater than equalt
print(3<=4)#less than equal to






x=2

print(x<5 and x<8) # here and is used as it is used for both return true if both statement are true



print(x<5 or x>8) # return true if any one of the given condition is true



print(not(x<5 and x>8))# reverse the result for eg if the result is true it will return false and vice versa




a=[10,20]# these are list
b=[10,20]# these are list
c=a

a.remove(20) # to remove a variable from a list
print (a)
print(b)
print(c)

print(a is c) # returns true if both the variables are the same object  pointing to the same memory location


print(b is c) # it will return false because b is not pointing  to the same memory location        
