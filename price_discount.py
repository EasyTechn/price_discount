
def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount_amount=price*(discount_percent/100)
        print(f"price after discount {price-discount_amount}")
    else:
        print(price)
        print('no discount')
        
price=float(input("Enter price"))
discount_percent=float(input('Enter discount'))

calculate_discount(price,discount_percent)