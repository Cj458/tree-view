# Department Tree View Application

This project provides a hierarchical tree view of departments and their employees, fetching data from a Django REST API. It allows users to expand departments to view their children and a paginated list of employees.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Backend Setup](#backend-setup)
5. [Frontend Setup](#frontend-setup)
6. [Running the Application](#running-the-application)
7. [Usage](#usage)
8. [Screenshots](#screenshots)
9. [Contributing](#contributing)
10. [License](#license)

## Introduction

This application is designed to display a hierarchical structure of departments and employees. The frontend is built with React, and the backend is powered by Django REST Framework, providing paginated API endpoints for departments and employees.

## Features

- Expandable and collapsible department tree view.
- Fetches department and employee data from a Django REST API.
- Paginated employee lists to handle large datasets.
- Search functionality to filter departments by name.
- Modern, Apple-like styling for the user interface.

## Technologies Used

- **Frontend**: React, CSS
- **Backend**: Django, Django REST Framework

## Backend Setup

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Cj458/tree-view.git
    cd tree-view/backend
    ```

2. **Set Up Python Environment**:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Run the seed script**:
    ```sh
    python manage.py seed_db
    ```
6. **Run the Server**:
    ```sh
    python manage.py runserver
    ```

## Frontend Setup

1. **Navigate to Frontend Directory**:
    ```sh
    cd frontend
    ```

2. **Install Dependencies**:
    ```sh
    npm install
    ```

3. **Start the React Application**:
    ```sh
    npm start
    ```

## Running the Application

- Ensure both the backend and frontend servers are running.
- Open your browser and navigate to `http://localhost:3000` to see the application in action.

## Usage

1. **Viewing Departments**: Expand and collapse departments by clicking on the toggle icons.
2. **Viewing Employees**: Expand a department to see a list of employees. Click "Load More..." to fetch additional employees.
3. **Searching**: Use the search bar to filter departments by name.

## Screenshots

### Main View

![Rest API](https://drive.google.com/file/d/1x9AokM8DOqbPum15myrp989-OkVfCY0Y/view?usp=sharing)

### Expanded Department

![Main view](https://drive.google.com/file/d/1e6IhqV-C2jAF5omJiDyY5RXu1bpe9tzK/view?usp=sharing)

### Employee List

![Employee List](https://drive.google.com/file/d/1Nw_75n3UwxfcrV5oqzi4YHpwXPw5Djka/view?usp=sharing)

## Contributing

1. **Fork the Repository**: Click the Fork button at the top right of this page.
2. **Clone Your Fork**: 
    ```sh
    git clone https://github.com/Cj458/tree-view.git
    cd tree-view
    ```
3. **Create a Branch**: 
    ```sh
    git checkout -b feature/your-feature-name
    ```
4. **Make Your Changes**: Commit your changes.
5. **Push to Your Fork**: 
    ```sh
    git push origin feature/your-feature-name
    ```
6. **Create a Pull Request**: Submit your pull request on the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Replace the placeholders with your actual image paths and repository URL. This README provides a comprehensive guide for setting up and running the application, as well as contributing to the project.