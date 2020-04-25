from math import *
import xlrd

def average(x, y):
    return (x+y)/2

def closeEnaught(x, y):
    if abs(x-y)<0.00001:
        return 1
    return 0

def print_file(x, y):
    print("Given file")
    print("---------------------")
    print("|    x    |    y    |")
    for i in range(0, len(x)):
        print("|" "{:8.2f}".format(x[i]), "|" "{:8.2f}".format(y[i]), "|")

def input_init():
    code = 0
    x = float(input("Input х: "))
    n = int(input("Input power of polinom: "))
    if n < 0:
        print("Error! Power of polinom must be greater than zero!")
        code = -1
    return code, x, n


def read_file():
    data_file = xlrd.open_workbook('./data1.xlsx')
    sheet = data_file.sheet_by_index(0)
    x = []
    y = []
    row_number = sheet.nrows

    if row_number > 0:
        for row in range(0, row_number):
            curx = float(str(sheet.row(row)[0]).replace("number:", ""))
            cury = float(str(sheet.row(row)[1]).replace("number:", ""))
            x.append(curx)
            y.append(cury)
            
    else:
        print("Error! Input file is empty!")
    return x, y

def form_arr(arrx, arry, x, n):
    i = 0
    cur_x = []
    cur_y = []

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
            cur_y.append(arry[j])
        for j in range(i + 1, i + low + 1):
            cur_x.append(arrx[j])
            cur_y.append(arry[j])
    if high > before and low < after:
        for j in range(0, i + 1):
            cur_x.append(arrx[j])
            cur_y.append(arry[j])
        for j in range(i + 1, i + 1 + low + high - before):
            cur_x.append(arrx[j])
            cur_y.append(arry[j])
    if high < before and low > after:
        for j in range(i + 1, len(arrx)):
            cur_x.append(arrx[j])
            cur_y.append(arry[j])
        for j in range(i - high - (low - after) + 1, i + 1):
            cur_x.append(arrx[j])
            cur_y.append(arry[j])
    return cur_x, cur_y

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

def search(negPoint, posPoint, n, arrx, arry):
    midPoint=average(negPoint, posPoint)
    if closeEnaught(negPoint, posPoint):
        return midPoint
    keys_x1, keys_y1 = form_arr(arrx, arry, midPoint, n)
    keys_x1.sort()
    keys_y1.sort()
    testValue = polinom(keys_x1, keys_y1, midPoint)
    if testValue>0:
        return search(negPoint, midPoint, n, arrx, arry)
    elif testValue<0:
        return search(midPoint, posPoint, n, arrx, arry)
    return midPoint

def halfIntervalMethod(a ,b, n, arrx, arry):
    keys_x1, keys_y1 = form_arr(arrx, arry, a, n)
    keys_x1.sort()
    keys_y1.sort()
    if len(keys_x1) != 0 and len(keys_y1) != 0:
        aVal = polinom(keys_x1, keys_y1, a)
        keys_x2, keys_y2 = form_arr(arrx, arry, b, n)
        keys_x2.sort()
        keys_y2.sort()
        if len(keys_x2) != 0 and len(keys_y2) != 0:
            bVal = polinom(keys_x2, keys_y2, b)
            if aVal>0 and bVal<0:
                return search(b, a, n, arrx, arry)
            elif aVal<0 and bVal>0:
                return search(a, b, n, arrx, arry)
            else:
                print ("Arguments has equal signs")
                return 0
        else:
            print("Error! x is out of range of our table of x's")
            return 0
            
    else:
        print("Error! x is out of range of our table of x's")
        return 0

    

def main():
    print("Program starts...")
    #print("Given function is (x + 6)^3")
    
    arrx, arry = read_file()
    print_file(arrx, arry)
    arrx.sort()
    arry.sort()

    print("---------------------")
    print("|        MENU      |")
    print("1) Find y(x)")
    print("2) Find the root of the equation by half division")
    print("3) Back interpolation")

    key = int(input("Press any option from menu: "))
    if key == 1:
        code, x, n = input_init()          
        if code == 0:
            if arrx[0]<= x <= arrx[len(arrx) - 1]:
                keys_x, keys_y = form_arr(arrx, arry, x, n + 1)
                keys_x.sort()
                keys_y.sort()
                if len(keys_x) != 0 and len(keys_y) != 0:
                    print("Polinom = {:5.8f}".format(polinom(keys_x, keys_y, x)))
            else:
                print("Error! x is out of range of our table of x's")
    if key == 2:
        n = int(input("Input power of polinom: "))
        if n >= 0:
            result = halfIntervalMethod(arrx[0], arrx[len(arrx) - 1], n + 1, arrx, arry)
            if result != 0:
                print("Root = {:5.4f}". format(result))
    if key == 3:
        n = int(input("Input power of polinom: "))
        if n >= 0:
            keys_y, keys_x = form_arr(arry, arrx, 0, n + 1)
            if n <= len(keys_x):
                if len(keys_x) != 0 and len(keys_y) != 0:
                    print("Back interpole = {:5.5f}".format(polinom(keys_y, keys_x, 0)))
            else:
                print("Error! Out of range.")

main()
    


