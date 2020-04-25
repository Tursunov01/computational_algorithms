import matplotlib.pyplot as plt
import numpy as np

def read_file(name):
    f = open(name, "r")
    matrix = [line.replace("\n", "").split() for line in f]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])
    return matrix
    
def input_n(N, flag):
    n = int(input("Input a degree of approximating polynomial: "))
    if n <= 0 or n >= N:
        flag = False
    return n

def print_data(matrix):
    print("|  x  |  y  |  p  |")
    print("-------------------")
    for i in range(0, len(matrix)):
            print('|  {}  |  {}  |  {}  |'.format(matrix[i][0],matrix[i][1], matrix[i][2]))

def print_matr(matr):
    for i in matr:
        print(i)

def change_mass(matrix):
    mass = float(input("Input a mass:"))
    result = str(input("Do you want change all mass in table to this number (y|n):  "))
    if result == "y":
        for i in range(0, len(matrix)):
            matrix[i][len(matrix[i]) - 1] = mass
    else:
        pos = int(input("Input i of mass from table to change: "))
        matrix[pos][len(matrix[pos]) - 1] = mass
    rec = str(input("Do you want continue to change mass (y|n):  "))
    if rec == "y":
        change_mass(matrix)

def choose_mode(matrix, n, a):
    mode = int(input("Choose mode from menu: "))
    if mode == 1:
        flag = True
        matrix = read_file("data.txt")
        n = input_n(len(matrix), flag)
        if flag == False:
            print("Error! You input wrong n. Try again")
    if mode == 2:
        if (len(matrix)):
            print_data(matrix)
        else:
            print("Error! Matrix doesn`t exist. Try again")
    if mode == 3:
         if (len(matrix)):
            change_mass(matrix)
         else:
            print("Error! Matrix doesn`t exist. Try again")
    if mode == 4:
        if len(matrix) > 0 and 0 < n < len(matrix):
            a = root_mean_square(matrix, n)
            print("a = ", a)
        else:
            print("Error! Input data is incorrect. Try again")
    if mode == 5:
        if a != True and len(matrix):
            show(a, matrix)
        else:
            print("Error! Input data is incorrect. Try again")
    rec = str(input("Do you want to choose mode (y|n):  "))
    if rec == "y":
       choose_mode(matrix, n, a)

def f(x_arr, coeff):
    res = np.zeros(len(x_arr))
    for i in range(len(coeff)):
        res += coeff[i]*(x_arr**i)
    return res        

def root_mean_square(matrix, n):
    length = len(matrix) 
    sum_x_n = [sum([matrix[i][0]**j*matrix[i][2] for i in range(length)]) for j in range(n*2 -1)]
    sum_y_x_n = [sum([matrix[i][0]**j*matrix[i][2]*matrix[i][1] for i in range(length)]) for j in range(n)]
    matr = [sum_x_n[i:i+n] for i in range(n)]
    for i in range(n):
        matr[i].append(sum_y_x_n[i])
    print_matr(matr)
    return gauss(matr)

def gauss(matr):
    n = len(matr)
    for k in range(n):
        for i in range(k+1,n):
            coeff = -(matr[i][k]/matr[k][k])
            for j in range(k,n+1):
                matr[i][j] += coeff*matr[k][j]
    print("\ntriangled:")
    print_matr(matr)
    a = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            matr[i][n] -= a[j]*matr[i][j]
        a[i] = matr[i][n]/matr[i][i]
    return a
    

### Отобразить результат
def show(a, matr):
    t = np.arange(-1.0, 5.0, 0.02)
    plt.figure(1)
    plt.ylabel("y")
    plt.xlabel("x")
    plt.plot(t, f(t, a), 'k')
    for i in range(len(matr)):
        plt.plot(matr[i][0], matr[i][1], 'ro', markersize=matr[i][2]+2)
    plt.show()

def main():
    print("MENU\n")
    print("1) Download file and input n\n")
    print("2) Print table\n")
    print("3) Change mass\n")
    print("4) Find root\n")
    print("5) Show graph\n")
    
    matrix = []
    n = 0
    a = True
    choose_mode(matrix, n, a)

main()
