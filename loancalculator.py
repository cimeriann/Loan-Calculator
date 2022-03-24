from tkinter import *
class LoanCalculator:
    def __init__(self):
        # create a window
        window = Tk()
        # add a title
        window.title('Loan Calculator Widget') 
        # defining and placing labels in the window
        Label(window, text='Annual Interest Rate').grid(row=1,column=1,sticky=W)
        Label(window, text='Number of years').grid(row=2, column=1,sticky=W)
        Label(window, text='Loan Amount').grid(row=3,column=1,sticky=W)
        Label(window, text='Monthly Payment').grid(row=4, column=1,sticky=W)
        Label(window, text='Total Payment').grid(row=5,column=1,sticky=W)
        # create variables that hold the values that will be entered into the entry boxes
        self.annualInterestRateVar = StringVar()
        self.numberOfYearsVar = StringVar()
        self.loanAmountVar = StringVar()
        self.monthlyPaymentVar = StringVar()
        self.totalPaymentVar = StringVar()
        # labels that display the monthly and total payment
        labelMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar).grid(row=4, column=1,sticky=E)
        labelTotalPayment = Label(window, text=self.totalPaymentVar).grid(row=5,column=1,sticky=E)
        
        # defining and placing entry boxes in the parent window
        Entry(window,textvariable=self.annualInterestRateVar,justify=RIGHT).grid(row=1,column=2)
        Entry(window,textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=2, column=2)
        Entry(window,textvariable=self.loanAmountVar).grid(row=3, column=2)

        # create a button that computes and returns the payment to be made
        Button(window,text='Compute Payment',command=self.ComputePayment).grid(row=6, column=3, sticky=E)
        
        #run the event loop
        window.mainloop()
    
        # create a function that computes and returns  the payment to be made
    def ComputePayment(self):
        monthlyPayment = float(self.getmonthlyPayment(float(self.loanAmountVar.get()),
                        float(self.annualInterestRateVar.get())/1200,
                        int(self.numberOfYearsVar.get())))
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getmonthlyPayment(self,
            loanAmount,monthlyInterestRate,numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 
                    1 / (1+monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment


LoanCalculator()
        
        