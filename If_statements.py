is_hot = False
is_cold = False
if is_hot:
    print("Its a hot day")
    print("Enjoy your day")
elif is_cold:
    print("its a cold day")
    print(("Wear warm cloth"))
else:
    print("Its a lovely day")

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")