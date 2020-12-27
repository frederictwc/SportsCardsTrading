import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import datetime as dt


data = np.genfromtxt("data/A_Davis_PSA_10.txt",dtype=(str,str),delimiter=" ")
x = data[:,0]
x = [dt.datetime.strptime(d,"%Y-%m-%d").date() for d in x]
y = [float(element.replace(",","")) for element in data[:,1]]

#plot
plt.title("Price vs date")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=100))
plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()