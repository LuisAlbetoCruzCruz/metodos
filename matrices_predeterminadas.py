"""padimos filas y comumnas de las matrizes 1 y 2"""
import random 
filas1=int(input("introduce el numero de filas de la matriz 1:"))
colum1= int(input("introduce el numero de columnas de la matriz 1:"))
colum2=int(input("introduce l numero de columnas de la matriz 2:"))

"""creamos la matriz 1"""
A=[]
for i in range(filas1):
	A.append([0]*colum1)

for i in range(filas1):
	print(A[i])

"""creamos la matriz 2"""
B=[]
for i in range(colum1):
	B.append([0]*colum2)

for i in range(colum1):
	print(B[i])

"""cambiamos los valores de la matriz 1"""
for i in range(filas1):
	for j in range(colum1):
		A[i][j]=(random.randrange(100))
"""
introduce el componente (0,0):
introduce el componente (0,1):
introduce el componente (0,2):
introduce el componente (1,0):
introduce el componente (1,1):
introduce el componente (1,2):"""
for i in range(filas1):
	print(A[i])

"""cambiamos los valores de la matriz 2"""
for i in range(colum1):
	for j in range(colum2):
		B[i][j]=(random.randrange(100))
"""
introduce el componente (0,0):
introduce el componente (0,1):
introduce el componente (1,0):
introduce el componente (1,1):
introduce el componente (2,0):
introduce el componente (2,1):"""
for i in range(colum1):
	print(B[i])

"""creamos la matriz de resultado"""
C=[]
for i in range(filas1):
	C.append([0]*colum2)

for i in range(filas1):
	print(C[i])

"""multiplicamos las matrices 1 y 2"""
for i in range(filas1):
	for j in range(colum2):
		#for k in range(colum1):
			C[i][j]+= A[i][j] * B[j][i]

"""visualisamos la matriz final """
for i in range(filas1):
	R=[]
	for j in range(colum2):
		R.append(C[i][j])
	print(R)
