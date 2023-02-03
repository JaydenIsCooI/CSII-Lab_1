def main_menu():
    print("----MAIN MENU----")
    print("s: Shop")
    print("x: Exit")

    user_option = input("Option: ").strip().lower()
    while user_option not in ['s', 'x']:
        user_option = input("Invalid (s/x): ").strip().lower()

    return user_option


def cart_menu():
    print("----CART MENU----")
    print("1: Cookie - $1.50")
    print("2: Sandwich - $4.00")
    print("3: Water - $1.00")

    user_item = input("Item: ").strip()
    while True:
        if user_item.isdigit() and int(user_item) in range(1, 4):
            return int(user_item)
        user_item = input("Invalid (1-3): ").strip()

# main
def main():
    cart = {}

    while True:

        user_option = main_menu()
        if user_option == "x":
            break

        user_item = cart_menu()

        match user_item:
            case 1:
                if "Cookie" in cart.keys():
                    cart["Cookie"][0] += 1
                else:
                    cart["Cookie"] = [1, 1.50]
            case 2:
                if "Sandwich" in cart.keys():
                    cart["Sandwich"][0] += 1
                else:
                    cart["Sandwich"] = [1, 4.00]
            case 3:
                if "Water" in cart.keys():
                    cart["Water"][0] += 1
                else:
                    cart["Water"] = [1, 1.00]

    grand_total = 0
    print("-" * 25)
    for item, info in cart.items():
        quantity = info[0]
        price = info[1]
        total = price * quantity
        grand_total += total
        print(f"({quantity}) - {item} = ${total:.2f}")
    print("-" * 25)
    print(f"GRAND TOTAL = ${grand_total:.2f}")
    print("-" * 25)

main()