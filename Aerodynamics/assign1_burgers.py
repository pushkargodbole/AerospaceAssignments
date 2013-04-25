import numpy as np
import matplotlib.pyplot as plt


print "***Burgers' Equation***"
print "(More accurate results are reached with higher Np, like 5000. Although it will take longer to plot.)"
N = int(raw_input("Np = "))
CFL = 0.8
print "CFL = ", CFL

x1 = -2.0
x2 = 2.0
t1 = 0.0
t2 = 4./3.
	
x = np.linspace(x1, x2, N)
dx = x[1] - x[0]
print "dx =", round(dx, 4)
Nt = int((t2-t1)/CFL/dx)
t = np.linspace(t1, t2, Nt)
dt = t[1] - t[0]
print "dt =", round(dt, 4)

u0 = np.where((abs(x) < 1./3.), np.ones(N), np.zeros(N))

u = np.copy(u0)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('x')
ax.set_ylabel('u')
plot, = ax.plot(x, u)

for ti in t:
	f = u**2./2.
	phi = np.array([(f[i+1]-f[i]) for i in range(N-1)])
	sign = np.array([(u[i+1]+u[i])/2. for i in range(N-1)])
	for i in range(N-1):
		if sign[i] >= 0.:
			u[i+1] = u[i+1] - dt/dx*phi[i]
		else:
			u[i] = u[i] - dt/dx*phi[i]
	if ti > 0.6 and ti < 2./3.:
		u_t1 = np.copy(u)
	if ti > 1.3 and ti < 4./3.:
		u_t2 = np.copy(u)
	plot.set_ydata(u)
	ax.set_title('t = '+str(round(ti, 2)))
	fig.canvas.draw()

plt.ioff()
plt.close()

fig2 = plt.figure()

ax1 = fig2.add_subplot(121)
ax1.set_xlabel('x')
ax1.set_ylabel('u')
ax1.set_title('t = 2/3')
plot1 = ax1.plot(x, u_t1)

ax2 = fig2.add_subplot(122)
ax2.set_xlabel('x')
ax2.set_ylabel('u')
ax2.set_title('t = 4/3')
plot2 = ax2.plot(x, u_t2)

plt.show()
