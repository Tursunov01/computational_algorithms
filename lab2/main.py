from math import *

def print_file(x, y, z):
    print("Given file")
    print("---------------------")
    print("\nx/y", end = ' ')
    for i in range(0, len(y)):
        print(y[i], end = '  ')
    print("\n")
    for i in range(0, len(z)):
        print(x[i], end = '   ')
        for j in range(0, len(y)):
            print(z[i][j], end = '  ')
        print("\n")

def input_init():
    code = 0
    x = float(input("Input х: "))
    nx = int(input("Input power of polinom for x: "))
    y = float(input("Input y: "))
    ny = int(input("Input power of polinom for y: "))
    if nx < 0 or ny < 0:
        print("Error! Power of polinom must be greater than zero!")
        code = -1
    return code, x, y, nx, ny


def read_file():
    f = open('data1.txt', 'r')
    matrix_row = [line.replace("\n", "").split() for line in f]
    x = []
    y = matrix_row[0] 
    for i in range(1, len(matrix_row)):
        x.append(matrix_row[i][0])
    matrix_row.remove(matrix_row[0])
    for i in range(0, len(matrix_row)):
        del(matrix_row[i][0])
    for i in range(0, len(x)):
        x[i] = float(x[i])
    for i in range(0, len(y)):
        y[i] = float(y[i])
    for i in range(0, len(matrix_row)):
        for j in range(0, len(matrix_row[i])):
            matrix_row[i][j] = float(matrix_row[i][j])
            
    return x, y, matrix_row

def form_arr(arrx, x, n):
    i = 0
    cur_x = []
    pos_x = []

    while i < len(arrx) - 1:
        if  arrx[i] <= x <= arrx[i + 1]:
            pos = i
        i = i + 1
    after = len(arrx) - pos - 1
    before = len(arrx) - after
    i = pos
    high = floor(n / 2)
    low = n - high
    if high <= before and low <= after:
        for j in range(i - high + 1, i + 1):
            cur_x.append(arrx[j])
            pos_x.append(j)
        for j in range(i + 1, i + low + 1):
            cur_x.append(arrx[j])
            pos_x.append(j)
    if high > before and low < after:
        for j in range(0, i + 1):
            cur_x.append(arrx[j])
            pos_x.append(j)
        for j in range(i + 1, i + 1 + low + high - before):
            cur_x.append(arrx[j])
            pos_x.append(j)
    if high < before and low > after:
        for j in range(i + 1, len(arrx)):
            cur_x.append(arrx[j])
            pos_x.append(j)
        for j in range(i - high - (low - after) + 1, i + 1):
            cur_x.append(arrx[j])
            pos_x.append(j)
    return cur_x, pos_x


        
def newton(x, y, i, n):
    return ((y[i + 1] - y[i]) / (x[i + n] - x[i]))
    
def polinom(arrx, arry, x):
    koef = 1
    summ = arry[0]
    cur = []
    i = 0
    n = 1
    j = 0
    k = len(arry)
    while i < k - 1:
        cur.append(newton(arrx, arry, i, n))
        i = i + 1
        if i + 1 == k:
            arry = cur
            koef = koef * (x - arrx[j])
            summ = summ + koef * cur[0]
            cur = []
            j = j + 1
            i = 0
            n = n + 1
            k = len(arry)
    return float(summ)    


def find_range(arrx, arry, matr_z, x, nx, y, ny):
    cur_x, pos_x = form_arr(arrx, x, nx)
    cur_y, pos_y = form_arr(arry, y, ny)
    arr_z = []
    z_x = []
    for i in range(0, len(pos_x)):
        for j in range(0, len(pos_y)):
            arr_z.append(matr_z[pos_x[i]][pos_y[j]])
        z_x.append(polinom(cur_y, arr_z, y))
        arr_z = []
    result = polinom(cur_x, z_x, x)
    return result

##def find_range(arrx, arry, matr_z, x, nx, y, ny):
##    cur_x, pos_x = form_arr(arrx, x, nx)
##    cur_y, pos_y = form_arr(arry, y, ny)
##    print(cur_x)
##    print(cur_y)
##    arr_z = []
##    z_y = []
##    for i in range(0, len(pos_y)):
##        for j in range(0, len(pos_x)):
##            arr_z.append(matr_z[pos_y[i]][pos_x[j]])
##        print(arr_z)
##        z_y.append(polinom(cur_x, arr_z, x))
##        arr_z = []
##    result = polinom(cur_y, z_y, y)
##    return result

def main():
    print("Program starts...")
    arrx, arry, arrz = read_file()
    print_file(arrx, arry, arrz)

    print("---------------------")
    code, x, y, nx, ny = input_init()          
    if code == 0:
        if float(arrx[0]) <= float(x) <= float(arrx[len(arrx) - 1]):
            print("Polinom = ", find_range(arrx, arry, arrz, x, nx + 1, y, ny + 1))
        else:
            print("Error! x is out of range of our table of x's")

main()
    


