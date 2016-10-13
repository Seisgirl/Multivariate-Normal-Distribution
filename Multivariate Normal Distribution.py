import numpy as np
import math
from scipy.stats import chi2
import matplotlib.pyplot as plt
#PART_ONE
x1 = np.linspace(-10.0, 10.0, 5000.0)
y1 = np.linspace(-10.0, 10.0, 5000.0)
X, Y = np.meshgrid(x1, y1) #seting up a symmertrical meshgrid
r=math.sqrt(2/27)#(math.exp(-0.5/(1-(r**2))*((X**2)/9-(2*r)*X*Y/3*math.sqrt(6)+(Y**2)/6))
N = (6*X**2 + 9*Y**2 + 4*X*Y)#expression for pdf
t=0.5/np.pi*1/math.sqrt(1-r**2)*1/(3*(6**0.5))
plt.figure()
plot = plt.contour(X, Y,t*np.exp(-N/100))
plt.colorbar()
plt.title('Contour Map of Probability Distribution Function of x and y')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#PART_TWO
mean = [0, 0] #given means of the two vbls are 0
covMat = [[9, -2], [-2, 6]] #covariance matrix
x, y = np.random.multivariate_normal(mean, covMat, 50000).T #Part(b)generating 500 pairs of random normally distributed variables
Normal_Multivariate, xt, yt = np.histogram2d(x, y, bins=100, normed=True) #Part (c) plotting a heatmap (2d histogram) with number of bins for both dimentions = 100
extent = [xt[0], xt[-1], yt[0], yt[-1]] #setting the bin edges along each direction
plt.imshow(Normal_Multivariate, extent=extent, cmap='spectral') #printing the plot
plt.title("Heatmap/Histogram of Normal Bivariate Distribution")
plt.ylabel("y")
plt.xlabel("x")
plt.colorbar() #adding colorbar to chart values corresponding to colors
plt.show()
#PART_THREE
z = (6*x**2 + 9*y**2 + 4*x*y)/50 #introducing z
t2=np.linspace(0,15,1000)
print "Mean of z is:",np.mean(z)
print "Standard Deviation of z is:",np.std(z)
plt.clf() #clearing the plot, resettin axes scales
plt.hist(z, 100, normed=True, facecolor='cyan', label='z')  # Plotting the histogram. Number of bins = 100
plt.plot(t2,chi2.pdf(t2,2),'r',label='chi2')
plt.title("Histogram for Probability Density of z")
plt.ylabel("Probability Density")
plt.xlabel("z")
plt.legend()
plt.show()
