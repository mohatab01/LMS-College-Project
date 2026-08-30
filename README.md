# LMS — Library Management System

A Library Management System built as a custom Odoo module for the university graduation project. It handles books, categories, students, and the borrowing process.

## 🛠️ Tech Stack

- Odoo (Python framework)
- XML (views & menus)
- PostgreSQL (Odoo's underlying database)

## 🏗️ Structure

- **models/** — core entities: `book`, `category`, `student`, `borrows`
- **controllers/** — module controllers
- **views/website/** — front-end pages (home, menu, view definitions)
- **security/** — access rights configuration (`ir.model.access.csv`)
- **static/** — front-end assets

## ✨ Features

- Manage books and categories
- Manage student records
- Track book borrowing and returns
- Basic website front-end for the library
