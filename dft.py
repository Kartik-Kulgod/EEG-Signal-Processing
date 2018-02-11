import cmath,math
import numpy as np 

x_input = [1,2,3,4,5];
Nfft = len(x_input)
N = 2**(math.ceil(math.log(Nfft)/math.log(2)))
x = [0 for i in range(0,N)]
x[0:Nfft] = x_input;
del x_input,Nfft;
print(x)
#x_e = [x[2*i] for i in range(0,Nfft)]
#x_o = [x[2*i+1] for i in range(0,Nfft)]
#Wn = camth.exp(-cmath.sqrt(-1)*cmath.pi*2/N)
X = [0 for i in range(0,N)];


def ditfft2(x,N):
	#print (x)
	#print (N)
	#print (X)
	#print ("\n")
	if(N==1):
		y = []
		y.append(x[0])
		return y;
	else:
		E = [0 for i in range(0,N//2)];
		O = [0 for i in range(0,N//2)];
		x_e = [x[2*i] for i in range(0,N//2)]
		x_o = [x[2*i+1] for i in range(0,N//2)]
		E[0:N//2] = (ditfft2(x_e,N//2))
		O[0:N//2] = (ditfft2(x_o,N//2))
		#print(E)
		#print(O)
		k = 0;
		while (k<N//2):
			X[k] = E[k] + cmath.exp(-2*cmath.pi*cmath.sqrt(-1)*k/N)*O[k]
			X[k+N//2] = E[k] - cmath.exp(-2*cmath.pi*cmath.sqrt(-1)*k/N)*O[k]
			k = k+1
			#print(X[0:N])
		return X[0:N]

ditfft2(x,N)

print(X)

 
