

# Bliss Application README

This README provides step-by-step instructions on how to set up and run a Django application on both Windows and Linux systems. We'll cover installing `pip`, setting up a virtual environment, installing dependencies from `requirements.txt`, and running the Django app.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python 3.x
- `pip` (Python package installer)

## Step 1: Install `pip`

### Windows

1. Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer.
2. Open a command prompt and navigate to the folder containing `get-pip.py`.
3. Run the following command to install `pip`:

   ```
   python3 get-pip.py
   ```

### Linux

1. Open a terminal.
2. Run the following command to update package lists:

   ```
   sudo apt update
   ```

3. Install `pip` using the following command:

   ```
   sudo apt install python3-pip
   ```

## Step 2: Set Up a Virtual Environment

### Windows and Linux

1. Open a terminal (Command Prompt on Windows or a terminal on Linux).
2. Navigate to the directory where you want to create your Django project.
3. Run the following command to create a virtual environment (replace `myenv` with your preferred name):

   ```
   python -m venv myenv
   ```

4. Activate the virtual environment:

   **Windows:**

   ```
   myenv\Scripts\activate
   ```

   **Linux:**

   ```
   source myenv/bin/activate
   ```

## Step 3: Install Dependencies and Run the App

1. With the virtual environment active, navigate to the project directory and install the dependencies from `requirements.txt`:

   ```
   pip install -r requirements.txt
   ```

2. Create a new Django project:

   ```
   django-admin startproject myproject
   ```

   This will create a directory named `myproject` containing the initial project files.

3. Navigate into the project directory:

   ```
   cd myproject
   ```

4. Run database migrations:

   ```
   python manage.py migrate
   ```

5. Create a superuser (admin account) to access the Django admin panel:

   ```
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```

   The server will start, and you can access your Django app by opening a web browser and navigating to `http://127.0.0.1:8000/`.

7. Access the admin panel by going to `http://127.0.0.1:8000/admin/` and logging in with the superuser credentials you created earlier.

## Shutting Down

To stop the development server, press `Ctrl + C` in the terminal where the server is running. To deactivate the virtual environment, simply run:

```
deactivate
```

This concludes the setup process for running a Django application on both Windows and Linux systems. You can now start building your Django project within the virtual environment.