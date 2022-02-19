import math
from os import curdir
from numpy import string_
import pandas as pd
from datetime import date, datetime

def point_add(N_x, N_y, Q_x, Q_y, p):
    m = (Q_y - N_y) * pow((Q_x-N_x), p-2, p)
    ret_x = (m ** 2 - N_x - Q_x) % p
    ret_y = (m*(N_x - ret_x) - N_y) % p
    return ret_x, ret_y

def isPrime(p):
    if(p <= 1): return False
    if(p == 2): return True
    if(p%2 == 0): return False

    for i in range(3, int(math.sqrt(p))):
        if(p%i == 0): return False
        i += 2

    return True

def write_file(data, filename):
    filename += datetime.now().strftime(" %H %M %S ") + ".csv"
    pd.DataFrame(data).to_csv(filename, index=False)
    print("Output was written to ", filename)


def point_double(N_x, N_y, a, p):
    m = (3*(N_x ** 2)+a) * pow(2*N_y, p-2, p)
    ret_x = (m ** 2 - N_x - N_x) % p
    ret_y = (m*(N_x - ret_x) - N_y) % p
    return ret_x, ret_y

def multiplication_calculator(k, x, y, a, b, p):
    k = format(k, "b")
    binary = list(k)
    P = [x, y]
    P1 = [x, y]

    for i in range(1, len(k)):
        if binary[i] == '1':
            P = point_double(P[0], P[1], a, p)
            P = point_add(P[0], P[1], P1[0], P1[1], p)
            
        elif binary[i] == '0':
            P = point_double(P[0], P[1], a, p)
    return P

def multiplication():
    k = int(input("Enter the value of k : "))
    x = int(input("Enter the value of x : "))
    y = int(input("Enter the value of y : "))
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    p = int(input("Enter value of p : "))
    print("Point is: ", multiplication_calculator(k, x, y, a, b, p))

def order_curve(a, b, p):
    points = []
    X = []
    Y = []
    order = 1
    for n in range(p):
        #For X
        X.append(dict({'index': n, 'value': (((n * n * n) + (a * n) + (b % p)) % p)}))
        
        #For y
        Y.append(dict({'index': n, 'value': ((n * n) % p)}))
    
    for Px in X:
        for Py in Y:
            if Px['value'] == Py['value']:
                order += 1
    return order


def order_c():
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    p = int(input("Enter value of p : "))
    print("Order is:", order_curve(a, b, p))

def order_finder(x, y, a, b, p):

    Xc = (((x * x * x) + (a * x) + (b % p)) % p)
    Yc = ((y * y) % p)
    if(Xc != Yc):
        print("Given point doesnt lie on curve")
        return 

    order  = 2
    curve = order_curve(a, b, p)

    while True and order <= curve:
        print ("currently checking for", order, end="\r")

        X = multiplication_calculator(order, x, y, a, b, p)

        if X[0] == x and X[1] == y: break

        order += 1
    
    # if(order >= curve): order = curve
    return order-1

def order():
    x = int(input("Enter the value of x : "))
    y = int(input("Enter the value of y : "))
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    p = int(input("Enter value of p : "))
    print("\nOrder is: ", order_finder(x, y, a, b, p))

def order_finder_points(curve, x, y, a, b, p):

    Xc = (((x * x * x) + (a * x) + (b % p)) % p)
    Yc = ((y * y) % p)
    if(Xc != Yc):
        print("Given point doesnt lie on curve")
        return 

    order  = 2
    
    while True and order <= curve:
        print ("currently checking for", order, end="\r")

        X = multiplication_calculator(order, x, y, a, b, p)

        if X[0] == x and X[1] == y: break

        order += 1
    
    # if(order >= curve): order = curve
    return order-1

def points_finder_order(a, b, p):
    curve = order_curve(a, b, p)
    points = []
    X = []
    Y = []
    for n in range(p):
        #For X
        X.append(dict({'index': n, 'value': (((n * n * n) + (a * n) + (b % p)) % p)}))
        
        #For y
        Y.append(dict({'index': n, 'value': ((n * n) % p)}))
    
    for Px in X:
        for Py in Y:
            if Px['value'] == Py['value']:
                points.append(dict({'x': Px['index'], 'y': Py['index'], 'order': order_finder_points(curve, Px['index'], Py['index'],a, b, p)}))
                print("  (", Px['index'], ", ", Py['index'], ")  ")
    
    write_file(points, str(a)+ " " + str(b) + " " + str(p)+" with order")
    print("Order of curve is: ", (len(points) +1))

def points_order():
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    p = int(input("Enter value of p : "))
    points_finder_order(a, b, p)

def points_finder(a, b, p):
    points = []
    X = []
    Y = []
    for n in range(p):
        #For X
        X.append(dict({'index': n, 'value': (((n * n * n) + (a * n) + (b % p)) % p)}))
        
        #For y
        Y.append(dict({'index': n, 'value': ((n * n) % p)}))
    
    for Px in X:
        for Py in Y:
            if Px['value'] == Py['value']:
                points.append(dict({'x': Px['index'], 'y': Py['index']}))
                print("  (", Px['index'], ", ", Py['index'], ")  ")
    
    write_file(points, str(a)+ " " + str(b) + " " + str(p))
    print("Order of curve is: ", (len(points) +1))

def points():
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    p = int(input("Enter value of p : "))
    points_finder(a, b, p)

def squareroot_cal(a, p):
    roots = []
    if(a < 0 or p < 0):
        print("Square Root does not exists for given values")
        return roots

    if(p == 2 or not(isPrime(p))):
        print("Square exists only for odd primes")
        return roots

    for i in range(p):
        if((a%p) == ((i**2)%p)):
            roots.append(i)
            break
    
    print(len(roots))
    if(len(roots) <= 0):
        print("Square Root does not exists for given values")
        return roots
    
    roots.append(p-roots[0])
    return roots

    


def squareroot():
    a = int(input("Enter value of a : "))
    p = int(input("Enter value of p : "))
    print("Roots are: ", squareroot_cal(a, p))

def menu():
    print("1. Scalar multiplication")
    print("2. Points of EC")
    print("3. Order of point on EC")
    print("4. Order of EC")
    print("5. Square Root")
    print("6. Points of EC With order of each point")

    option = int(input("Choose from menu Options[1-6]: "))

    if option == 1:
        multiplication()
    elif option == 2:
        points()
    elif option == 3:
        order()
    elif option == 4:
        order_c()
    elif option == 5:
        squareroot()
    elif option == 6:
        points_order()
    else:
        print("Invalid option! try again")
        menu()

print("\033[H\033[2J")
menu()
