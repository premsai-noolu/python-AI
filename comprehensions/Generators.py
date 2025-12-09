#It is like a list comprehension, but it does not store all values in memory.
#It generates values one by one when needed.

daily_sales = [5, 10,12, 7, 3, 8, 9, 15,2]

total_cups = (sale for sale in daily_sales if sale > 5)

print(total_cups)

"""2. total_cups_sum = sum(sale for sale in daily_sales if sale > 5)
Here, you directly pass the generator expression into sum().
✔ What happens:
Python goes through each value that is > 5 and adds them."""

total_cups_sum = sum(sale for sale in daily_sales if sale > 5)
print(total_cups_sum)