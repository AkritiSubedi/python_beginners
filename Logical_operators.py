# and or not
high_income = True
good_credit = False
if high_income and good_credit :
    print("Eligible for loan")
elif high_income or good_credit:
    print("May be Eligible for loan")
else:
    print(("Not Eligible for loan"))



has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan!!!")