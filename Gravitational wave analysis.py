##a code to that uses Time series anayltical techniques
##on simulated gravitational waves from two LIGO interferomter
##sites that are 3000 Km apart
##(prewhitening and band-pass filters) that remove
##unwanted noises. This isolated the desried signal.
##


import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import signal
from scipy.optimize import curve_fit
from scipy import stats


#loading the data----------------------------

t, A, B = np.loadtxt("w9s88.dat", usecols=[0,1,2], unpack=True)

A = A - np.mean(A) # remove any constant offset

B = B - np.mean(B)

# Time Series Analysis:


#pre whitening----------------------

#remove unwanted periodic peaks in fourier spectrum. by substracting the frequency
#by fiting a sine wave to the time series
# this makes  signal spectrum more uniform.

def func(t,f,p,a,offset):
        return a*np.sin(t*2*np.pi*f+p)+offset

N=10
for i in range (N):
    A = A - np.mean(A) # remove any constant offset
    ftA = fftpack.fft(A)
    freqsA = fftpack.fftfreq(len(t), d=(t[1]-t[0])) # d is sample spacing

    freq_estA = freqsA[np.argmax(np.abs(ftA))] # frequency of highest peak
    amp_estA = np.max(np.abs(ftA))/len(A)*2 # amplitude of the highest peak

    # Estimate phase
    matrixA_A = np.vstack([np.sin(freq_estA*2*np.pi*t),
                         np.cos(freq_estA*2*np.pi*t),
                         np.ones(len(t))]).T

    alphaA = np.dot(matrixA_A.T,matrixA_A)
    betaA = np.dot(matrixA_A.T,A)

    matrixCA = np.linalg.inv(alphaA) # covariance matrix
    afitA = np.dot(matrixCA,betaA) # solution vector
    phase_estA = np.arctan2(afitA[1],afitA[0])

    # Assume offset is zero
    poptA, pcovA = curve_fit(func,t,A,p0=[freq_estA,phase_estA,amp_estA,0.])
    A = A-func(t,*poptA) # subtract fit from data


for i in range (N):
    B = B - np.mean(B) # remove any constant offset
    ftB = fftpack.fft(B)
    freqsB = fftpack.fftfreq(len(t), d=(t[1]-t[0])) # d is sample spacing

    freq_estB = freqsB[np.argmax(np.abs(ftB))] # frequency of highest peak
    amp_estB = np.max(np.abs(ftB))/len(B)*2 # amplitude of the highest peak

    # Estimate phase
    matrixA_B = np.vstack([np.sin(freq_estB*2*np.pi*t),
                         np.cos(freq_estB*2*np.pi*t),
                         np.ones(len(t))]).T

    alphaB = np.dot(matrixA_B.T,matrixA_B)
    betaB = np.dot(matrixA_B.T,B)

    matrixCB = np.linalg.inv(alphaB) # covariance matrix
    afitB = np.dot(matrixCB,betaB) # solution vector
    phase_estB = np.arctan2(afitB[1],afitB[0])


    # Assume offset is zero
    poptB, pcovB = curve_fit(func,t,B,p0=[freq_estB,phase_estB,amp_estB,0.])
    B = B-func(t,*poptB) # subtract fit from data

    
#band pass---------------------------

##to filter the signal by band-passing the Fourier transform with chosen cut-off 
##frequencies that eliminate the noise from the data    

f_cL_A =  130# cutoff frequency 180Hz
filtL_A = np.exp(-(0.5*freqsA/f_cL_A)**2) # Low-pass filter
f_cH_A = 50 #cutoff frequency 50 Hz
filtH_A = (1-(np.exp(-(0.5*freqsA/f_cH_A)**2))) # High-pass filter
filt_A = filtL_A*filtH_A # band-pass filter

ft_filteredA = ftA*filt_A

f_cL_B = 120 # cutoff frequency 200Hz
filtL_B = np.exp(-(0.5*freqsB/f_cL_B)**2) # Low-pass filter
f_cH_B = 50 #cutoff frequency 50 Hz
filtH_B = (1-(np.exp(-(0.5*freqsB/f_cH_B)**2))) # High-pass filter
filt_B = filtL_B*filtH_B # band-pass filter

ft_filteredB = ftB*filt_B

#filtered signal---------------------------------

##Signal A and B cleaned of any noises through prewhitening
##and band passing to show the desired signal of the gravitational wave
##at around 12s

A_filtered = np.real(fftpack.ifft(ft_filteredA))#time domain

B_filtered = np.real(fftpack.ifft(ft_filteredB))#time domain

plt.subplot(2,1,1)
plt.plot(t[500:(len(t)-500)],A_filtered[500:(len(t)-500)],c = "tomato")
plt.xlabel("Time [s]")
plt.ylabel("Signal")
plt.title("Filtered Signal A")


plt.subplot(2,1,2)
plt.plot(t[500:(len(t)-500)],B_filtered[500:(len(t)-500)], c = "cornflowerblue")
plt.xlabel("Time [s]")
plt.ylabel("Signal")
plt.title("Filtered Signal B")


plt.show()


#-----------------------

##to show that they were both the same signal, the data was placed ontop of each other
##there was a slight offset measured between the two Interferometers

plt.plot(t[500:(len(t)-500)],A_filtered[500:(len(t)-500)],c = "tomato", label="A")
plt.plot(t[500:(len(t)-500)],B_filtered[500:(len(t)-500)], c = "cornflowerblue", label="B")
plt.xlim(12.45,12.64)
plt.xlabel("Time [s]")
plt.ylabel("Signal")
plt.title("Filtered Signal ontop ")
plt.legend()

plt.show()

#cross correlation----------

##to find the offset between the signals, the signlas were cross correlated
##this gave the time delay
##there was a time delay of 0.0014 s

##the time delay was due to the waves travelling from one
##interferometer to the other as there is a far distance between them

xcorr = signal.correlate(B_filtered,A_filtered, mode= "same")

tmid = t[len(t)//2] # midpoint time
tmax = t[np.argmax(xcorr)] # time of maximum value in xcorr
tdelay = tmax - tmid
print("Time difference between the detection of graviational wave between the two interferometer:", tdelay )#0.001464840000000578

#-------------------


plt.plot(t,xcorr)
#plt.xlim(12.2,12.68)
plt.xlabel("Time [s]")
plt.ylabel("Cross correlation")
plt.title("xcorr ")

plt.show()

#final graph--------------------

##the final graph are the two signals on top of each other
##with the offset of 0.0014 applied

plt.plot(t[500:(len(t)-500)],A_filtered[500:(len(t)-500)],c = "tomato", label="A")
plt.plot(t[500:(len(t)-500)]-tdelay,B_filtered[500:(len(t)-500)], c = "cornflowerblue", label="B")
plt.xlim(12.45,12.64)
plt.xlabel("Time [s]")
plt.ylabel("Signal")
plt.title("Final signal that was time-shifted")
plt.legend()

plt.show()

#angle of gravitational wave----------------------

##With the offset now known, we can calsulate the angle at which
##the gravitational wave hit the earth can now be calculated.
##
##Gravtational waves travel at the speed of, the distance
##between the interferometers are 3000 km and with the time delay
##we calculated from the cross correlation.


c = 3*(10**8)
d = 3*(10**6)#distance between sites
d2 = tdelay * c
theta = np.arcsin(d2/d)*(180/np.pi)#angle in deg
print()
print("Angle of gravitational wave hitting the two interferometers:")
print("theta:", theta , "\u03B8" )#8.423223796431657
















