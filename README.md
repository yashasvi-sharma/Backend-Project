# Multilingual FAQ System

This project implements a multilingual FAQ system using Django, Django Rest Framework, and various other technologies.

## Features

- Multilingual FAQ management
- WYSIWYG editor for answers using django-ckeditor
- REST API for retrieving FAQs with language selection
- Caching mechanism using Redis
- Automatic translation using Google Translate API
- Admin panel for managing FAQs
- Unit tests using pytest

## Installation

1. Set up a virtual environment:
   \`\`\`
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   \`\`\`

2. Install dependencies:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

3. Set up environment variables:
   Create a `.env` file in the project root and add:
   \`\`\`
   DJANGO_SECRET_KEY=your_secret_key
   GOOGLE_TRANSLATE_API_KEY=your_google_translate_api_key
   \`\`\`

4. Run migrations:
   \`\`\`
   python manage.py makemigrations
   python manage.py migrate
   \`\`\`

5. Create a superuser:
   \`\`\`
   python manage.py createsuperuser
   \`\`\`

6. Run migrations:
   \`\`\`
   python manage.py makemigrations faq
   python manage.py migrate faq
   python manage.py showmigrations
   python manage.py migrate
   \`\`\`

7. Run the development server:
   \`\`\`
   python manage.py runserver
   \`\`\`

8. Access the application:
   \`\`\`
    Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
    FAQ list: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    API: [http://127.0.0.1:8000/api/faqs/](http://127.0.0.1:8000/api/faqs/)
   \`\`\`


## Running Tests

To run the test suite:

\`\`\`
pytest
\`\`\`

## Docker Support

To run the application using Docker:

1. Build the Docker image:
   \`\`\`
   docker-compose build
   \`\`\`

2. Run the containers:
   \`\`\`
   docker-compose up
   \`\`\`


