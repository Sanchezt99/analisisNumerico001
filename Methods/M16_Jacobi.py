
x0, y0, z0 = 0

i = 1

#falta hacer que se cambie a diagonal dominante automaticamente pero no se como.
f1 = lambda x,y,z: (8-y+6*z)/10
f2 = lambda x,y,z: (-18-3*x+z)/10
f3 = lambda x,y,z: (25-2*x+3*y)/10



# Reading tolerable error
e = float(input('Enter tolerance (1e-n): '))

# Implementation of Jacobi Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x0,y0,z0)
    z1 = f3(x0,y0,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(i, x1,y1,z1))
    e1 = abs(x0-x1)
    e2 = abs(y0-y1)
    e3 = abs(z0-z1)
    
    i += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = e1>e and e2>e and e3>e

print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))