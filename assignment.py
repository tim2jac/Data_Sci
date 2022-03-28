# Define the variables and assign them from user input

def check_fermat(a, b, c, n):
    print('There are no positive integers a, b, and c such that (a*n)(bn) = (c*n) For any values of n > 2')

a = int(input('Enter a number for a'))
b = int(input('Enter a number for b'))
c = int(input('Enter a number for c'))
n = int(input('Enter a number for n'))

if (a * n) + (b * n) == (c ** n):
    print('Holy smokes, Fermat was wrong!')

else:
    print('No, that does not  work')
    
check_fermat('a', 'b', 'c', 'n')


def check_fermat(a, b, c, n):
    print('There are no positive integers a, b, and c such that (a*n)(bn) = (c*n) For any values of n > 2')

a = int(input('Enter a number for a'))
b = int(input('Enter a number for b'))
c = int(input('Enter a number for c'))
n = int(input('Enter a number for n'))

if (a * n) + (b * n) == (c ** n):
    print('Holy smokes, Fermat was wrong!')

else:
    print('No, that does not  work')
    

check_fermat('a', 'b', 'c', 'n')


