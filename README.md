# Task Manager

Task Manager is a web application for managing tasks and categories. It provides a comprehensive backend developed with Django and a frontend implemented with Vue.js 3 Composition API.

## Features

- **Tasks:** Create, read, update, and delete tasks. Assign tasks to users and categorize them.
- **Categories:** Create, read, update, and delete categories for organizing tasks.
- **User Management:** Admins can manage users, including superuser privileges.
- **Authentication:** Users can authenticate via the provided authentication endpoints.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Nanguti/Django-Vuejs-Task-Manager-With-JWT.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Django-Vuejs-Task-Manager-With-JWT
   ```

3. Install dependencies for both backend and frontend:

   ```bash
   # Backend (Django)
   pip install -r requirements.txt

   # Frontend (Vue.js)
   cd frontend
   npm install
   ```

4. Set up the Django project:

   ```bash
   # Create and apply migrations
   python manage.py makemigrations
   python manage.py migrate

   # Create a superuser (for accessing the admin interface)
   python manage.py createsuperuser
   ```

5. Run the development servers:

   ```bash
   # Backend (Django)
   python manage.py runserver

   # Frontend (Vue.js)
   cd frontend
   npm run serve
   ```

6. Access the application in your browser:

   - Backend: http://localhost:8000
   - Frontend: http://localhost:3000

## API Endpoints

- **Admin Interface:** http://localhost:8000/admin/
- **Tasks API:** http://localhost:8000/api/v1/tasks/
- **Categories API:** http://localhost:8000/api/v1/categories/
- **User Management API:** http://localhost:8000/api/v1/users/

## Technologies Used

- **Backend:**

  - Django 5.0.3
  - Django Rest Framework
  - Djoser (for user authentication)
  - PostgreSQL (as the database)

- **Frontend:**
  - Vue.js 3
  - Vue Router (for routing)
  - Vuex (for state management)
  - Axios (for API requests)

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
