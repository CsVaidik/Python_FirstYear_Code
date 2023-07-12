def p1():
    print("Hello World!")

def p2():
    a = int(input("Enter the number :"))
    b = int(input("Enter the number :"))
    c = a + b 
    print("Sum of {} & {} is {}".format(a,b,c))
    
def p3():
    a = int(input("Enter the 1st Number :"))
    b = int(input("Enter the 2nd Number :"))
    Q = a // b
    R = a % b
    print("Quotient is {} & Remainder is {}".format(Q,R))

def p4():
    a = int(input("Enter the 1st Number :"))
    b = int(input("Enter the 2nd Number :"))
    c = int(input("Enter the 3rd Number :"))
    Avg = (a + b + c)/3
    print("Average of a three number is {}".format(Avg))

def p5():
    a = float(input("Enter the Marks of Physics: "))
    b = float(input("Enter the Marks of Chemistry :"))
    c = float(input("Enter the Marks of Maths :"))
    d = float(input("Enter the Marks of English :"))
    e = float(input("Enter the Marks of Cs :"))
    Sum = a + b + c + d + e
    pr = (Sum/500)*100
    print("Sum of a 5 subjects is {} And Percentage is {}".format(Sum,pr))

def p6():
    ta = float(input("Enter The ta Salary : "))
    da = float(input("Enter The da Salary : "))
    basic = float(input("Enter The Basic Salary : "))
    hra = float(input("Enter The hra Salary : "))
    Gs = ta + da + basic + hra
    print("The Gross Salary of Employee is {}".format(Gs))

def p7():
    l = float(input("Enter the length :"))
    b = float(input("Enter the breath :"))
    Ar = l*b
    print("Area of Rectangle is",Ar)
    s = float(input("Enter the Side of Square :"))
    As = s*s
    print("Area of Square is",As) 

