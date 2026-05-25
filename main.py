import products
import store


def start(store_obj):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        user_input = input("Please choose a number: ")

        if user_input == "1":
            print("------")
            all_items = store_obj.get_all_products()
            for i in range(len(all_items)):
                print(str(i + 1) + ". " + all_items[i].show())
            print("------")

        elif user_input == "2":
            total = store_obj.get_total_quantity()
            print("Total items in store: " + str(total))

        elif user_input == "3":
            all_items = store_obj.get_all_products()
            print("------")
            for i in range(len(all_items)):
                print(str(i + 1) + ". " + all_items[i].show())
            print("------")

            basket = []
            print("When you want to finish order, enter empty text.")

            while True:
                pick = input("Which product # do you want? ")
                qty = input("Amount? ")

                if pick == "" or qty == "":
                    break

                try:
                    product_index = int(pick) - 1
                    amount = int(qty)
                    basket.append((all_items[product_index], amount))
                    print("Added to cart!")
                except:
                    print("Error with input, try again.")

            if len(basket) > 0:
                try:
                    total_price = store_obj.order(basket)
                    print("Order made! Total cost: " + str(total_price))
                except Exception as e:
                    print("Order failed: " + str(e))

        elif user_input == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    setup_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(setup_list)
    start(best_buy)
