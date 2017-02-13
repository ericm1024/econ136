Economics 136
Purpose: Using portfoliovariance.py for data downloads from Yahoo finance.
Data downloaded is exactly like the data we use in HW1.
Credits:
Professor Evans did not write these programs.
The core library program ystockquote.py, which is Open GNU, was written by 
Corey Goldberg. Thanks to him.
The other two programs, YFinanceDaya.py and portfoliovariance.py, were 
written by Mudder Aaron Rosen in 2015. Thanks to him also.
End credits
These programs require SciPy.
These programs should all reside in the same directory.
portfoliovariance is the executable. Open that in a shell to run it.
It will call the other two programs. You may want to look at them.
They have good examples of how to write this kind of code.
Operation:
It will ask for a stock symbol like SPY, plus a beginning date and an 
ending date. Output, a .csv file, will be saved to a file of the same 
name. Therefore if you reload the scraper at a later date to get data 
for the same stock, you will overwrite the original, so  change its 
name (or rewrite the code).  
The program is designed to download the data that we use for HW1 (
just date, volume, and adjusted close).  It is easy to program 
downloads of other fields.
portfoliovariance can do much more than scrub data.

Prof Evans, January 29, 2017