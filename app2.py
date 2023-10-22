import tkinter as tk

menu = {
    "Burger": 80,
    "Pizza": 35,
    "Pasta": 100,
    "Sprite": 40,
}

order = []

def display_menu():
    menu_text.config(state=tk.NORMAL)
    menu_text.delete('1.0', tk.END)
    for item, price in menu.items():
        menu_text.insert(tk.END, f"{item} - Rs. {price:.2f}\n")
    menu_text.config(state=tk.DISABLED)

def take_order():
    choice = item_entry.get().strip()
    if choice.lower() == 'done':
        item_entry.delete(0, tk.END)
    elif choice in menu:
        order.append(choice)
        item_entry.delete(0, tk.END)
        update_order_text()
    else:
        status_label.config(text="Invalid item. Please choose from the menu.")
        item_entry.delete(0, tk.END)

def calculate_total():
    total = sum(menu[item] for item in order)
    status_label.config(text=f"Total cost of your order: Rs. {total:.2f}")

def update_order_text():
    order_text.config(state=tk.NORMAL)
    order_text.delete('1.0', tk.END)
    for item in order:
        order_text.insert(tk.END, f"{item}\n")
    order_text.config(state=tk.DISABLED)

app = tk.Tk()
app.title("Food Ordering App")
app.geometry("600x500")

welcome_label = tk.Label(app, text="Welcome to the Food Ordering App!")
welcome_label.pack()

menu_text = tk.Text(app, height=10, width=30)
menu_text.pack()
menu_text.config(state=tk.DISABLED)
display_menu()

item_label = tk.Label(app, text="Enter the items to order:")
item_label.pack()

item_entry = tk.Entry(app)
item_entry.pack()

order_button = tk.Button(app, text="Order", command=take_order)
order_button.pack()

order_frame = tk.Frame(app)
order_frame.pack()

order_label = tk.Label(order_frame, text="Your current order:")
order_label.pack()

order_text = tk.Text(order_frame, height=10, width=30)
order_text.pack()
order_text.config(state=tk.DISABLED)

status_label = tk.Label(app, text="")
status_label.pack()

total_button = tk.Button(app, text="Calculate Total", command=calculate_total)
total_button.pack()

app.mainloop()