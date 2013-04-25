import numpy as np
import matplotlib.pyplot as plt

print "***Trafic problem***"
part = raw_input("Select part (a/b/c) : ")

if part == 'a' :
	x1 = -30.0
	x2 = 30.0
	t1 = 0.0
	t2 = 25.0
	
elif part == 'b' :
	x1 = -40.0
	x2 = 10.0
	t1 = 0.0
	t2 = 36.0
	
elif part == 'c' :
	x1 = -30.0
	x2 = 20.0
	t1 = 0.0
	t2 = 18.0
	
else :
	assert False, "Incorrect choice.. (Choose one of a/b/c)"
	
N = int(raw_input("Np = "))
u_max = 1.0
print "u_max = ", u_max
CFL = 0.8
print "CFL = ", CFL

x = np.linspace(x1, x2, N)
dx = x[1] - x[0]
print "dx =", round(dx, 3)
Nt = int((t2-t1)/CFL/dx)
t = np.linspace(t1, t2, Nt)
dt = t[1] - t[0]
print "dt =", round(dt, 3)

if part == 'a' :
	rho0 = 0.25 + 0.75*np.exp(-0.25*(x**2.))
elif part == 'b' :
	rho0 = np.where((x < 0.), 0.25*np.ones(N), np.ones(N))
elif part == 'c' :
	rho0 = np.where((x < 0.), np.ones(N), np.zeros(N))

rho = np.copy(rho0)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('x')
ax.set_ylabel('rho')
plot, = ax.plot(x, rho)
for ti in t:
	f = rho*u_max*(1.-rho)
	phi = np.array([(f[i+1]-f[i]) for i in range(N-1)])
	sign = np.array([(1-rho[i+1]-rho[i]) for i in range(N-1)])
	
	for i in range(N-1):
		if sign[i] >= 0.:
			rho[i+1] = rho[i+1] - dt/dx*phi[i]
		else:
			rho[i] = rho[i] - dt/dx*phi[i]
			
	plot.set_ydata(rho)
	ax.set_title('t = '+str(round(ti, 2)))
	fig.canvas.draw()

plt.ioff()
plt.show()
