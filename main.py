import products
import store
import promotions

"""Initial setup for store products"""
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

"""Setup promotions catalog"""
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

"""Assign promotions to specific products"""
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = store.Store(product_list)


def start(store_obj):
    """Main CLI interaction loop"""
    while True:
        print("\n--- Store Menu ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option (1-4): ").strip()

        if choice == "1":
            print("\nAvailable Products:")
            active_items = store_obj.get_all_products()
            for i, p in enumerate(active_items, 1):
                print(f"{i}. {p.show()}")

        elif choice == "2":
            total_items = store_obj.get_total_quantity()
            print(f"\nTotal items in store: {total_items}")

        elif choice == "3":
            active_items = store_obj.get_all_products()
            if not active_items:
                print("Store is completely out of stock!")
                continue

            shopping_list = []
            while True:
                print("\nWhat do you want to buy? (Press Enter to finish)")
                for i, p in enumerate(active_items, 1):
                    print(f"{i}. {p.show()}")

                prod_idx = input("Product number: ").strip()
                if not prod_idx:
                    break

                qty_str = input("Quantity: ").strip()

                try:
                    idx = int(prod_idx) - 1
                    qty = int(qty_str)

                    if 0 <= idx < len(active_items) and qty > 0:
                        shopping_list.append((active_items[idx], qty))
                        print("Added to cart!")
                    else:
                        print("Invalid product number or quantity.")
                except ValueError:
                    print("Please enter valid numbers.")

            if shopping_list:
                try:
                    grand_total = store_obj.order(shopping_list)
                    print(f"\nOrder successful! Total cost: ${grand_total}")
                except Exception as e:
                    print(f"Order failed: {e}")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid selection, try again.")


if __name__ == "__main__":
    start(best_buy)