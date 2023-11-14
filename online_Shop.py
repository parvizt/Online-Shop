import tkinter as tk
from tkinter import messagebox
import pyodbc

class OnlineShopDatabaseCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Shop Database Creator")

        self.label = tk.Label(root, text="Online Shop Database Creator", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.make_db_button = tk.Button(root, text="RUN MAKE DATABASE", command=self.create_database, bg="green", fg="white")
        self.make_db_button.grid(row=1, column=0, pady=10)

        self.exit_button = tk.Button(root, text="EXIT", command=root.destroy, bg="red", fg="white")
        self.exit_button.grid(row=1, column=2, pady=10)

    def create_database(self):
        try:
            conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-2EA2N5I;Database=Online Shop;Trusted_Connection=yes;')
            cursor = conn.cursor()

            # ایجاد جداول

            cursor.execute('''
                CREATE TABLE Products (
                    ProductID INT PRIMARY KEY,
                    Name NVARCHAR(255),
                    Description NVARCHAR(MAX),
                    Price DECIMAL(10, 2),
                    Sold NVARCHAR(50),
                    Bought NVARCHAR(50),
                    StockQuantity INT,
                    Category NVARCHAR(50),
                    Brand NVARCHAR(50),
                    CreatedDate DATE,
                    ImageURLs NVARCHAR(MAX)
                )
            ''')

            cursor.execute('''
                CREATE TABLE Customers (
                    CustomerID INT PRIMARY KEY,
                    FirstName NVARCHAR(50),
                    LastName NVARCHAR(50),
                    Gender NVARCHAR(1),
                    Email NVARCHAR(100),
                    Password NVARCHAR(255),
                    ShippingAddress NVARCHAR(MAX),
                    BillingAddress NVARCHAR(MAX),
                    RegistrationDate DATE
                )
            ''')

            cursor.execute('''
                CREATE TABLE Employees (
                    EmployeeID INT PRIMARY KEY,
                    FirstName NVARCHAR(50),
                    LastName NVARCHAR(50),
                    Position NVARCHAR(50),
                    Email NVARCHAR(100),
                    Password NVARCHAR(255),
                    HireDate DATE,
                    Salary DECIMAL(10, 2)
                )
            ''')

            # ادامه ایجاد جداول برای Orders، OrderDetails، Payment، Reviews، Categories و Brands

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Online Shop database created successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineShopDatabaseCreator(root)
    root.mainloop()
