

import numpy as np

def Sgen(m,n):
    #define parameters
    T=0.5
    S0=52
    V0=0.3
    delta_t=T/m
    S=np.zeros(shape=(m+1,n))
    V=np.zeros(shape=(m+1,n))
    S[0,:]=S0
    V[0,:]=V0
    for i in range (0,m):
        dB1=np.sqrt(delta_t)*np.random.randn(n)
        dB2=np.sqrt(delta_t)*np.random.randn(n)
        S[i+1,:]=S[i,:]*(1+0.02*delta_t+V[i,:]*dB1)
        V[i+1,:]=V[i,:]+(0.25-V[i,:])*delta_t+0.2*V[i,:]*(dB1+dB2)
    return S[m,:]
    
result=Sgen(40,10000)
max_sgen=np.maximum(abs(result-50)-5, 0)
answer= np.mean(max_sgen)
print("Expected value of the maximum of abs(S(T)-50)-5,0):",answer) 
