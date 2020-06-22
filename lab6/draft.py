from math import e, log

a0, a1, a2 = 1, 2, 3
'''
def f(x):
    return e**x
def psi(y):
    return log(y)
'''
def f(x):
    return (a0*x / (a1 + a2*x))
def f_det(x):
    return (a0*(a1+a2*x)-a0*a2*x)/((a1+a2*x)**2)

def etaksi(): # производная эта по кси
    return a1/a0

def etay(y): # производная эта по у
    return y * y

def ksix(x): # производная кси по х
    return 1 / (x*x)


def get_table(x_beg, step, amount):
    x_tbl = [x_beg + step*i for i in range(amount)]
    y_tbl = [f(x) for x in x_tbl]
    return x_tbl, y_tbl


def left_side_diff(y, h):
    return [None if not i
            else ((y[i] - y[i - 1]) / h)
            for i in range(len(y))]


def right_side_diff(y, h):
    return [None if i == len(y) - 1
            else ((y[i + 1] - y[i]) / h)
            for i in range(len(y))]          


def center_diff(y, h):
    return [None if not i or i == len(y) - 1
            else (y[i + 1] - y[i - 1]) / (2*h)
            for i in range(len(y))]


def edge_accuracy(y, h):
    n = len(y)
    a = [None for i in range(n)]
    a[0] = (-3 * y[0] + 4 * y[1] - y[2]) / (2 * h)
    a[n-1] = (y[n - 3] - 4 * y[n - 2] + 3 * y[n - 1]) / (2 * h)
    return a     


def Runge_center(y, h):
    n = len(y)
    p = 2
    r = 2
    
    ksi_h = [(y[i + 1] - y[i - 1]) / (2*h) for i in range(2, n-2)]
    ksi_rh = [(y[i + r] - y[i - r]) / (2*h*r) for i in range(2, n-2)]
    
    return [None if  i >= n - 4 or i < 0
            else (ksi_h[i] + (ksi_h[i] - ksi_rh[i]) / (r**p - 1)) 
            for i in range(-2, n-2)]


def Runge_left_side(y, h):
    n = len(y)
    p = 1

    yh = left_side_diff(y, h)
    y2h = [0 if i < 2 else (y[i] - y[i-2]) / (2*h) for i in range(0, n)]
    
    return [None if  i < 2
            else (yh[i] + (yh[i] - y2h[i]) / (2**p - 1)) 
            for i in range(0, n)]


def aline(x, y):
    return [None if x[i] == 0 else etaksi()*etay(y[i])*ksix(x[i]) for i in range(len(x))]


def print_res_line(text, res):
    print("{:<20}".format(text), end = "")
    for i in res:
        if (i != None):
            print("{: <15.4f}".format(i), end = "")
        else:
            print("{: <15}".format("None"), end = "")
    print()

    
x_start = 0
x_h = 1
x_amount = 11
#x, y = get_table(x_start, x_h, x_amount)

x = [1, 2, 3, 4, 5, 6]
y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

a = [None, 0.317, 0.202, 0.138, 0.99, 0.079]
b = [None, 0.263, 0.117, 0.121, 0.089, None]
c = [None, None, 0.144, 0.106, 0.089, 0.070]
d = [0.408, 0.247, 0.165, 0.118, 0.089, None]
f = [None, -0.120, -0.062, -0.038, -0.020, None]


print_res_line("x:", x)
print_res_line("y:", y)
print_res_line("Left side:", a)
print_res_line("Center differences:", b)
print_res_line("Runge left side:", c)
print_res_line("Aligning:", d)
print_res_line("Second differences:", f)