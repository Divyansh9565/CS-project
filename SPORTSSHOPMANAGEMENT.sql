create database SportsShopManagement;
use SportsShopManagement;
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(50) NOT NULL,
    Category VARCHAR(30) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Stock INT NOT NULL
);
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerName VARCHAR(50) NOT NULL,
    ContactNumber VARCHAR(15),
    Email VARCHAR(50)
);
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT NOT NULL,
    SaleDate DATE NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
INSERT INTO Products (ProductName, Category, Price, Stock) VALUES
('Football', 'Outdoor', 500.00, 20),
('Cricket Bat', 'Outdoor', 1500.00, 15),
('Tennis Racket', 'Indoor', 1200.00, 10),
('Basketball', 'Outdoor', 600.00, 25);
INSERT INTO Customers (CustomerName, ContactNumber, Email) VALUES
('John Doe', '9876543210', 'john.doe@example.com'),
('Jane Smith', '9123456789', 'jane.smith@example.com');
INSERT INTO Sales (CustomerID, ProductID, Quantity, SaleDate) VALUES
(1, 1, 2, '2025-01-01'),
(2, 3, 1, '2025-01-02');
SELECT * FROM Prducts;
SELECT * FROM Customers;
SELECT * FROM SALES;
SELECT 
    Sales.SaleID, 
    Customers.CustomerName, 
    Products.ProductName, 
    Sales.Quantity, 
    Sales.SaleDate
FROM Sales
JOIN Customers ON Sales.CustomerID = Customers.CustomerID
JOIN Products ON Sales.ProductID = Products.ProductID;
UPDATE Products
SET Stock = Stock - 2
WHERE ProductID = 1;
SELECT ProductName, Stock FROM Products WHERE Stock > 10;
DELETE FROM Products WHERE ProductID = 4;
SELECT * FROM PRODUCTS;
SELECT * FROM CUSTOMERS;
SELECT * FROM SALES;