def p8():
    a = float(input("Enter the 1st Side :"))
    b = float(input("Enter the 2nd Side :"))
    c = float(input("Enter the 3rd Side :"))
    s = (a+b+c)/2
    ar = (s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of a Scalene Triangle is",ar)
    p = float(input("Enter The perpendicular Height :"))
    b = float(input("Enter The Base Lenght :"))
    RA = (b*p)/2
    print("And Area of Right Angle Triangle is ",RA)

def p9():
    l = float(input("Enter the l :"))
    b = float(input("Enter the b :"))
    h = float(input("Enter the h :"))
    Vc = l*b*h
    Sc = 2*((l*b)+(b*h)+(h*l))
    print("Volume of Cuboid is {} And Surface area of Cuboid is {}".format(Vc,Sc))
    s = int(input("Enter the side :"))
    Vcu = s**3
    Scu = 6*(s**2)
    print("Volume of Cube is {} And Surface area of Cube is {}".format(Vcu,Scu))
    pi = 3.14
    r = float(input("Enter the Radius :"))
    h1 = float(input("Enter the Hieght of Cylinder :"))
    Vcc = pi*(r**2)*h1
    Scc = 2*pi*r*(r+h1)
    print("Volume of Cylinder is {} And Surface area of Cylinder is {}".format(Vcc,Scc))

def p10():
    pi = 3.14
    h = float(input("Enter the Height :"))
    r = float(input("Enter the Radius :"))
    cv = (1/3)*pi*h
    cs = pi*r*(r+((h**2+r**2)*0.5))
    sv = (4/3)*pi*r**3
    ss = 4*pi*(r**2)
    print("Volume of Cone is {} And Surface area of cone is {}".format(cv,cs))
    print("Volume of Sphere is {} And Surface area of Sphere is {}".format(sv,ss))

def p11():
    d1 = float(input("Enter The Diagonal lenght 1 :"))
    d2 = float(input("Enter The Diagonal lenght 2 :"))
    rh = (d1 + d2)/2
    print("Area of a rhombus :",rh)
    
    print("                        ")
    a = float(input("Enter length of parallel side 1 : "))
    b = float(input("Enter length of parallel side 2 : "))
    h = float(input("Enter the hieght of a trapezium :"))
    tr = (h/2)*(a + b)
    print("Area of a Trapezium :",tr)
    
    print("                        ")
    bs = float(input("Enter the base :"))
    he = float(input("Enter the height : "))
    prl = bs * he
    print("Area of a Parellogram :",prl)
    
def p12():
    pi = 3.14 
    r = int(input("Enter the radius : "))
    pr = 2*pi*r
    print("Perimeter of a Circle :",pr)
    
    print("                 ")
    l = float(input("Enter the lenght : "))    
    b = float(input("Enter the breath : "))
    pr2 = 2*(l+b)
    print("Perimeter of Rectangel :",pr2)
    
    print("                             ")
    a = float(input("Enter the a side : "))    
    b = float(input("Enter the b side : "))
    c = float(input("Enter the c side : "))
    p = a + b + c
    print("Perimeter of a Triangle :",p)
    
    
def p13():
    p = float(input("Enter the p"))
    r = float(input("Enter the r"))
    t = float(input("Enter the t"))
    si = (p*r*t)/100
    print("Simple interest is ",si)

def p14():
    f = float(input("Enter the Fahrenhiet :"))
    c = (f-32)*(5/9)
    print("Fahrenhiet to celcius is ",c)

def p15():
    G = 45
    m1 = float(input("Enter the mass m1 : "))     
    m2 = float(input("Enter the mass m2 : ")) 
    d = float(input("Enter the distance d : "))
    f = G * ((m1+m2)/d)
    print("Gravitational Force acting between two bodies is :",f)
    

def p16():
    a = int(input("Enter the 1st number :"))
    b = int(input("Enter the 2nd number :"))
    print("a = ",a,"b = ",b)
    a,b = b,a
    print("Now a = ",a,"Now b = ",b)

def p17():
    a = 8
    b = 3
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    print(add,sub,mul,div)

def p18():
    print("relational operations")
    print("a=8 and b=3")
    a=8
    b=3
    print(a==b)
    print(a!=b)
    print(a>=b)
    print(a<=b)
    print(a<b)
    print(a>b)

def p19():
    print("assignment operations")
    print("a=8 and b=3")
    a=8
    b=3
    a += b
    print(a)
    a=8
    a -=b
    print(a)
    a=8
    a *= b
    print(a)
    a=8
    a /= b
    print(a)
    a=8
    a %= b
    print(a)
    a=8
    a //= b
    print(a)
    a=8
    a **= b
    print(a)

def p20():
    print("logical operations")
    print("a=8 and b=3")
    a=8
    b=3
    print(a and b)
    print(a or b)
    print( not a)

def p21():
    print("bitwise operations ")
    print("a=8 and b=3")
    a=8
    b=3
    print(a & b)
    print(a | b)
    print(a ^ b)
    print( ~ b)
    print(a << b)
    print(a >> b)

def p22():
    print ("identity operations")
    print("a=8 and b=3")
    a=8
    b=3
    print(a is b)
    print(a is not b)

def p23():
    print("swap number using bitwise XOR")
    print("a=8 and b=3")
    a=8
    b=3
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("a is {} and b is {}".format(a,b))

# def p24():

def p25():
    n = int(input("Enter The Number :"))
    r = n**0.5
    print("Square Root of a Number is ",r)

def p26():
    h = int(input("Enter the hours :"))
    hs = h * 3600
    m = int(input("Enter the minute :"))
    ms = m * 60
    tt = hs + ms
    print("{}hour {}min is {}sec".format(h,m,tt)) 
    
def p27():
    x1 = int(input("Enter the x1 "))
    x2 = int(input("Enter the x2 "))    
    y1 = int(input("Enter the y1 "))
    y2 = int(input("Enter the y2 "))   
    x = (x1 + x2)/2
    y = (y1 + y2)/2
    print("Midpoint of a line segment ({},{}) & ({},{}) is ({},{})".format(x1,x2,y1,y2,x,y))
    
def p28():
    N = input("Enter Your Name :")
    a = int(input("Enter your Age :"))
    ad = input("Enter Your Address :")
    print("Name : {}\nAge : {}\nAddress : {} ".format(N,a,ad))     
    
def p29():
    x1 = int(input("Enter the x1 "))
    x2 = int(input("Enter the x2 "))    
    y1 = int(input("Enter the y1 "))
    y2 = int(input("Enter the y2 "))  
    d = ((x2-x1)**2 + (y2-y1)**2  )*0.5
    print("Distance Betwwen the Points is ",d)
     
     
def p30():
    n = int(input("Enter the number :"))
    print("The Absolute of given num is :",abs(n))
    
#def p31():



def p32():
    c = -9+9-8*6%8-int(19//10//2)|12&14
    print("The Values is ",c)
       
def p33():
    St = "Hello World!"
    print(St)
    print("The Reverse of a String is : ",St[::-1])
    
def p34():
    s = "GOKUGOHAN"
    print(s)
    print("The Reverse of a String is : ",s[0::2])

#Condition Statement 

def p35():
    a = int(input("Enter the A number : "))
    b = int(input("Enter the B number : "))
    if a == b:
        print("A is Equal to B ")
    else:
        print("A is Not Equal to B")
        
        
def p36():
    n = int(input("Enter the number :"))
    if n > 0 :
        print(n,"is Positive")
    elif n < 0 : 
        print(n,"is Negative")
    elif n % 2 == 0 :
        print(n,"is Even")
    elif n % 2 != 0 :
        print(n,"is odd")
    else :
        print("Wrong Input !!!")
        
def p37():
    n = int(input("Enter the Number :"))
    
    if n % 7 == 0 :
        print("Divisible by 7")
    else :
        print("Not Divisible by 7")
          

def p38():
    a = int(input("Enter Num A : "))
    b = int(input("Enter Num B : "))
    c = int(input("Enter Num C : "))
    
    if a > b and a > c :
        print("A is Greater")
    elif b > a and b > c :
        print("B num is Greater")
    else :
        print("C num is Greater")
        
def p39():
    a = int(input("Enter Num A : "))
    b = int(input("Enter Num B : "))
    c = int(input("Enter Num C : "))
    
    if a > b :
        if a > c :
            print("A is greatest ")
        else :
            print("B is Greatest ")
    else :
        if b > c : 
            print("B is Greatest ")
        else : 
            print("C is Greatest ")

def p40():
    s = input("Enter The Character :")  
    nS = ""  
   
    for i in range(0, len(s)):  
        if s[i].islower():  
            nS += s[i].upper()  
        elif s[i].isupper():    
            nS += s[i].lower()  
        else:  
            nS += s[i]          
    print("Character Conversion : ", nS) 
    
def p41():
    y = int(input("Enter the Year :"))
    
    if y % 4 == 0 :
        print("The Year is Leap year ")
    else :
        print("The Year is Not Leap Year ") 
        
def p42():
    ch = input("Enter A Character :")
    
    if ch=='a'or ch=='A' or ch=='e'or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U':
        print(ch,"Is Vowels")  
    else :
        print(ch,"Is consotant")
        
def p43():
    x = float(input("Enter x-axis : "))
    y = float(input("Enter y-axis : "))
    if x > 0 and y > 0 :
        print("The Coordinate Are in First Quadrant ")
    elif x < 0 and y > 0 :
        print("The Coordinate Are in Second Quadrant ")
    elif x < 0 and y < 0 :
        print("The Coordinate Are in Third Quadrant ")
    elif x > 0 and y < 0 :
        print("The Coordinate Are in Fourth Quadrant ")
    else :
        print("Wrong input!!!")

def p44():
    print("Format for writing complex number: a+bj.\n")
    c1 = complex(input("Enter First Complex Number: "))
    c2 = complex(input("Enter second Complex Number: "))
    print("Sum of both the Complex number is", c1 + c2)

def p45():
    a = int(input("Enter the a : "))
    b = int(input("Enter the b : "))
    c = int(input("Enter the c : "))
    d = (b**2) - (4*a*c)
    x1 = (b + (d**0.5))/2*a  #taking +iv
    x2 = (b - (d**0.5))/2*a  #taking -iv
    print("The Root of a Given Equation is :",x1,x2)
    
def p46():
    days =["Monday", "Tuesday", "Wednesday", "Thursday",
       "Friday", "Saturday","Sunday"]
    n= int(input("Enter Day"))
    if n==(1):
        print("monday")
    elif n==(2):
        print("tuesday")
    elif n==(3):
        print("wednesday")
    elif n==(4):
        print("thurday")
    elif n==(5):
        print("friday")
    elif n==(6):
        print("saturday")
    elif n==(7):
        print("sunday")


#def p47():



def p48():
    a = int(input("Enter 1st num : "))
    b = int(input("Enter 2nd num : "))
    
    print("""Press 1 for Adding
                  Press 2 for Subtracring
                  Press 3 for Dividing
                  Press 4 for Multiply """)
    
    c = input("Enter Operation :")
    
    if c == '1' :
        n = a + b
        print("Sum of {} & {} is {}".format(a,b,n))
    elif c == '2' :
        n = a - b
        print("Subtracting  of {} & {} is {}".format(a,b,n))
    elif c == '3' :
        n = a/b
        print("Dividing  of {} & {} is {}".format(a,b,n))
    elif c == '4':
        n = a * b
        print("Multiply  of {} & {} is {}".format(a,b,n))
    else :
        print("Wrong choice")

def p49():
    print("""Press 1 for Area of Circle
                  Press 2 for Area of Square
                  Press 3 for Area of Rectangle
                  Press 4 for Area of Triangle""")
    
    ch = input("Enter Operation :")
    if ch == '1' :
        pi = 3.14
        r = int(input("Enter The Radius :"))
        c = pi*(r**2)
        print("Area of Circle is :",c)
    elif ch == '2' :
        s = int(input("Enter Side of a Square :"))
        sq = s*s
        print("Area of a Square is :",sq)
    elif ch == '3' :
        l = int(input("Enter the lenght :"))
        b = int(input("Enter the breath :"))
        r = l*b
        print("Area of a Rectangle is :",r)
    elif ch == '4' :
        a = float(input("Enter the 1st Side :"))
        b = float(input("Enter the 2nd Side :"))
        c = float(input("Enter the 3rd Side :"))
        s = (a+b+c)/2
        ar = (s*(s-a)*(s-b)*(s-c))**0.5
        print("Area of a  Triangle is",ar)
        
    else :
        print("Wrong Input !!")
        
        
def p50():
    m1 = float(input("Enter the marks of Maths : "))
    m2 = float(input("Enter the marks of English : "))    
    m3 = float(input("Enter the marks of Phsics : "))
    m4 = float(input("Enter the marks of Chemistry : "))
    m5 = float(input("Enter the marks of Cs : "))
    s = m1 + m2 + m3 + m4 + m5
    pr = (s/500)*100
    print("Percentage of 5 marks :",pr)
    
    if pr >= 90 :
        print("Grade A")
    elif pr >= 80:
        print("Grade B")
    elif pr >= 60 :
        print("Grade C")
    elif pr >= 50 :
        print("Grade D")
    elif pr >= 40 :
        print("Grade E")
    else :
        print("Grade f")

# Q51 is repeat

def p52():
    n = int(input("Enter the Range :"))

    for i in range(1,n+1):
        if i % 2 == 0 :
            print(i)

def p53():
    n = int(input("Enter the Range :"))

    for i in range(1,n+1):
        if i % 7 == 0 :
            print(i)

def p54():
    n = int(input("Enter the number for Table :"))

    for i in range(1,11):
        p = n * i 
        print(p)

def p55():
    for i in range(1,10):
        if i == 4:
            continue
        print(i,end = "")
        
        
def p56():        
     n = int(input("Enter the number for Table :"))
     for i in range(1,11):
            T = n * i
            print("{} X {} = {} ".format(n,i,T))

def p57():
    n = int(input("Enter the number :"))
    s = 0
    for i in range(1,n+1):
        s += i
        print("Sum of first {} Natural Number is {}".format(n,s))

def p58():
    print("By Using For loop ")
    n = int(input("Enter the Number : "))
    f = 1
    for i in range(1,n+1):
        f *= i
    print("Factorial of Given number is",f)
    print("")
    print("By While Loop")

    j = 0
    f1 = 1
    while i <= n :
        f *= i
        i += 1
    print("Factorial1 of Given number is",f1)

def p59():
    n = int(input("Enter the Number :"))
    c = 0
    s = 0
    while n > 0 :
        r = n % 10
        s = s + r
        c = c + 1
        n = n // 10
    print("Count of Given Number is {} And Sum of digit of a number is {} ".format(c,s))
    
def p60():
    n = int(input("Enter the Number :"))
    s = 0
    while n > 0 :
        r = n % 10
        s = s*10 + r
        n = n // 10
    print("Reverse of a Number is ",s)

#def p61():
    
def p62():
    n = int(input("Enter the Number :"))
    s = 0
    i = len(str(n))
    Dia = n
    while n > 0 :
        r = n % 10
        s = s + r**i
        i = i - 1
        n = n // 10
    if Dia == s :
        print("The Number is Disarium")
    else :
        print("The Number is not Disarium")

def p63():
    n = int(input("Enter the Number :"))
    s = 0
    h = n
    while n > 0 :
        r = n % 10
        s = s + r
        n = n // 10
    if h % s == 0 :
        print("The number is Harsad Number")
    else :
        print("The number is not Harsad Number")
    
def p64():
    
    for j in range(1,1001):
        s = 0
        i = len(str(j))
        arm = j
        while j > 0 :
            r = j % 10
            s = s + r**i
            j = j // 10
        if s == arm :
            print(s)
            
def p65():
    X = int(input("Enter The Value of X : "))
    n = int(input("Enter the Value of n : "))
    c = X**n
    print(c)

#def p66():
    
    
def p67():
    n = int(input("Enter the number of terms :"))
    a = -1
    b = 1
    i = 1
    while i <= n:
        c = a + b
        a = b
        b = c
        i = i+1
        print(c)

    
def p68():
    n = int(input("Enter the Number :"))
    s = 0
    pal = n
    while n > 0 :
        r = n % 10
        s = s*10 + r
        n = n // 10
    if pal == s:
        print("The Number is Palindrome")
    else :
        print("The Number is not Palindrome")


def p69():
    n = int(input("Enter the num :"))
    i = len(str(n))
    s = 0 
    Arm = n
    while n > 0 :
        r = n % 10
        s = s + r**i
        n = n // 10
    if s == Arm :
        print("The number is Armstrong Number ")
    else :
        print("The number is not Armstrong  ")

#def p70(): # Doubt
   
        
       
def p73():
    n = int(input("Enter the Number :"))

    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*",end = '')
        print()

    
        
def p74():
    n = int(input("Enter "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end =" ")
        print()

def p75():
    n = int(input("Enter "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end =" ")
        print()

       
def p76():
    n = int(input("Enter "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end =" ")
        print()

    

def p77():
    for i in range(65,70):
        for j in range(65,i+1):
            print(chr(i),end = " ")
        print()           
    
    
def p78():
    n = int(input("Enter the number of rows : "))

    for i in range(n+1,0,-1):
        for j in range(0,i-1):
            print("*", end = " ")
        print()
    
def p79():
    n = int(input("Enter the number of rows : "))

    for i in range(n,0,-1):
        for j in range(0,i-1):
            print(i, end = " ")
        print()


        
def q001():
    n = int(input("Enter the number of rows : "))

    for i in range(1,n+1):
        for j in range(1,n+1-i):
            print(" " , end = "")
        for j in range(1,i+1):
            print("*",end = "")
        print()

def r1():
    l = [1,2,3,4,5,6,7,8,9]
    s = 0
    for i in l:
         s +=i
    print(s)
        
def r2():
    l = [1,2,3,4,5,6,7,8,9]
    s = 0
    for i in l:
        s +=i
        if i == 5 :
            break
    print(s)    
    

