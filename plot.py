#format
#graph = plot()  #initialise plot class
#graph.adddata([100,50,25,12,6,3,1,0.5],[0,2,3,4,5,6,7,9])  #add a single series as a list folowed by the time series
#graph.adddata([data],[timesereies]) 
#graph.adddata([[1,2,3,5,8,13,21],[15,4,3,2,1,2,3]],[1,2,3,4,5,6,7]) #add two sets of data with a common time series
#graph.adddata([[data1],[data2]],[timesereies]) 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class plot():
    def __init__(self, masses=[],times=[]):
        solveData = pd.DataFrame(data = masses, columns=times)
        self.currentData = solveData.transpose()

    def adddata (self,newData=[], newtimeseries=[]):
        newData = np.array(newData)

        if len(newData.shape) == 1:
            newData = pd.DataFrame(data = [newData], columns=newtimeseries)
        else:
            newData = pd.DataFrame(data = newData, columns=newtimeseries)



        newData = newData.transpose()

        self.currentData = pd.concat([self.currentData, newData], axis=1, sort=False)

        self.show()
    def show(self):

        self.setupFig()
        self.fig = plt.plot(self.currentData)
        plt.show()



    def setupFig(self, title="PK Model", xunits="",yunits=""):
        """establishes a matplotlib figure to hold the graph displaying the results of the PK model

        :param title: Title displayed above graph, defaults to "PK Model"
        :type title: string, optional
        :param xunits: units for time on the axis, defaults to ""
        :type xunits: string, optional
        :param yunits: units for mass of the drug administered, defaults to ""
        :type yunits: string, optional
        ...
        :raises [ErrorType]: [ErrorDescription]
        ...
        :return: matplotlib figure
        :rtype: class 'matplotlib.figure.Figure'
        """
        self.fig = plt.figure()
        self.fig.suptitle(title)
      
                
        ax = self.fig.add_subplot(1,1,1)
        ax.set_xlabel("Time"+self.__unitsFormat(xunits))
        ax.set_ylabel("Volume"+self.__unitsFormat(yunits))

        return self.fig

    def __unitsFormat(self, unitsInput):
        if unitsInput != "":
            unitsOutput = " ("+unitsInput+")"
        else:
            unitsOutput = unitsInput
        return unitsOutput
