
# Without args
def print_hello():
   print("Hello!")
print_hello()

# With args
def add_numbers(num1, num2):
   print(num1 + num2)
add_numbers(1, 2)


# accept as many arguments as you want 
def print_args(*args):
   for arg in args:
      print(arg)
# Print every argument passed in
print_args(1, 2, 3, 4)


def factorial(n):    
    if n == 1:
        print(n)
        return 1    
    else:
        print (n,'*', end=' ')
        return n * factorial(n-1)

factorial(5)        


# MAG LINUX 230

from mpmath import mp  # pip3 install mpmath

def compare_mp(nb : mp.mpf, ref : mp.mpf, precision : int = 25) -> None:
    nb = mp.nstr(nb, precision)
    nb_len = len(nb)
    ref = mp.nstr(ref, precision)
    ref_len = len(ref)
    cursor = 0
    while cursor < nb_len and cursor < ref_len and nb[cursor] == ref[cursor]:
        cursor += 1
    print(nb, end='')
    if ref_len > nb_len:
        print('-' * (ref_len - nb_len), end='')
    print()
    print('*' * cursor, end='')
    if cursor < ref_len:
        print('#' * (ref_len - cursor), end='')
    if nb_len > ref_len:
        print('+' * (nb_len - ref_len), end='')
    print()

def heron_mp(x : int, n : int) -> mp.mpf:
    xn = mp.mpf('1')
    x = mp.mpf(str(x))
    for i in range(n):
        xn = (xn + x / xn) / 2
    return xn

def pi(i : int) -> mp.mpf:
    if i <= 0:
        return 0
    n = mp.mpf('3')
    r = mp.mpf('1')
    c = mp.mpf('1')
    for j in range(i):
        n = mp.mpf('2') * n
        old_r = c
        r = old_r / mp.mpf('2')
        a = mp.sqrt(mp.mpf('1') - mp.power(r, 2))
        d = mp.mpf('1') - a
        c = mp.sqrt(mp.power(d, 2) + mp.power(r, 2))
        P = n * old_r
        res = P / mp.mpf('2')
    return res

print(pi(20))    