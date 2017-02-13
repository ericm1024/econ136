#Aaron Rosen
#HMC ECON136
#Original: January 23,2015
#V1.1.0: May 2015


import ystockquote,datetime,csv,re

def GetData(name=False,update=False):
    """ Pulls down data for quote from startDate to
    endDate and removes unneeded data (as per Prof.
    Evans's video 'Download SPY data').  Data is stored in
    (quote).csv in the same directory as this file"""

    #Input Checkers
    dateChecker=re.compile("([1-2][0-9][0-9][0-9])-([0-1][0-9])-([0-3][0-9])")
    data = False
    while data == False:
        startDate="a"
        endDate="a"

        #Inputs
        if  name:
            quote = name
        else:
            quote = raw_input("Ticker: ")
        while len(startDate)!=10 and dateChecker.search(startDate) == None:
            startDate = raw_input("Start Date (yyyy-mm-dd): ")
        while len(endDate)!=10 and dateChecker.search(endDate) == None:
            endDate = raw_input("End Date (yyyy-mm-dd): ")

        #Establish Connection and download data
        try:
            pricedict = ystockquote.get_historical_prices(quote,startDate,endDate)
            data = True
        except Exception:
            print "Page not found.  Check inputs and connection and try again."
    
    #Obtain list of days and sort from earliest to latest
    dayList=[]
    for day in pricedict:
        dayList.append(day.split('-'))
    sortedDays = sorted(dayList)
    
    #Populate rows of CSV file
    csvData=[['Date','Volume','Adj Close']]
    for n in range(len(sortedDays)):
        sortedDays[n] = sortedDays[n][0]+'-'+sortedDays[n][1]+'-'+sortedDays[n][2]
        csvData.append([sortedDays[n],pricedict[sortedDays[n]]['Volume'],pricedict[sortedDays[n]]['Adj Close']])

    filename = quote + ".csv"
    if update:
        saveQ = raw_input("Type 'Yes' to save as " + filename + " or 'No' to choose your own file name\n Note: Typing Yes will overwrite the previous file!: ")
    else:
        saveQ = raw_input("Type 'Yes' to save as " + filename + " or 'No' to \nchoose your own file name: ")
    if saveQ == 'No' or saveQ == 'no':
        filename = raw_input("Please choose file name (must end in .csv): ")
    with open(filename,'w') as outputfile:
        csvwriter = csv.writer(outputfile,lineterminator='\n')
        for n in range(len(csvData)):
            csvwriter.writerow(csvData[n])
    print "Data written to ", filename
    print

	


