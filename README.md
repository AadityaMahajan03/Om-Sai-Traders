
---

# 🛒 Om Sai Traders - Web-Based Management System

![GitHub stars](https://img.shields.io/github/stars/AadityaMahajan03/om-sai-traders?style=social)
![GitHub forks](https://img.shields.io/github/forks/AadityaMahajan03/om-sai-traders?style=social)

Welcome to **Om Sai Traders**, a powerful web-based management system designed to help businesses efficiently store, manage, and analyze company data. Built with **Django** and **SQLite**, this application streamlines inventory tracking, sales management, customer records, and financial transactions. It also supports **multi-table functionality** to store supplier information and other critical data.

---

## ✨ Features

- **Admin Login System**: Secure admin login to access the management system.
- **Multi-Table Functionality**: Store and manage data for suppliers, inventory, sales, and more.
- **Dashboard Overview**: Visualize key metrics and data at a glance.
- **User-Friendly Interface**: Intuitive and easy-to-use interface for seamless navigation.
- **Secure & Reliable**: Built with Django's robust security features to ensure data safety.

---

## 📸 Screenshots

### Before Login - Admin Login Page
![Admin Login](https://github.com/AadityaMahajan03/Om-Sai-Traders/blob/b552f19e06bf719a7b9aa6712b383d4f0d876aa8/Om%20Sai%20Traders%20Web%20App/app/dashboard.png)

The **admin login page** ensures secure access to the management system. Only authorized users can log in to view and manage data.

---

### After Login - Dashboard
![Dashboard](https://github.com/AadityaMahajan03/Om-Sai-Traders/blob/b552f19e06bf719a7b9aa6712b383d4f0d876aa8/Om%20Sai%20Traders%20Web%20App/app/dashboard2.png)
The **dashboard** provides an overview of key metrics, including supplier information, inventory levels, sales performance, and financial summaries.

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/om-sai-traders.git
   cd om-sai-traders
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the application**

   Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 📂 Project Structure

```
om-sai-traders/
├── manage.py
├── om_sai_traders/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── inventory/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── suppliers/
├── sales/
├── customers/
├── finance/
├── templates/
├── static/
└── requirements.txt
```

---

## 🛠️ Built With

- **Django** - The web framework used
- **SQLite** - Database management
- **HTML/CSS/JavaScript** - Frontend development
- **Bootstrap** - Frontend styling

---

## 🤝 Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 🙏 Acknowledgments

- Hat tip to anyone whose code was used.
- Inspiration.
- etc.

---

## 📧 Contact

For any inquiries, please reach out to us at [your-email@example.com](mailto:mahajanaaditya50.com).

---

⭐️ If you find this project helpful, don't forget to give it a star! ⭐️

---

**Happy Coding!** 🚀

---
