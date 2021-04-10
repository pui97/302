import ttk
import unittest
from Tkinter import *

from tkMessageBox import *

main = Tk()



###########################################################################################
#function

        




def single_calculate(int_income):
    
    
    if int_income< 7099*12:
        int_mpf=0
    elif int_income >=7100*12 and int_income <30000*12:
        int_mpf = int_income*0.05
    elif int_income>30000*12:
        int_mpf = 18000
    
    if int_income < 2040050:
        net_chargeable_income= int(int_income-int_mpf-132000)
        
        Check = net_chargeable_income
       
        if net_chargeable_income > 0:
            if Check <= 49999:               
                tax = int(net_chargeable_income*0.02)
                print "tax is $",tax
                return tax
            elif Check >= 50000 and Check <=99999:
                on9=net_chargeable_income-50000
                tax=int((on9*0.06)+1000)
                print "tax is $",tax
                return tax
            elif Check >= 100000 and Check <=149999:
                on9j=net_chargeable_income-100000
                tax= int((on9j*0.1)+4000)
                print "tax is $",tax
                return tax
            elif Check >= 150000 and Check <=199999:
                on9pui=net_chargeable_income-150000
                tax=int((on9pui*0.14)+9000)
                print "tax is $",tax
                return tax
            elif Check >= 200000:
                puipui=net_chargeable_income-200000
                tax=int((puipui*0.17)+16000)
                print "tax is $",tax
                return tax
           
    else:
        aaronB=int_income-int_mpf
        tax=int(aaronB*0.15)
        print tax
        return tax
    

def married_single_calculate(int_income1,int_income2):
    
    global total_single_tax

    if int_income1< 7099*12:
        int_mpf1=0
    elif int_income1 >=7100*12 and int_income1 <30000*12:
        int_mpf1 = int_income1*0.05
    elif int_income1>30000*12:
        int_mpf1 = 18000

    if int_income2< 7099*12:
        int_mpf2=0
    elif int_income2 >=7100*12 and int_income2 <30000*12:
        int_mpf2 = int_income2*0.05
    elif int_income2>30000*12:
        int_mpf2 = 18000
    
    if int_income1 < 2040050:
        net_chargeable_income1= int(int_income1-int_mpf1-132000)
        
        Check1 = net_chargeable_income1
       
        if net_chargeable_income1 > 0:
            if Check1 <= 49999:               
                tax1 = int(net_chargeable_income1*0.02)
                
               
            elif Check1 >= 50000 and Check1 <=99999:
                on91=net_chargeable_income1-50000
                tax1=int((on91*0.06)+1000)
                
                
            elif Check1 >= 100000 and Check1 <=149999:
                on9j1=net_chargeable_income1-100000
                tax1= int((on9j1*0.1)+4000)
              
                
            elif Check1 >= 150000 and Check1 <=199999:
                on9pui1=net_chargeable_income1-150000
                tax1=int((on9pui1*0.14)+9000)
             
                
            elif Check1 >= 200000:
                puipui1=net_chargeable_income1-200000
                tax1=int((puipui1*0.17)+16000)
               
                
        
        else:
            tax1=int(0)
           
    else:
        aaronB1=int_income1-int_mpf1
        tax1=int(aaronB1*0.15)
    
       
    
        
    if int_income2 < 2040050:
        net_chargeable_income2= int(int_income2-int_mpf2-132000)
        
        Check2 = net_chargeable_income2
       
        if net_chargeable_income2 > 0:
            if Check2 <= 49999:               
                tax2 = int(net_chargeable_income2*0.02)
                
                
            elif Check2 >= 50000 and Check2 <=99999:
                on92=net_chargeable_income2-50000
                tax2=int((on92*0.06)+1000)
                
                
            elif Check2 >= 100000 and Check2 <=149999:
                on9j2=net_chargeable_income2-100000
                tax2= int((on9j2*0.1)+4000)
              
                
            elif Check2 >= 150000 and Check2 <=199999:
                on9pui2=net_chargeable_income2-150000
                tax2=int((on9pui2*0.14)+9000)
             
                
            elif Check2 >= 200000:
                puipui2=net_chargeable_income2-200000
                tax2=int((puipui2*0.17)+16000)
               
                
        
        else:
            tax2=int(0)
           
    else:
        aaronB2=int_income2-int_mpf2
        tax2=int(aaronB2*0.15)
    

    total_single_tax = tax1+tax2
    print "Seprate Assessment is $",total_single_tax
    return total_single_tax
    
    
    

def married_calculate(int_income1,int_income2):
    
    global tax
    
    if int_income1< 7099*12:
        int_mpf1=0
    elif int_income1 >=7100*12 and int_income1 <30000*12:
        int_mpf1 = int_income1*0.05
    elif int_income1>30000*12:
        int_mpf1 = 18000

    if int_income2< 7099*12:
        int_mpf2=0
    elif int_income2 >=7100*12 and int_income2 <30000*12:
        int_mpf2 = int_income2*0.05
    elif int_income2>30000*12:
        int_mpf2 = 18000

        
    total_income = int_income1+int_income2
    total_mpf = int_mpf1+int_mpf2

    
    if total_income < 3180024:
        net_chargeable_income= int(total_income-total_mpf-264000)
        
        Check = net_chargeable_income
       
        if net_chargeable_income > 0:
            if Check <= 49999:               
                tax = int(net_chargeable_income*0.02)
                print "Under Joint Assessment is $",tax
                return tax
               
            elif Check >= 50000 and Check <=99999:
                on9=net_chargeable_income-50000
                tax=int((on9*0.06)+1000)
                print "Under Joint Assessment is $",tax
                return tax
                
            elif Check >= 100000 and Check <=149999:
                on9j=net_chargeable_income-100000
                tax= int((on9j*0.1)+4000)
                print "Under Joint Assessment is $",tax
                return tax
                
            elif Check >= 150000 and Check <=199999:
                on9pui=net_chargeable_income-150000
                tax=int((on9pui*0.14)+9000)
                print "Under Joint Assessment is $",tax
                return tax
               
            elif Check >= 200000:
                puipui=net_chargeable_income-200000
                tax=int((puipui*0.17)+16000)
                print "Under Joint Assessment is $",tax
                return tax
                
        else :
            tax = 0
            print "Under Joint Assessment is $",tax
            return tax
    else:
        aaronB=total_income-total_mpf
        tax=int(aaronB*0.15)
        print "Separate Assessment",tax
        return tax
    
     



def suggestion(total_single_tax,tax):
    if tax > 0 and total_single_tax > 0 :
        
        if tax > total_single_tax:
            print "suggest use seprate Assesment"
            return "suggest use seprate Assesment"
        elif tax < total_single_tax:
            print "suggest use Joint Assessment"
            return "suggest use Joint Assessment"
        else:
            print "using single or joint assessment is the same price"
    else:
        print "no need to pay"

def status(status):
    if int(status) ==1:
        income = int(input("income"))
        single_calculate(income)
        
    elif int(status) ==2:
        income1 = input("user 1 income ")
        income2 = input("user 2 income ")
        married_single_calculate(income1,income2)
        married_calculate(income1,income2)
        suggestion(total_single_tax,tax)
    else:
        print "input error"
        

puipuipuipui = input("single(1)/married(2)")

status(puipuipuipui)
    

