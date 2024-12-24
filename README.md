# Labelbox Web App

A Django-based web application for annotating images

## Features

- **User Authentication**:
  Register, login, and logout functionality.
  User-specific annotation tracking.
- **Annotation**:
  Annotate images directly from the web interface.
  Save annotations to the database without local device storage.
- **Deployment**:
  Fully containerized using Docker for easy deployment.

## Technology Stack

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Deployment**: Docker

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/benjaminogbonna/labelbox.git
cd labelbox
```

### 2. Install Dependencies

Create a virtual environment and install the necessary dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Django

Run the following commands to set up the Django project:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

The app will be accessible at `http://127.0.0.1:8000/`.

## Using Docker
```bash
docker build -t labelbox .
docker run -d -p 8000:8000 labelbox
```

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License.
