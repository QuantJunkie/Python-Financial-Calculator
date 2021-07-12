#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:12:37 2021

@author: maven
"""

from retirement_calculator import RetirementCalculator
from aprtoear_converter import AprtoEarConverter
from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Annual Percentage Yield')
        self.lbl2=Label(win, text='Number of Compounding Per Year')
        self.lbl3=Label(win, text='Retirement Target')
        self.lbl4=Label(win, text='Compounding Periods In Months')
        self.lbl5=Label(win, text='Annual Interest Rate')
        self.lbl6=Label(win, text='...')
        self.lbl7=Label(win, text='....')
        self.lbl8=Label(win, text='Convert APY to EAR')
        self.lbl9=Label(win, text='Retirement Target')

        self.t1=Entry()
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry()
        self.t6=Entry()
        self.t7=Entry()
        self.t8=Entry()
        self.t9=Entry()
        
        self.lbl8.place(x=250, y=0)
        self.lbl1.place(x=90, y=50)
        self.t1.place(x=310, y=50)
        self.lbl2.place(x=90, y=100)
        self.t2.place(x=310, y=100)
        self.lbl9.place(x=250, y=250)
        self.lbl3.place(x=90, y=300)
        self.t3.place(x=310, y=300)
        self.lbl4.place(x=90, y=350)
        self.t4.place(x=310, y=350)
        self.lbl5.place(x=90, y=400)
        self.t5.place(x=310, y=400)

        self.btn1 = Button(win, text='Calculate')
        self.b1=Button(win, text='Calculate', command=self.calculateEAR)
        self.b1.place(x=90, y=150)
        
        self.lbl6.place(x=90, y=200)

        self.btn2 = Button(win, text='Calculate')
        self.b2=Button(win, text='Calculate', command=self.calculate)
        self.b2.place(x=90, y=450)

        self.lbl7.place(x=90, y=500)

    def calculateEAR(self):
        aprr=float(self.t1.get())
        no_compoundingg=int(self.t2.get())
        interestConverter = AprtoEarConverter(aprr, no_compoundingg)
        result1 = float(interestConverter.calculate_ear())
        self.lbl6['text'] = "Your effective annual rate is " + str(round(result1,4))

    def calculate(self):
        retirement_target=int(self.t3.get())
        period=int(self.t4.get())
        interest=float(self.t5.get())
        retirementCalculator = RetirementCalculator(retirement_target, period, interest)
        result2 = retirementCalculator.calculate_monthly_payment()
        self.lbl7['text'] = "The monthly contribution needed to hit your retirment target is " + "$"+ str(round(result2,2))

window=Tk()
mywin=MyWindow(window)
window.title('Retirement Calculator')
window.geometry("500x350+10+10")
window.mainloop()

