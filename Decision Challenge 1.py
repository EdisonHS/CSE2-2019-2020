order_amt = float(input("What is the order amount?"))
state = input("What state is it?")
tax = 0
if state == "CA":
    tax = 0.08
tax_amt = tax * order_amt
print("The subtotal is {:.2f}".format(order_amt))
print("The tax is {:.2f}".format(tax_amt))
total_cost = order_amt + tax_amt
print("The total cost is {:.2f}".format(total_cost))
