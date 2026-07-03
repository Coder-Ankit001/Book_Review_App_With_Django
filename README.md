# 📚 Book Review & Management System

A role-based **Book Review and Management** web application built with **Django**, letting readers explore a catalog of books while giving editors and administrators full content-management capabilities — backed by PostgreSQL full-text search with relevance ranking.

![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Full--Text%20Search-4169E1?logo=postgresql&logoColor=white)

<div align="center">
  <a href="https://book-review-app-with-django.onrender.com">🌐 Live Demo</a> 
</div>

---


## ✨ Overview

This project is a full-stack book cataloging and review platform demonstrating production-grade Django patterns: role-based access control, optimized ORM querying, weighted full-text search, signal-driven side effects, and thorough test coverage.

---

## 🚀 Features

### 👤 Authentication & Roles
- Custom user model (extends Django's `AbstractUser`)
- Role-based access control:
  | Role | Permissions |
  |------|-------------|
  | **Admin** | Full access — manage users, books, authors, genres |
  | **Editor** | Create/update books, authors, genres |
  | **User** | Read-only access — browse, search, review |

### 📖 Book Management
- Create, update, and delete books (permission-restricted)
- Book details include:
  - Title
  - Author
  - Genres (Many-to-Many)
  - Featured image
  - Plot / description

### 🔍 Full-Text Search (PostgreSQL)
Replaced naive `icontains` filtering with PostgreSQL's native full-text search stack for faster, more relevant results:

- **`SearchVector`** — indexes searchable text across multiple fields
- **`SearchQuery`** — parses and normalizes the user's query (stemming, stop-word handling)
- **`SearchRank`** — scores and orders results by relevance
- **Weighted fields** so matches in more important fields rank higher:

  | Field | Weight |
  |-------|--------|
  | Title | `A` (highest) |
  | Author name | `B` |
  | Genre | `C` |
  | Plot / description | `D` (lowest) |

  This means a search for `"django"` ranks a book **titled** "Django Unleashed" above one that merely **mentions** Django in its plot summary.

- Still case-insensitive and supports partial/keyword matching across titles, authors, and genres
- Falls back gracefully to `icontains` search on SQLite (since PostgreSQL FTS extensions aren't available there) — see [Database Notes](#-database-notes)

### 🧑‍💼 Author & Genre System
- Authors linked to multiple books
- Genres used for categorization
- Annotated book counts per author/genre (`annotate(book_count=Count("books"))`)

### 📊 UI & UX
- Responsive card- and table-based layouts
- Pagination for large datasets
- Clean, dashboard-style views for admin/editor workflows

### ⚙️ Backend Engineering
- Optimized queries using `select_related`, `prefetch_related`, and `annotate`
- Mix of Class-Based Views and Function-Based Views where each fits best
- Django forms with server-side validation
- Custom permissions layered on top of Django's built-in auth system

### 🧪 Testing
- Model tests
- View tests
- Form validation tests
- Permission tests
- Signal tests (welcome email, avatar cleanup)
- Search ranking tests (verifying weighted relevance ordering)

### 📩 Signals
- Welcome email sent on user registration
- Automatic cleanup of user avatar files on account deletion

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django |
| Database | PostgreSQL (recommended, required for full-text search) / SQLite (dev fallback) |
| Frontend | HTML, CSS, Bootstrap-style components |
| ORM | Django ORM |
| Search | PostgreSQL `SearchVector` / `SearchQuery` / `SearchRank` |
| Auth | Django built-in authentication |

---

## 🔐 Permissions System

Enforced via Django's built-in permission framework:

- `books.add_*`
- `books.change_*`
- `books.delete_*`
- `books.view_*`

Applied using:
- `LoginRequiredMixin`
- `PermissionRequiredMixin`

---

## 🔎 Example URLs

| Endpoint | Description | Access |
|----------|-------------|--------|
| `/api/books/` | Book listing | All users |
| `/api/authors/` | Author listing | Editor/Admin |
| `/api/genres/` | Genre listing | Editor/Admin |
| `/api/books/search/?q=django` | Weighted full-text search | All users |
| `/api/books/<id>/` | Book detail | All users |

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/Coder-Ankit001/Book_Review_App_With_Django.git
cd Book_Review_App_With_Django

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your database (see Database Notes below)

# 5. Apply migrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver
```

### 🗄 Database Notes

Full-text search relies on PostgreSQL's `django.contrib.postgres` search module. To use it:

1. Set `DATABASES` in `settings.py` to a PostgreSQL connection.
2. Add `'django.contrib.postgres'` to `INSTALLED_APPS`.
3. (Optional but recommended) Add a `GinIndex` on the search vector for large datasets:

   ```python
   from django.contrib.postgres.indexes import GinIndex

   class Meta:
       indexes = [GinIndex(fields=["search_vector"])]
   ```

If running on SQLite for local development, the app falls back to a simpler `icontains`-based search — full-text ranking is unavailable in that mode.

---

## 👤 Default Roles Setup

1. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

2. Log in to the Django admin panel and assign roles/groups:
   - **Admin**
   - **Editor**

3. Assign the relevant `books.*` permissions to each group as needed.

---
