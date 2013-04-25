from math import sin, cos, pi, sqrt, log, atan
from numpy import array, zeros, linalg
from pylab import *
line_count = 0
X_u = []
X_l = []
Y_u = []
Y_l = []
x_u = []
x_l = []
y_u = []
y_l = []
phi_u = []
phi_l = []
A_u = []
A_l = []
B_u = []
B_l = []
C_u = []
C_l = []
D_u = []
D_l = []
E_u = []
E_l = []
I_u = zeros((97,97))
I_l = zeros((97,97))
J_u = zeros((97,97))
J_l = zeros((97,97))
V_u = []
V_l = []
Cp_u = []
Cp_l = []
b_u = zeros((97))
b_l = zeros((97))
sigma_u = 0
sigma_l = 0
S_u = []
S_l = []
print "This program will plot the Cp distribution over the upper and lower surface of the NACA0012 aerofoil for alpha = 0. This program makes use of panel method to generate the results."
print "Plotting..."
f = open("naca0012.dat", "r")
while 1:
	line=f.readline()
	if not line: break
	line_count = line_count + 1
	field = line.split()
	if(line_count>3):	
		if(line_count<101):
			X_u.append(float(field[0]))
			Y_u.append(float(field[1]))
		elif(line_count>101):
			X_l.append(float(field[0]))
			Y_l.append(float(field[1]))
X_u.append(X_u[0])
Y_u.append(Y_u[0])
X_l.append(X_u[0])
Y_l.append(Y_u[0])
for k in range(0,97):
	x_u.append((X_u[k]+X_u[k+1])/2)
	y_u.append((Y_u[k]+Y_u[k+1])/2)
	x_l.append((X_l[k]+X_l[k+1])/2)
	y_l.append((Y_l[k]+Y_l[k+1])/2)
	if(X_u[k+1]==X_u[k]):
		if(Y_u[k+1]>Y_u[k]):
			phi_u.append(pi/2)
		else:
			phi_u.append(-pi/2)
	else:
		phi_u.append(atan((Y_u[k+1]-Y_u[k])/(X_u[k+1]-X_u[k])))
	if(X_l[k+1]==X_l[k]):
		if(Y_l[k+1]>Y_l[k]):
			phi_l.append(pi/2)
		else:
			phi_l.append(-pi/2)
	else:
		phi_l.append(atan((Y_l[k+1]-Y_l[k])/(X_l[k+1]-X_l[k])))
x_u.append(x_u[0])
y_u.append(y_u[0])
x_l.append(x_l[0])
y_l.append(y_l[0])
for k in range(0,97):
	S_u.append(sqrt(pow((X_u[k+1]-X_u[k]),2)+pow((Y_u[k+1]-Y_u[k]),2)))
	S_l.append(sqrt(pow((X_l[k+1]-X_l[k]),2)+pow((Y_l[k+1]-Y_l[k]),2)))
for i in range(0,97):
	A_u.append([])
	B_u.append([])
	C_u.append([])
	D_u.append([])
	E_u.append([])
	A_l.append([])
	B_l.append([])
	C_l.append([])
	D_l.append([])
	E_l.append([])
	for j in range(0,97):
		if(i==j):
			A_u[i].append(0)
			B_u[i].append(0)
			C_u[i].append(0)
			D_u[i].append(0)
			E_u[i].append(0)
			I_u[i,j] = pi
			A_l[i].append(0)
			B_l[i].append(0)
			C_l[i].append(0)
			D_l[i].append(0)
			E_l[i].append(0)
			I_l[i,j] = -pi
		else:
			A_u[i].append(-(x_u[i]-X_u[j])*cos(phi_u[j])-(y_u[i]-Y_u[j])*sin(phi_u[j]))
			B_u[i].append(pow((x_u[i]-X_u[j]),2) + pow((y_u[i]-Y_u[j]),2))
			C_u[i].append(sin(phi_u[i]-phi_u[j]))
			D_u[i].append((y_u[i]-Y_u[j])*cos(phi_u[i]) - (x_u[i]-X_u[j])*sin(phi_u[i]))
			E_u[i].append(sqrt(B_u[i][j]-pow(A_u[i][j],2)))
			A_l[i].append(-(x_l[i]-X_l[j])*cos(phi_l[j])-(y_l[i]-Y_l[j])*sin(phi_l[j]))
			B_l[i].append(pow((x_l[i]-X_l[j]),2) + pow((y_l[i]-Y_l[j]),2))
			C_l[i].append(sin(phi_l[i]-phi_l[j]))
			D_l[i].append((y_l[i]-Y_l[j])*cos(phi_l[i]) - (x_l[i]-X_l[j])*sin(phi_l[i]))
			E_l[i].append(sqrt(B_l[i][j]-pow(A_l[i][j],2)))
			I_u[i,j] = C_u[i][j]/2*log((pow(S_u[j],2)+2*A_u[i][j]*S_u[j]+B_u[i][j])/B_u[i][j])+(D_u[i][j]-A_u[i][j]*C_u[i][j])/E_u[i][j]*(atan((S_u[j]+A_u[i][j])/E_u[i][j])-atan(A_u[i][j]/E_u[i][j]))
			I_l[i,j] = C_l[i][j]/2*log((pow(S_l[j],2)+2*A_l[i][j]*S_l[j]+B_l[i][j])/B_l[i][j])+(D_l[i][j]-A_l[i][j]*C_l[i][j])/E_l[i][j]*(atan((S_l[j]+A_l[i][j])/E_l[i][j])-atan(A_l[i][j]/E_l[i][j]))
for k in range(0,97):
	b_u[k] = sin(phi_u[k])
	b_l[k] = sin(phi_l[k])
lambda1_u = linalg.solve(I_u,b_u)
lambda1_l = linalg.solve(I_l,b_l)
for i in range(0,97):
	for j in range(0,97):
		if(i==j):
			J_u[i,j] = 0
			J_l[i,j] = 0
		else:
			J_u[i,j] = (D_u[i][j]-A_u[i][j]*C_u[i][j])/2/E_u[i][j]*log((pow(S_u[j],2)+2*A_u[i][j]*S_u[j]+B_u[i][j])/B_u[i][j])-C_u[i][j]*(atan((S_u[j]+A_u[i][j])/E_u[i][j])-atan(A_u[i][j]/E_u[i][j]))
			J_l[i,j] = (D_l[i][j]-A_l[i][j]*C_l[i][j])/2/E_l[i][j]*log((pow(S_l[j],2)+2*A_l[i][j]*S_l[j]+B_l[i][j])/B_l[i][j])-C_l[i][j]*(atan((S_l[j]+A_l[i][j])/E_l[i][j])-atan(A_l[i][j]/E_l[i][j]))
for i in range(0,97):
	for j in range(0,97):
		sigma_u = sigma_u + J_u[i][j]*lambda1_u[j]
		sigma_l = sigma_l + J_l[i][j]*lambda1_l[j]
	V_u.append(cos(phi_u[i])+sigma_u)
	Cp_u.append(1-pow(V_u[i],2))
	sigma_u = 0
	V_l.append(cos(phi_l[i])-sigma_l)
	Cp_l.append(1-pow(V_l[i],2))
	sigma_l = 0
subplot(221)
plot(X_u,Y_u,'g')
plot(X_l,Y_l,'g')
xlabel('Aerofoil : NACA 0012')
subplot(223)
plot(Cp_l,'b.')
xlabel('upper surface')
ylabel('Cp')
subplot(224)
plot(Cp_u,'r.')
xlabel('lower surface')
ylabel('Cp')
show()
print "Done!"
