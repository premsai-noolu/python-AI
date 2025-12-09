tea_prices_inr = {
    "masala_chai": 40,
    "Green_tea": 50,
    "lemon_tea":200
}

tea_prices_usd ={item: price / 80 for item,price in tea_prices_inr.items()}

print(tea_prices_usd)