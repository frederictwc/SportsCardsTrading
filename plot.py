import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import datetime as dt


data = np.genfromtxt("data/Zion_PSA_9.txt",dtype=(str,str),delimiter=" ")
x = data[:,0]
x = [dt.datetime.strptime(d,"%Y-%m-%d").date() for d in x]
y = [float(element.replace(",","")) for element in data[:,1]]

data_2 = np.genfromtxt("data/Zion_PSA_10.txt",dtype=(str,str),delimiter=" ")
x_2 = data_2[:,0]
x_2 = [dt.datetime.strptime(d,"%Y-%m-%d").date() for d in x_2]
y_2 = [float(element.replace(",","")) for element in data_2[:,1]]

#plot
plt.title("Price vs date")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=100))
plt.plot(x,y)
plt.plot(x_2,y_2)
plt.legend(['Zion_PSA_9', 'Zion_PSA_10'])
plt.gcf().autofmt_xdate()
plt.show()