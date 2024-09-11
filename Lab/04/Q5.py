class Restaurant:
    def __init__(self):
        self.menu_items = {}  
        self.book_table = {}  
        self.customer_orders = {}  
    def add_item(self, item, price):
        self.menu_items[item] = price
        print(f"Added {item} to the menu for ${price:.2f}")
    def book_tables(self, table_number, customer_name):
        self.book_table[table_number] = customer_name
        print(f"Table {table_number} booked for {customer_name}")
    def customer_order(self, table_number, order):
        if table_number in self.book_table:
            if table_number not in self.customer_orders:
                self.customer_orders[table_number] = []
            self.customer_orders[table_number].append(order)
            print(f"Order {order} placed for table {table_number}")
        else:
            print("Table not booked. Please book a table first.")
    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price:.2f}")
    def print_reservations(self):
        print("Table Reservations:")
        for table_number, customer_name in self.book_table.items():
            print(f"Table {table_number}: {customer_name}")

    def print_orders(self):
        print("Customer Orders:")
        for table_number, orders in self.customer_orders.items():
            print(f"Table {table_number}: {', '.join(orders)}")
restaurant = Restaurant()
restaurant.add_item("Burger", 10.99)
restaurant.add_item("Pizza", 12.99)
restaurant.add_item("Salad", 8.99)
restaurant.book_tables(1, "John Doe")
restaurant.book_tables(2, "Jane Doe")
restaurant.customer_order(1, "Burger")
restaurant.customer_order(1, "Pizza")
restaurant.customer_order(2, "Salad")
restaurant.print_menu()
restaurant.print_reservations()
restaurant.print_orders()
