## 📚 Book Review & Management System

A role-based Book Review and Management web application built using Django that allows users to explore books, while providing editors and administrators with full content management capabilities.

### 🚀 Features

#### 👤 Authentication & Roles
- Custom user system (based on Django AbstractUser)
- Role-based access control:
  - Admin → full access
  - Editor → manage books, authors, genres
  - User → read-only access

#### 📖 Book Management
- Create, update, delete books (restricted by permissions)
- Book details include:
  - Title
  - Author
  - Genres (Many-to-Many)
  - Featured image
  - Plot/description

#### 🔍 Search System
- Keyword-based search across:
  - Book titles
  - Authors
  - Genres
- Case-insensitive partial matching

#### 🧑‍💼 Author & Genre System
- Authors linked to multiple books
- Genres used for categorization
- Annotated book counts per author/genre

#### 📊 UI & UX
- Responsive card + table-based layouts
- Pagination support for large datasets
- Clean dashboard-style views for admin/editor workflows

#### ⚙️ Backend Features
- Optimized queries using:
  - select_related
  - prefetch_related
  - annotate
- Class-Based Views + Function-Based Views
- Django forms with validation
- Custom permissions using Django auth system

#### 🧪 Testing
- Model tests
- View tests
- Form validation tests
- Permission tests
- Signal tests (email + file cleanup)

#### 📩 Signals
- Welcome email sent on user registration
- Automatic cleanup of user avatars on deletion

#### 🛠 Tech Stack
- Backend: Django
- Database: SQLite / PostgreSQL (configurable)
- Frontend: HTML, CSS, Bootstrap-style components
- ORM: Django ORM
- Authentication: Django built-in auth system

#### 🔐 Permissions System

The project uses Django permissions:

- books.add_*
- books.change_*
- books.delete_*
- books.view_*

Access is enforced using:

- LoginRequiredMixin
- PermissionRequiredMixin

#### 🔎 Example URLs
- /api/books/ → Book listing
- /api/authors/ → Author listing (editor/admin only)
- /api/genres/ → Genre listing (editor/admin only)
- /api/books/search/?q=django → Search books
- /api/books/<id>/ → Book detail

#### 📦 Installation

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

git clone https://github.com/Coder-Ankit001/Book_Review_App_With_Django.git

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

#### 👤 Default Roles Setup

Create superuser:

```bash
python manage.py createsuperuser
```

Assign roles via Django admin:
- Admin
- Editor
