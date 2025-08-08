'''
num = 10
if num > 10:
    print("inside if block")
else:
    print("else block")
'''
'''
scores = float(input("input your scores: "))
if 70<= scores <100:
    print("your grade is A")
elif 50<= scores <69.9:
    print("your grade is B")
elif 40 <= scores <59.9:
    print("your grade is C")
elif 30 <= scores <49.9:
    print("your grade is D")
elif 0 <= scores < 30.9:
    print("F you fail the course")
else:
    print("invalid entry")
'''
'''

Task 2: Smart Restaurant Discount System

You are helping a restaurant in Jos implement an automated discount system for their weekend promo.

The rules are:
Customers with a loyalty card get a 10% discount.,
If the customer's order amount is above 20,000 NGN:
Loyalty card holders get an additional 5% discount.,
Non-loyalty card holders get a free soft drink instead.,
,
Students (verified with student ID) get an extra 5% discount on top of whatever they qualify for.,

Customer data is stored in a dictionary like this:

customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

Write a nested if-else block that:
Calculates the final discount or freebie for the customer.,
Stores the result in a dictionary called order_summary.,
Prints out a summary for the cashier.,
"""
'''

percent = 0
customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True, 
    "is_student": True
}

if customer["loyalty_card"]:
    percent += 10

if customer["order_amount"] > 20000:
    if customer["loyalty_card"] == True:
        percent +=5
    else:
        print("you get a free drink")

if customer["is_student"]:
    percent +=5
    
percentage = percent
print(percentage)

discount = percentage/100 *customer["order_amount"]
print(discount)

amount_to_pay = customer["order_amount"] - discount
print(amount_to_pay)

customer.update({"discount":discount, "percentage":percentage, "amount_to_pay": amount_to_pay})
print(customer)
