# pow5 = lambda x : (x**2)*(x**2)*(x**2)
# b=float(input('Please insert the number'))
# print(pow5(b))
#a=1
#for i in range(2):
#    for j in range(3):
#       a+=1
#        print(f" a is: {a}, i is {i}, j is {j}")
# print(a)
def function1():
   a=1
   b=2
   for i in range(1,10,3):
 
    for j in range(2,12,4):
            a+=b
            b+=1
            print(f" a is: {a}, b is: {b} , i is {i}, j is {j}")
def function2():
    a=1
    b=2
    c=3
    for i in range(1,10,5):
        for j in range(2,12,6):
            a+=2
            b+=3
            c+=4
            print(f" a is: {a}, b is: {b} , c is {c}: i is {i}, j is {j}")

def function3():
    a=1
    b=2
    c=3
    for i in range(2,10,4):
        for j in range(1,9,2):
            a+=b
            b+=c
            c+=2
            print(f" a is: {a}, b is: {b} , c is {c}: i is {i}, j is {j}")
        #print(a,b,c)

#function3()
        
def function4():
    a=1
    b=2
    c=3
    for i in range(2,12,3):
        for j in range(9,16,3):
            a+=2
            b+=3
            c+=1
            print(f" a is: {a}, b is: {b} , c is {c}: i is {i}, j is {j}")
        #print(a,b,c)

#function4()       

def function5():
    a=1
    b=1
    c=1
    list1=[]
    for i in range(1,8,3):
        for j in range(2,10,4):
            a+=1
            b+=a
            c+=b
            list1.append([a,b,c])
            print(f" a is: {a}, b is: {b} , c is {c}: i is {i}, j is {j}, list1 is: {list1}")
            #print(list1)
        
#function5()    

def function6():
    a=1
    b=1
    c=1
    list1=[]
    for i in range(2,5,2):
        for j in range(3,8,2):
            for k in range(4,10,3):
                a+=1
                b+=b
                c+=c
                list1.append([a,b,c])
                print(f" a is: {a}, b is: {b} , c is {c}: i is {i}, j is {j}, k is {k} list1 is: {list1}")
                #print(list1)
        
function6()     
