# AE 617 : Numerical Methods for Conservation Laws
# Assignment 2
# Name : Pushkar Godbole
# Roll no. : 09D01005

import numpy as np
import matplotlib.pyplot as plt
from time import sleep
print "***Acoustic equations***"
print "a) Closed ends"
print "b) Open ends"
part = raw_input("Select part (a/b) : ")
N = int(raw_input("Np = "))
CFL = 0.8
print "CFL = ", CFL

K0 = 1./4.
rho0 = 1.0
c0 = np.sqrt(K0/rho0)

x1 = -1.0
x2 = 1.0
t1 = 0.0
t2 = 3.2
	
x = np.linspace(x1, x2, N)
dx = x[1] - x[0]
print "dx =", round(dx, 4)
dt = CFL*dx/c0
print "dt =", round(dt, 4)
t = np.arange(t1, t2, dt)
Nt = len(t)

A = np.array([[ 0.0  , K0  ],
             [ 1.0/rho0, 0.0 ]])
             
e_vals, e_vecs = np.linalg.eig(A)
eig_vecs = e_vecs.transpose() # Contains the eigen vectors as rows

S = np.zeros(N)
for i in range(N):
    if ( -0.3 < x[i] < -0.1 ):
        S[i] = 0.5        
p0 = 0.5*np.exp(-80.0*x**2) + S
u0 = np.zeros(N)

p = np.copy(p0)
u = np.copy(u0)

v = np.array([ np.array([ p[i], u[i] ]) for i in range(N) ])

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('x')
ax.set_ylim(-c0, c0)
plot1, = ax.plot(x[1:N-1], p[1:N-1], label="pressure")
plot2, = ax.plot(x[1:N-1], u[1:N-1], label="velocity")
ax.legend()

done1 = 0
done2 = 0
done3 = 0
for ti in t:
    dv = v[1:,:] - v[:-1,:]
    a = [ np.linalg.inv(e_vecs).dot(dv[i]) for i in range(N-1) ]
    for i in range(1, N-1):
        for j in range(len(e_vals)):
            e_val = e_vals[j]
            if e_val > 0:
                v[i] = v[i] - dt/dx*e_val*a[i-1][j]*eig_vecs[j]
            else:
                v[i] = v[i] - dt/dx*e_val*a[i][j]*eig_vecs[j]
    
    if part == 'a': # For closed ends : Pressure at ends will be constant (here 0)
        v[1][1] = 0
        v[N-2][1] = 0
    #elif part == 'b': # For open ends : Velocity at ends will be 0
        #v[1][0] = 0
        #v[N-2][0] = 0
        
    for i in range(N):
        p[i] = v[i][0]
        u[i] = v[i][1]
          
    plot1.set_ydata(p[1:N-1])
    plot2.set_ydata(u[1:N-1])
    ax.set_title('t = '+str(round(ti, 2)))
    fig.canvas.draw()
    
    if ti >= 1.0 and done1 ==0:
        p1 = np.copy(p)
        u1 = np.copy(u)
        done1 = 1
    if ti >= 2.0 and done2 ==0:
        p2 = np.copy(p)
        u2 = np.copy(u)
        done2 = 1
    if ti >= 3.0 and done3 ==0:
        p3 = np.copy(p)
        u3 = np.copy(u)
        done3 = 1

       
plt.ioff()
plt.close() 
fig2 = plt.figure()

ax0 = fig2.add_subplot(221)
ax0.set_xlabel('x')
ax0.set_title('t = 0.0')
ax0.plot(x[1:N-1], p0[1:N-1], label="pressure")
ax0.plot(x[1:N-1], u0[1:N-1], label="velocity")
ax0.legend()

ax1 = fig2.add_subplot(222)
ax1.set_xlabel('x')
ax1.set_title('t = 1.0')
ax1.plot(x[1:N-1], p1[1:N-1], label="pressure")
ax1.plot(x[1:N-1], u1[1:N-1], label="velocity")
ax1.legend()

ax2 = fig2.add_subplot(223)
ax2.set_xlabel('x')
ax2.set_title('t = 2.0')
ax2.plot(x[1:N-1], p2[1:N-1], label="pressure")
ax2.plot(x[1:N-1], u2[1:N-1], label="velocity")
ax2.legend()

ax3 = fig2.add_subplot(224)
ax3.set_xlabel('x')
ax3.set_title('t = 3.0')
ax3.plot(x[1:N-1], p3[1:N-1], label="pressure")
ax3.plot(x[1:N-1], u3[1:N-1], label="velocity")
ax3.legend()

plt.show()

