menu = {
    "burger": 80.20,
    "pizza" : 35.30,
    "pasta" : 100.10,
    "sprite" : 40.20,
}

order = []
def display_menu():
    print("Menu")
    for item , price in menu.items():
        print(f"{item} Rs.{price:.2f}")

def take_order():
    display_menu()
    while True:
        choice = input("Enter the items to order (or 'done' to finish):").lower()
        if choice == 'done':
            break 
        elif choice in menu:
            order.append(choice)
        else:
            print("Invalid item.Please choose from the menu.")

def calculateTotal():
    total = sum(menu[item] for item in order)
    return total

def main():
    print("Welcome to food ordering app")
    while True:
        print("\nOptions:")
        print("1. Take an order")
        print("2. View order")
        print("3. Calculate total")
        print("4. Quit")
        choice = input("Enter your choice:")
        if choice == '1':
            take_order()
        elif choice=='2':
            print("Your current order:")
            for item in order:
                print(item)
        elif choice == '3':
            total = calculateTotal()
            print(f"Total cost of your order: Rs.{total:.2f}")
        elif choice == '4':
            print("Thank you for using the Food Ordering App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__=="__main__":
    main()
import tkinter as tk

def order_food():
    selected_item = menu_listbox.get(menu_listbox.curselection())

    print(f"Ordered: {selected_item}")

app = tk.Tk()
app.title("Food Ordering App")

# Create a list of menu items
menu_items = ["Pizza", "Burger", "Pasta", "Salad", "Sushi", "Ice Cream"]

# Create a Listbox to display the menu
menu_listbox = tk.Listbox(app)
for item in menu_items:
    menu_listbox.insert(tk.END, item)
menu_listbox.pack()

# Create an "Order" button
order_button = tk.Button(app, text="Order", command=order_food)
order_button.pack()

app.mainloop()

