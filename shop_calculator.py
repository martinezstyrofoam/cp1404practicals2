"""A shop requires a small program that would allow them to quickly work out the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.

This uses f-string formatting to set the currency to 2 decimal places."""
menu = "Please enter the number of items."
print(menu)
shop_items_number = int(input("No. of items: "))
while shop_items_number < 0:
    print("Invalid number of items!")
    shop_items_number = int(input("No. of items: "))
if shop_items_number > 0:
    print(f"Number of items: {shop_items_number}")
    shop_items_total = 0
    for i in range(0, shop_items_number):
        shop_items_price = float(input("Price of item:"))
        shop_items_total += shop_items_price
    if shop_items_total > 100:
        shop_items_total = shop_items_total * 0.9
    print(f"Total price for {shop_items_number} is ${shop_items_total:.2f}")



