CREATE TABLE Authors (
    Author_ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL
);

CREATE TABLE Books (
    Book_ID INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Author_ID INT NOT NULL,
    Price DECIMAL(10,2),
    FOREIGN KEY (Author_ID) REFERENCES Authors(Author_ID)
);

CREATE TABLE Customers (
    Customer_ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Customer_ID INT NOT NULL,
    Order_Date DATE NOT NULL,
    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID)
);

CREATE TABLE Order_Details (
    Order_Detail_ID INT PRIMARY KEY,
    Order_ID INT NOT NULL,
    Book_ID INT NOT NULL,
    Quantity INT NOT NULL,
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID),
    FOREIGN KEY (Book_ID) REFERENCES Books(Book_ID)
);

