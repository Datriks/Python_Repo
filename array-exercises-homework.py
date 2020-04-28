# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 08:06:32 2020

@author: Juvette
"""
#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

#calculate Profit as a diference between revenue and expenses
profit = list([])

for i in range(0, len(revenue)):
    profit.append(revenue[i]-expenses[i])
print(profit)

#%%
#Calculate Tax As 30% Of Profit And Round To 2 Decimal Points
tax = [round(i*0.30,2) for i in profit]
print(tax)
#%%
#Calculate profit ater tax
profit_after_tax = list([])

for i in range(0, len(profit)):
    profit_after_tax.append(profit[i]-tax[i])

profit_after_tax = [round((i),2) for i in profit_after_tax]
print(profit_after_tax)

#%%
#Calculate The Profit Margin As Profit After Tax Over Revenue
#Round To 2 Decimal Points, Then Multiply By 100 To Get %

profit_margin = list([])

for i in range (0, len(profit)):
    profit_margin.append(profit_after_tax[i] / revenue[i])
#round the profit_margin
profit_margin = [round((i*100),2) for i in profit_margin]
print(profit_margin)

#%%
#Calculate The Mean Profit After Tax For The 12 Months
mean_pat = sum(profit_after_tax) / len(profit_after_tax)
print(mean_pat)

#%%
#Find The Months With Above-Mean Profit After Tax
good_months = list([])

for i in range(0, len(profit)):
    good_months.append(profit_after_tax[i] > mean_pat)

print(good_months)

#%%
#Bad Months Are The Opposite Of Good Months!
bad_months = list([])

for i in range(0, len(profit)):
    bad_months.append(not(good_months[i]))
    
print(bad_months)

#%%
#The Best Month Is Where Profit After Tax Was Equal To The Maximum of Profit after tax
best_month = list([])

for i in range(0, len(profit)):
    best_month.append(profit_after_tax[i] == max(profit_after_tax))

print(best_month)

#%%
#The Worst Month Is Where Profit After Tax Was Equal To The Minimum Profit after Tax
worst_month = list([])

for i in range(0, len(profit)):
    worst_month.append(profit_after_tax[i] == min(profit_after_tax))
    
print(worst_month)

#%%
#Convert All Calculations To Units Of One Thousand Dollars
revenue_1000 = [round(i/1000,2) for i in revenue]
expenses_1000 = [round(i/1000,2) for i in expenses]
profit_1000 = [round(i/1000,2) for i in profit]
profit_after_tax_1000 = [round(i/1000,2) for i in profit_after_tax]

#%%
revenue_1000 = [int(i) for i in revenue_1000]
expenses_1000 = [int(i) for i in expenses_1000]
profit_1000 = [int(i) for i in profit_1000]
profit_after_tax_1000 = [int(i) for i in profit_after_tax_1000]
                         
print(revenue_1000)
print(expenses_1000)
print(profit_1000)
print(profit_after_tax_1000)













