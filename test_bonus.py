import products
import store

mac = products.Product("MacBook Air M2", price=1450, quantity=100)
bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
pixel = products.Product("Google Pixel 7", price=500, quantity=250)

best_buy = store.Store([mac, bose])

print(mac)               # MacBook Air M2, Price: 1450, Quantity: 100
print(mac > bose)        # True
print(mac in best_buy)   # True
print(pixel in best_buy) # False

# mac.price = -100       # Uncomment to check if it throws an Exception