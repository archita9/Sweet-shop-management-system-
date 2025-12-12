# 🍬 Sweet Shop Management System

*A Python console application built using Test-Driven Development (TDD)*

The **Sweet Shop Management System** is a menu-driven Python application that helps manage sweets, track stock, search items, sort inventory, and process purchases.
This project is structured using a **Test-Driven Development (TDD)** workflow and includes a full suite of automated tests using **pytest**.

---

## 🌟 Key Features

✔ **Add new sweets** with input validation
✔ **Delete sweets** by name
✔ **View complete inventory**
✔ **Sort sweets** by:

* Name
* Category
* Price
* Quantity
  ✔ **Search sweets** by:
* Name
* Category
* Price Range
  ✔ **Purchase sweets** (automatically decreases stock)
  ✔ **Restock sweets**
  ✔ **Fully tested code** following TDD principles

---

## 📁 Project Structure

```
Sweet_Shop_Management_System/
│
├── main.py                    # Entry point – menu-driven console UI
│
├── sweet/
│   ├── __init__.py
│   └── Classes_logics.py      # Core business logic (SweetShop class)
│
├── tests/
│   └── test_sweet_shop.py     # Pytest test cases based on TDD
│
├── test-report.txt            # Auto-generated pytest report
│
└── README.md                  # Project documentation
```

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Pytest** for automated testing
* **OOP** (Object-Oriented Programming)
* **TDD (Test-Driven Development)**
* Developed in **VS Code**

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Sweet_Shop_Management_System.git
cd Sweet_Shop_Management_System
```

### 2️⃣ Run the application

```bash
python main.py
```

You will see a console menu like:

```
====== SWEET SHOP MANAGEMENT SYSTEM ======
1. Add Sweet
2. Delete Sweet
3. View All Sweets
4. Sort Sweets
5. Purchase Sweet
6. Restock Sweet
7. Search Sweets
8. Exit
```

---

## 🧪 Running Tests (TDD)

### Install pytest

```bash
pip install pytest
```

### Run test suite

```bash
pytest
```

### Export test output to file

```bash
pytest > test-report.txt
```

If `test-report.txt` shows weird characters, open it in VS Code using:

**File → Reopen with Encoding → UTF-8**

---

## 🖼️ Sample Operations

```
Enter choice: 1
Enter Sweet Name: Rasgulla
Enter Category: Milk
Enter Price: 20
Enter Quantity: 50
Sweet added successfully!
```

Each action is validated and processed using methods inside the *SweetShop* class.

---

## 👩‍💻 Author

**Archita Goyal**
🔗 GitHub: [https://github.com/archita9](https://github.com/archita9)

---




