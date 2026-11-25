# Scenario: A shopping cart remembers a discount rate between function calls.
def make_discount_calculator(rate):
    def apply_discount(price):
        return price - price * rate
    return apply_discount

student_discount = make_discount_calculator(0.10)
print("Original price: Rs.1000")
print("Student price: Rs.", student_discount(1000))
