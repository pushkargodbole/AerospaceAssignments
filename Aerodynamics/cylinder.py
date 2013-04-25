from math import sin, cos, pi, sqrt, log, atan
from numpy import array, zeros, linalg
from pylab import *
print "This program will plot the Cp distribution over a cylinder by simulating it as a structure made up of N panels. This program makes use of panel method to generate the results."
temp = raw_input("Choose number of panels : N = ")
print "Plotting..."
N = int(temp)
theta = 2*pi/N
X = []
Y = []
x = []
y = []
phi = []
A = []
B = []
C = []
D = []
E = []
I = zeros((N,N))
J = zeros((N,N))
V = []
Cp = []
b = zeros((N))
sigma = 0
angle = []
for k in range(0,N):
	X.append(-cos(k*theta-theta/2))
	Y.append(sin(k*theta-theta/2))
	phi.append(pi/2-k*theta)
	x.append(-cos(theta/2)*cos(k*theta+theta/2-theta/2))
	y.append(cos(theta/2)*sin(k*theta+theta/2-theta/2))
X.append(-cos(-theta/2))
Y.append(sin(-theta/2))
x.append(-cos(theta/2)*cos(0))
y.append(cos(theta/2)*sin(0))
S = sqrt(pow((X[1]-X[0]),2)+pow((Y[1]-Y[0]),2))
for i in range(0,N):
	A.append([])
	B.append([])
	C.append([])
	D.append([])
	E.append([])
	for j in range(0,N):
		if(i==j):
			A[i].append(0)
			B[i].append(0)
			C[i].append(0)
			D[i].append(0)
			E[i].append(0)
			I[i,j] = pi
		else:
			A[i].append(-(x[i]-X[j])*cos(phi[j])-(y[i]-Y[j])*sin(phi[j]))
			B[i].append(pow((x[i]-X[j]),2) + pow((y[i]-Y[j]),2))
			C[i].append(sin(phi[i]-phi[j]))
			D[i].append((y[i]-Y[j])*cos(phi[i]) - (x[i]-X[j])*sin(phi[i]))
			E[i].append(sqrt(B[i][j]-pow(A[i][j],2)))
			I[i,j] = C[i][j]/2*log((pow(S,2)+2*A[i][j]*S+B[i][j])/B[i][j])+(D[i][j]-A[i][j]*C[i][j])/E[i][j]*(atan((S+A[i][j])/E[i][j])-atan(A[i][j]/E[i][j]))
for k in range(0,N):
	b[k] = sin(phi[k])
lambda1 = linalg.solve(I,b)
for i in range(0,N):
	for j in range(0,N):
		if(i==j):
			J[i,j] = 0
		else:
			J[i,j] = (D[i][j]-A[i][j]*C[i][j])/2/E[i][j]*log((pow(S,2)+2*A[i][j]*S+B[i][j])/B[i][j])-C[i][j]*(atan((S+A[i][j])/E[i][j])-atan(A[i][j]/E[i][j]))
for i in range(0,N):
	for j in range(0,N):
		sigma = sigma + J[i][j]*lambda1[j]
	V.append(cos(phi[i])+sigma)
	Cp.append(1-pow(V[i],2))
	angle.append(pi*i/N)
	sigma = 0
subplot(121)
plot(X,Y)
xlabel("body")
subplot(122)
plot(angle,Cp,'r.')
xlabel("theta")
ylabel("Cp")
print "Done!"
