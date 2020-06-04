from tkinter import*

## Notes
# 
class GUI:
        
    def __init__(self, rWin):
        self.rWin = rWin
        self.rWin.title('GUI')
        self.f1 = Frame(self.rWin, bg = 'blue').grid()
        self.var1 = StringVar()
        self.e1 = Entry(self.f1, textvariable=self.var1, width=70, state='readonly').grid(row=0, column=1)
        self.b1 = Button(self.f1, width=20, text='Get Info', command=self.openStocks).grid(row=0, column=0)
        
        self.f2 = Frame(self.f1, bg = 'grey').grid(row=4, columnspan=3)
        self.l1 = Label(self.f2, text='Something').grid(row=2, column=1)
        self.b2 = Button(self.f1, width=20, text='Generate Report', command=self.genReport).grid(row=1, column=0)


        
    def openStocks(self):
        self.filename1 = filedialog.askopenfilename(title = "Please choose a file.")
        self.e1 = Entry(state='normal')
        self.var1.set(self.filename1)
        self.e1 = Entry(state='readonly')
        
        #self.l2 = Label(self.f2, text=
        
    def genReport(self):
        self.CoNames = ['Apple', 'Microsoft', 'Google', 'Netflix', 'Cisco']
        self.CoAbbrev = ['AAPL', 'MSFT', 'GOOG', 'NFLX', 'CSCO']
        self.stockData1 = open(self.filename1)
        self.stockData2 = self.stockData1.readlines()
        self.stockData1.close()

        self.stockData3 = []
        for line in self.stockData2:
            indivLines = line.split(',')
            self.stockData3.append(indivLines)

        self.stockData4 = []
        for line in self.stockData3:
            tempList = []
            for y in line:
                tempList.append(y)
            self.stockData4.append(tempList)

        #print("stockData4:", self.stockData4)

        for x in self.stockData4:
            x[-1] = x[-1][0:3:]
        print(self.stockData4)
##                
##                if type(x[-1][y]) == 
##            print(lastNum)
##            x[-1] = lastNum
##            #print(x)
            
        
        self.StockDict = {}
        self.StockList = [ [], [], [], [], [] ]
        for i in range(len(self.CoNames)):
            name = self.CoNames[i]
            self.StockDict[name] = self.stockData4[i]
    
        #print(self.StockDict)
        
        
        




rWin = Tk()
app = GUI(rWin)
rWin.mainloop()