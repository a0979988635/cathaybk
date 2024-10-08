'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')
import numpy as np


def calculate_investment_metrics(returns, monthly_investment):
    
    returns_decimal = np.array(returns) / 100
    
    monthly_balances = monthly_investment * (1 + returns_decimal)
    
  
    total_gain = np.sum(monthly_balances) - (monthly_investment * len(returns))

   
    avg_return_rate = np.mean(returns)

   
    std_return_rate = np.std(returns)
    
  
    return round(total_gain), round(avg_return_rate), round(std_return_rate)

# test
returns = [-12, 5, 7, 25, 11, 3, -9, -5, -17, -22, -15, 0]
monthly_investment = 1000

total_gain, avg_return_rate, std_return_rate = calculate_investment_metrics(returns, monthly_investment)

print(f"總收益: {total_gain} 元")
print(f"投資報酬率平均值: {avg_return_rate}%")
print(f"投資報酬率標準差: {std_return_rate}%")
