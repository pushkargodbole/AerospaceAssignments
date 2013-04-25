# AE 617 : Numerical Methods for Conservation Laws
# Assignment 2
# Name : Pushkar Godbole
# Roll no. : 09D01005

import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from math import sqrt
print "***Gas equations***"
Q = raw_input("Select Q (1/2) : ")
print "a) Without entropy fix"
print "b) With entropy fix"
part = raw_input("Select part (a/b) : ")
N = int(raw_input("Np = "))
CFL = 0.9
print "CFL = ", CFL

x1 = -5.0
x2 = 5.0
t1 = 0.0
t2 = 2.01
	
c0 = 6.0

x = np.linspace(x1, x2, N)
dx = x[1] - x[0]
print "dx =", round(dx, 4)
dt = CFL*dx/c0
print "dt =", round(dt, 4)
t = np.arange(t1, t2, dt)
Nt = len(t)


gamma = 1.4
if Q=='1':
    rho0 = np.where((x < 0.), np.ones(N), np.ones(N)*0.125)
    u0 = np.zeros(N)
    p0 = np.where((x < 0.), np.ones(N), np.ones(N)*0.1)
elif Q=='2':
    rho0 = np.where((x < 0.), np.ones(N)*3.857, np.ones(N))
    u0 = np.where((x < 0.), np.ones(N)*0.92, np.ones(N)*3.55)
    p0 = np.where((x < 0.), np.ones(N)*10.33, np.ones(N))
rho = np.copy(rho0)
u = np.copy(u0)
p = np.copy(p0)
rhou = rho*u
E = 1./2.*rho*u**2 + p/(gamma-1)
H = (E+p)/rho
v = np.array([ np.array([ rho[i], rhou[i], E[i] ]) for i in range(N) ])

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('x')
plot1, = ax.plot(x[1:N-1], rho[1:N-1], label="density")
plot2, = ax.plot(x[1:N-1], u[1:N-1], label="velocity")
plot3, = ax.plot(x[1:N-1], p[1:N-1], label="pressure")
ax.legend()

u_avg = np.array([ 0. for i in range(N-1) ])
H_avg = np.array([ 0. for i in range(N-1) ])
rho_avg = np.array([ 0. for i in range(N-1) ])
F = [ 0. for i in range(N) ]
e_vals = [ 0. for i in range(N-1) ] #Eigen values at intervals
e_vals_p = [ 0. for i in range(N) ] #Eigen values at points
e_vecs = [ 0. for i in range(N-1) ] #Eigen vectors at intervals as column vectors
eig_vecs = [ 0. for i in range(N-1) ] #Eigen vectors at intervals as row vectors (Transpose of eig_vecs)
for ti in t:
    #Averaging
    for i in range(N-1):
        u_avg[i] = (sqrt(rho[i])*u[i]+sqrt(rho[i+1])*u[i+1])/(sqrt(rho[i])+sqrt(rho[i+1]))
        H_avg[i] = (sqrt(rho[i])*H[i]+sqrt(rho[i+1])*H[i+1])/(sqrt(rho[i])+sqrt(rho[i+1]))
        rho_avg[i] = sqrt(rho[i]*rho[i+1])
    E_avg = 1./gamma*(rho_avg*H_avg+(gamma-1)/2*rho_avg*u_avg**2)
    p_avg=(rho_avg*H_avg)-E_avg
    #Finding eigen values at points and basic flux function
    for i in range(N):
        F[i] = np.array([ rhou[i], rho[i]*u[i]**2+p[i], u[i]*(E[i]+p[i]) ])
        c = sqrt(gamma*p[i]/rho[i])
        e_vals_p[i] = np.array([ u[i], u[i]+c, u[i]-c ])
    #Finding a values in intervals
    for i in range(N-1):
        c_avg = sqrt(gamma*p_avg[i]/rho_avg[i])
        e_vals[i] = np.array([ u_avg[i], u_avg[i]+c_avg, u_avg[i]-c_avg ])
        e_vecs[i] = np.array([[ 1,                 1,                       1                         ],
                              [ u_avg[i],          e_vals[i][1],            e_vals[i][2]              ],
                              [ 1./2.*u_avg[i]**2, H_avg[i]+u_avg[i]*c_avg, H_avg[i] - u_avg[i]*c_avg ]])
        eig_vecs[i] = e_vecs[i].transpose()
    dv = v[1:,:] - v[:-1,:]
    a = [ np.linalg.inv(e_vecs[i]).dot(dv[i]) for i in range(N-1) ]
    #Updating flux : F
    for i in range(N-1):
        for j in range(len(e_vals[i])):
            
            if e_vals_p[i][j] < 0. and e_vals_p[i+1][j] > 0. and part == 'b': #Entropy fix
                e_val = e_vals_p[i][j]*(e_vals_p[i+1][j] - e_vals[i][j])/(e_vals_p[i+1][j] - e_vals_p[i][j])
            
            elif e_vals[i][j] > 0.:
                e_val = 0.
            else:
                e_val = e_vals[i][j]   
            F[i] = F[i] + e_val*a[i][j]*eig_vecs[i][j]
    #Updating v
    for i in range(1, N):
        v[i] = v[i] - dt/dx*(F[i] - F[i-1])
    #Updating rho, u and p        
    for i in range(N):
        rho[i] = v[i][0]
        rhou[i] = v[i][1]
        E[i] = v[i][2]
    u = rhou/rho
    p = (gamma-1)*(E-1./2.*rho*u**2)
    H = (E+p)/rho     
    plot1.set_ydata(rho[1:N-1])
    plot2.set_ydata(u[1:N-1])
    plot3.set_ydata(p[1:N-1])
    ax.set_title('t = '+str(round(ti, 2)))
    fig.canvas.draw()
       
plt.ioff()
plt.show()
