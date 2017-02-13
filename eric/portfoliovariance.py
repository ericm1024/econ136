#Aaron Rosen
#April 27, 2015
#Econ136
#Covariance Matrix Calculator
#v1.1.0

#Documentation:
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.cov.html
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.corrcoef.html


import YFinanceData as scraper
import numpy as np
import math, csv

class Data:
    """Class for data imports"""
    def __init__(self,date,volume,adjclose,dcgr):
        self.date=date
        self.volume=volume
        self.adjclose=adjclose
        self.dcgr=dcgr
        self.range=[date[0],date[-1]]

    def displayPrices(self):
        """Displays date and adjusted close"""
        print ["Date","Adj Close"]
        print np.vstack((self.date,self.adjclose)).T

    def displayVolume(self):
        """Displays date and trading volume"""
        print ["Date","Volume"]
        print np.vstack((self.date,self.volume)).T

    def displayDCGRs(self):
        """Displays date and DCGRs"""
        print ["Date","DCGR"]
        print np.vstack((self.date[1:],self.dcgr)).T
    
    def displayAll(self):
        """Displays date, trading volume, and adjusted close"""
        dcgr=np.hstack(([float('nan')],self.dcgr))
        print ["Date","Volume","Adj Close"]
        print np.vstack((self.date,self.volume,self.adjclose,dcgr)).T

    def displayDateRange(self):
        """Displays Date Range for ticker"""
        print self.range


def CompileMatrix(TickerDict):
    print "Current Tickers in system: ",list(TickerDict.iterkeys())
    CompileList=raw_input("Type the names of the tickers you wish to \n include, "
                          "separated by commas (without spaces).\n if you want to "
                          "compile all tickers in the system, type \"all\": ")
    if CompileList=="all":
        listItems=list(TickerDict.iterkeys())
    else:
        listItems=CompileList.split(',')
    mat=[]
    order=[]
    for item in listItems:
        try:
            mat.append([TickerDict[item].dcgr])
            order.append(item)
        except KeyError:
            print "ERROR: Name ",item," misspelled or not present."
    print "Order is: ",order
    try:
        return [np.vstack(mat),order]
    except ValueError:
        print "ERROR: Array lengths unequal"
    return [np.vstack([1]),order]

def ListCurrentData(Dict):
    if len(Dict):
        print list(Dict.iterkeys())
    else:
        print "Empty."
    
TickerDict={}                       #Dict for storing ticker information

def importData(name=False):
    """Imports a CSV file into the program"""
    if name:
        filename=name
    else:
        filename=raw_input("Enter csv file name: ")
    if filename[-4:]!='.csv':       #check for file extension (assumes .csv)
        filename=filename+'.csv'    #Adds .csv file extension if missing
    tickername=filename[:-4]        #Extract Ticker
    while len(tickername)>5:        #We will use exec.  Make sure to guard against improper entries
        tickername=raw_input("ERROR: Invalid Ticker Name. Enter a new one: ")
    try:
        with open(filename,'rb') as csvfile:    
            reader=csv.reader(csvfile)
            data=[]
            for row in reader:
                data.append([row])
        stacked=np.vstack(data[1:])
        date=stacked[:,0]               #Date
        volume=stacked[:,1]             #Daily Trading Volume
        adjclose=stacked[:,2]           #Adjusted Close
        dcgr=np.array([math.log(float(adjclose[i+1])/float(adjclose[i])) for i in range(len(adjclose)-1)]) #Daily Continuous Growth Rate
        exec(tickername + "=Data(date,volume,adjclose,dcgr)")
        TickerDict[tickername]=(eval(tickername))
    except IOError:
        print "ERROR: File not found."
        download=raw_input("Type \"yes\" to download the data or \"no\" to return to the main loop. ")
        if download=="yes":
            scraper.GetData(tickername)
            print "Data Acquired"
            importData(tickername)

def printOptions():
    print "1) import data"
    print "2) update data"
    print "3) list tickers"
    print "4) view data"
    print "5) compile matrix"
    print "6) view current matrix"
    print "7) calculate covariances and correlations"
    print "8) help"
    print "9) end program"
    return
    

while True:
    printOptions()
    choice=raw_input("Choose an option: ")
    try:
        choice=int(choice)
        check=1/(choice<10)
        check=1/(choice>0)
    except Exception:
        print "Invalid choice"
        continue
    if choice == 1:
        importData()
    elif choice == 2:
        ListCurrentData(TickerDict)
        tick=raw_input("select a ticker: ")
        if tick in TickerDict:
            scraper.GetData(tick,True)
            importData(tick)
        else:
            print "ERROR: Invalid Choice."
    elif choice == 3:
        ListCurrentData(TickerDict)
    elif choice == 4:
        if(len(TickerDict)):
            ListCurrentData(TickerDict)
            tick=raw_input("select a ticker: ")
            if tick in TickerDict:
                print "1) adjusted closes"
                print "2) daily volume"
                print "3) DCGRs"
                print "4) Date Range"
                print "5) all"
                display=raw_input("pick a number: ")
                if display=='1':
                    TickerDict[tick].displayPrices()
                elif display=='2':
                    TickerDict[tick].displayVolume()
                elif display=='3':
                    TickerDict[tick].displayDCGRs()
                elif display=='4':
                    TickerDict[tick].displayDateRange()
                elif display=='5':
                    TickerDict[tick].displayAll()
                else:
                    print "ERROR: Invalid Choice."
            else:
                print "ERROR: Invalid Choice."
        else:
            print "ERROR: No tickers in system."
    elif choice == 5:
        mat,order=CompileMatrix(TickerDict)
    elif choice == 6:
        print order
        print mat
    elif choice == 7:
        cov=np.cov(mat)
        print "Covariance Matrix:\n",order,'\n',cov
        cor=np.corrcoef(mat)
        print "Correlation Coefficient Matrix:\n",order,'\n',cor
    elif choice == 8:
        print
        print ("1) import data \n"
              "Imports data into the program from a specifically formatted CSV \n"
              "Will offer to download and format information from Yahoo Finance \n"
              "if the requested data is not in the current directory.")
        print
        print ("2) update data\n"
              "Accesses Yahoo Finance and overwrites the previous file with the \n"
              "requested start and end dates.")
        print
        print ("3) list tickers \n"
              "Lists the tickers of data that has been imported into the program.")
        print
        print ("4) view data \n"
              "Allows you to view the imported data for a specific ticker.")
        print
        print ("5) compile matrix \n"
              "Constructs a matrix of DCGRs from the given tickers.")
        print
        print ("6) view current matrix \n"
              "Displays the most recently constructed matrix of DCGRs.")
        print
        print ("7) calculate covariances and correlations \n"
              "Returns the covariance and correlation matrices.")
        print
        print ("8) help \n"
              "Provides some documentation")
        print
        print ("9) end program \n"
              "Quits the program.  Data remains in IDLE until the window is closed.")
        print "-----------------------------------"
    else:
        break
