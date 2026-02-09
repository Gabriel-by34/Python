#WHEN Assignment.
# In this Assignment you will come Up with a Program that will store some Gross Salary in variable, Then Using If Else...Else if Statements Determine the Monthly Contribution Someone will Pay.Use Below Image For Reference.
grosssalary=int(input("enter your salary here:"))
if grosssalary>0 and grosssalary<=5999:
    print("monthly contribution is ksh150"),
elif grosssalary>5999 and grosssalary<=7999:
    print("monthly contribution is ksh 300")
elif grosssalary>7999 and grosssalary<=11999:
    print("monthly contribution is Ksh 400")
elif grosssalary>11999 and grosssalary<=14999:
    print("monthly contribution is ksh 500")
elif grosssalary>14999 and grosssalary<=19999:
    print("monthly contribution is Ksh600")
elif grosssalary>19999 and grosssalary<=24999:
    print("monthly contribution is Ksh750")
elif grosssalary>24999 and grosssalary <=29999:
    print("monthly contribution is Ksh 850")
elif grosssalary>29999 and grosssalary<=49999:
    print("monthly contribution is Ksh1000")
elif grosssalary>49999 and grosssalary <=99999:
    print("monthly contribution is Ksh1500")
else:
    print("monthly contribution as Ksh2000")
