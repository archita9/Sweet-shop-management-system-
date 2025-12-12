# 🍬 Sweet Shop Management System (Python + TDD)

This is a **console-based Sweet Shop Management System** built with Python. It helps manage sweets inventory through a menu-driven interface. The project follows the **Test-Driven Development (TDD)** approach and includes automated unit tests using `pytest`.

---

## ✅ Features

- Add new sweets with validation
- View all sweets in inventory
- Delete sweets by name
- Sort sweets by name, category, price, or quantity
- Search sweets by:
  - Name
  - Category
  - Price range
- Purchase sweets (stock decreases)
- Restock sweets (stock increases)

---

## 🗂️ Project Folder Structure

```
Sweet_Shop/
├── main.py                  # Main menu-driven interface
├── sweet/                  
│   ├── __init__.py          # Package initializer
│   └── Classes_logics.py    # Business logic class (SweetShop)
├── tests/                  
│   └── test_sweet_shop.py   # Pytest test cases
├── test-report.txt          # Pytest output report (optional)
└── README.md                # Project documentation
```


---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Pytest** for unit testing
- **VS Code** (Recommended IDE)
- **TDD approach** for robust design

---

## 🚀 How to Run

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/sweet-shop.git
cd Sweet_Shop
```

2. **Run the main app:**

```bash
python main.py
```

3. Follow the on-screen menu to interact with the system.

---

## 🧪 Run Tests (with Pytest)

> Make sure pytest is installed:

```bash
pip install pytest
```

> Run tests and save report:

```bash
pytest tests/ > test-report.txt
```

> Optional: View `test-report.txt` in **UTF-8 format** to avoid garbage characters (`��=`).

In VS Code:
- Click `File → Reopen with Encoding → UTF-8`

---

## 📸 Example Use

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

## 👤 Author

- **Archita [Archita Goyal]**
- GitHub: [https://github.com/archita9]

---

## 📝 License

This project is open-source and free to use.


