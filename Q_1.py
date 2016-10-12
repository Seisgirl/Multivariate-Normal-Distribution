import numpy as np
import math
import matplotlib.pyplot as plt
#PART_ONE
x1 = np.linspace(-100.0, 100.0, 5000.0)
y1 = np.linspace(-100.0, 100.0, 5000.0)
X, Y = np.meshgrid(x1, y1)                                                #seting up a symmertrical meshgrid
N = (6*X**2 + 9*Y**2 + 4*X*Y)/(1000*(2**0.5)*math.pi)                     #expression for pdf
plt.figure()
plot = plt.contourf(X, Y, N)
plt.colorbar()
plt.title('Contour Map of Probability Distribution Function of x and y')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#PART_TWO
mean = [0, 0]                                                             #given means of the two vbls are 0
covMat = [[9, -2], [-2, 6]]                                               #covariance matrix
x, y = np.random.multivariate_normal(mean, covMat, 50000).T               #Part(b)generating 500 pairs of random normally distributed variables
Normal_Multivariate, xt, yt = np.histogram2d(x, y, bins=100, normed=True) #Part (c) plotting a heatmap (2d histogram) with number of bins for both dimentions = 100
extent = [xt[0], xt[-1], yt[0], yt[-1]]                                   #setting the bin edges along each direction
plt.imshow(Normal_Multivariate, extent=extent, cmap='spectral')           #printing the plot
plt.title("Heatmap/Histogram of Normal Bivariate Distribution")
plt.ylabel("y")
plt.xlabel("x")
plt.colorbar()                                                            #adding colorbar to chart values corresponding to colors
plt.show()
#PART_THREE
z = (6*x**2 + 9*y**2 + 4*x*y)/50                                          #introducing z
z_m = sum(z)/(50000)                                                      #mean value of z
z_sd = math.sqrt(sum((z-z_m)**2)/50000)                                   #standard deviation of z
print (z_m)
print (z_sd)
plt.clf()                                                                 #clearing the plot, resettin axes scales
plt.hist(z, 100, normed=True, facecolor='cyan')                           # Plotting the histogram. Number of bins = 100
plt.title("Histogram for Probability Density of z")
plt.ylabel("Probability Density")
plt.xlabel("z")
plt.legend()
plt.show()
