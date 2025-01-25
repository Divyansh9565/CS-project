import mysql.connector

# Step 1: Connect to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="verma1divyansh",
    database="SportsShopManagement"
)
cursor = connection.cursor()

# Step 2: Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(50) NOT NULL,
    Category VARCHAR(30) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Stock INT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerName VARCHAR(50) NOT NULL,
    ContactNumber VARCHAR(15),
    Email VARCHAR(50)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT NOT NULL,
    SaleDate DATE NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
)
""")

# Step 3: Insert sample data
def insert_sample_data():
    # Insert Products
    products = [
        ("Football", "Outdoor", 500.00, 20),
        ("Cricket Bat", "Outdoor", 1500.00, 15),
        ("Tennis Racket", "Indoor", 1200.00, 10),
        ("Basketball", "Outdoor", 600.00, 25)
    ]
    cursor.executemany("""
    INSERT INTO Products (ProductName, Category, Price, Stock) VALUES (%s, %s, %s, %s)
    """, products)

    # Insert Customers
    customers = [
        ("John Doe", "9876543210", "john.doe@example.com"),
        ("Jane Smith", "9123456789", "jane.smith@example.com")
    ]
    cursor.executemany("""
    INSERT INTO Customers (CustomerName, ContactNumber, Email) VALUES (%s, %s, %s)
    """, customers)

    # Insert Sales
    sales = [
        (1, 1, 2, datetime(2025, 1, 1).date()),
        (2, 3, 1, datetime(2025, 1, 2).date())
    ]
    cursor.executemany("""
    INSERT INTO Sales (CustomerID, ProductID, Quantity, SaleDate) VALUES (%s, %s, %s, %s)
    """, sales)

    connection.commit()

# Uncomment the following line to insert data initially
# insert_sample_data()

# Step 4: Queries for management
def display_products():
    cursor.execute("SELECT * FROM Products")
    for row in cursor.fetchall():
        print(row)

def display_customers():
    cursor.execute("SELECT * FROM Customers")
    for row in cursor.fetchall():
        print(row)

def display_sales():
    cursor.execute("""
    SELECT Sales.SaleID, Customers.CustomerName, Products.ProductName, Sales.Quantity, Sales.SaleDate
    FROM Sales
    JOIN Customers ON Sales.CustomerID = Customers.CustomerID
    JOIN Products ON Sales.ProductID = Products.ProductID
    """)
    for row in cursor.fetchall():
        print(row)

def update_stock(product_id, quantity_sold):
    cursor.execute("""
    UPDATE Products
    SET Stock = Stock - %s
    WHERE ProductID = %s
    """, (quantity_sold, product_id))
    connection.commit()

def check_low_stock():
    cursor.execute("SELECT ProductName, Stock FROM Products WHERE Stock < 10")
    for row in cursor.fetchall():
        print(row)

# Additional SQL functions
def count_products():
    cursor.execute("SELECT COUNT(*) FROM Products")
    print("Total products:", cursor.fetchone()[0])

def average_price():
    cursor.execute("SELECT AVG(Price) FROM Products")
    print("Average product price:", cursor.fetchone()[0])

def max_price():
    cursor.execute("SELECT MAX(Price) FROM Products")
    print("Maximum product price:", cursor.fetchone()[0])

def min_price():
    cursor.execute("SELECT MIN(Price) FROM Products")
    print("Minimum product price:", cursor.fetchone()[0])

def sum_of_sales():
    cursor.execute("SELECT SUM(Quantity) FROM Sales")
    print("Total quantity sold:", cursor.fetchone()[0])

def total_revenue():
    cursor.execute("""
    SELECT SUM(Sales.Quantity * Products.Price) AS TotalRevenue
    FROM Sales
    JOIN Products ON Sales.ProductID = Products.ProductID
    """)
    print("Total revenue:", cursor.fetchone()[0])

def find_customer_sales(customer_id):
    cursor.execute("""
    SELECT Sales.SaleID, Products.ProductName, Sales.Quantity, Sales.SaleDate
    FROM Sales
    JOIN Products ON Sales.ProductID = Products.ProductID
    WHERE Sales.CustomerID = %s
    """, (customer_id,))
    for row in cursor.fetchall():
        print(row)

def product_details_by_category(category):
    cursor.execute("SELECT * FROM Products WHERE Category = %s", (category,))
    for row in cursor.fetchall():
        print(row)

def recent_sales():
    cursor.execute("SELECT * FROM Sales ORDER BY SaleDate DESC LIMIT 5")
    for row in cursor.fetchall():
        print(row)

def delete_old_sales(threshold_date):
    cursor.execute("DELETE FROM Sales WHERE SaleDate < %s", (threshold_date,))
    connection.commit()
    print("Old sales records deleted.")

# Example usage
def main():
    print("Products:")
    display_products()

    print("\nCustomers:")
    display_customers()

    print("\nSales:")
    display_sales()

    print("\nUpdating stock for ProductID 1 by reducing 2 items...")
    update_stock(1, 2)

    print("\nLow stock products:")
    check_low_stock()

    print("\nCounting products...")
    count_products()

    print("\nCalculating average product price...")
    average_price()

    print("\nFinding maximum product price...")
    max_price()

    print("\nFinding minimum product price...")
    min_price()

    print("\nCalculating total sales quantity...")
    sum_of_sales()

    print("\nCalculating total revenue...")
    total_revenue()

    print("\nFinding sales for CustomerID 1...")
    find_customer_sales(1)

    print("\nFetching product details for category 'Outdoor'...")
    product_details_by_category('Outdoor')

    print("\nDisplaying recent sales...")
    recent_sales()

    print("\nDeleting old sales before 2025-01-01...")
    delete_old_sales('2025-01-01')

if __name__ == "__main__":
    main()

# Close the connection
cursor.close()
connection.close()
