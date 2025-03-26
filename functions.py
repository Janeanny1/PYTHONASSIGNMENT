def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percent: "))

if discount_percent >= 20:
    final_price = calculate_discount(original_price, discount_percent)
    print(f"Final price after discount: {final_price:}") 
else:
    print(f"No discount. The price remains: {original_price:}")