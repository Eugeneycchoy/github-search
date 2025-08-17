# GitHub Search App

A Django web application for searching GitHub users, built as part of a Frontend Mentor challenge.

## Features

- Search GitHub users
- Display user profile information
- Responsive design with Tailwind CSS
- Dark theme UI
- Clean, modern interface

## Technologies Used

- **Backend**: Django 5.2
- **Frontend**: HTML, Tailwind CSS
- **Font**: Space Mono
- **CSS Framework**: Tailwind CSS with django-tailwind

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js (for Tailwind CSS)

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd github-search
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install django django-tailwind
   ```

4. Install Tailwind CSS:
   ```bash
   cd github_search
   python manage.py tailwind install
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

### Development

1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

2. In a separate terminal, start the Tailwind CSS watcher:
   ```bash
   python manage.py tailwind start
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000`

## Project Structure

```
github_search/
├── github_search/          # Main Django project
├── home/                   # Home app
│   ├── static/
│   │   ├── css/           # Custom CSS
│   │   └── img/           # Images and icons
│   ├── templates/         # HTML templates
│   └── views.py
├── theme/                 # Tailwind CSS app
└── manage.py
```

## License

This project is part of a Frontend Mentor challenge.
