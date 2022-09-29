import numpy as np
import matplotlib.pyplot as plt

#------------------------------------

r1, dr1, sigma_r1 = np.loadtxt("goodproject.txt", usecols=[0,2,4], unpack=True)
r2, dr2, sigma_r2 = np.loadtxt("goodproject.txt", usecols=[1,3,5], unpack=True)


plt.subplot(2,1,1)
plt.errorbar(r1, dr1, yerr=sigma_r1, fmt="o", c="black")
plt.text(0.27,0.0014, "offset=0.002")
plt.axhline(0.002,c='k',ls=':')
plt.xlabel(r'$r_{1}$')
plt.ylabel(r'$r_{1,best fit}$ - $r_{1,simulation}$')

plt.subplot(2,1,2)
plt.errorbar(r2, dr2, yerr=sigma_r2, fmt="o", c="black")
plt.text(0.0242,0.00003, "offset=0.0002")
plt.axhline(0.0002,c='k',ls=':')
plt.xlabel(r'$r_{2}$')
plt.ylabel(r'$r_{2,best fit}$ - $r_{2,simulation}$')
plt.tight_layout()
plt.savefig("final final boy.png")


plt.show()
