This project is for practising database management with ORM using SQLAlchemy

## Database Setup

This project uses MySQL and is tailored for Windows. Follow these steps to set up the database:

0. Use a Windows machine

1. **Install MySQL:**
    * Download and install the MySQL Community Server from [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/).

2. **Create a Database:**
    * Log in to the MySQL server:
        ```bash
        mysql -u root -p  # You'll be prompted for the root password
        ```
    * Create the database:
        ```sql
        CREATE DATABASE my_project_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;  # Important: Specify character set!
        GRANT ALL PRIVILEGES ON my_project_db.* TO 'myuser'@'localhost' IDENTIFIED BY 'mypassword';  # Create user and grant privileges
        FLUSH PRIVILEGES;  # Apply the changes
        EXIT;  # Exit the MySQL client
        ```
        * Replace `my_project_db` with your database name, `myuser` with the username you want to use, and `mypassword` with a strong unique password.  
        **Warning:**  Do *not* use these logins details in a real application! Make better choices..

3. **Set Up Environment Variables:**
    This project requires the `DATABASE_URL` environment variable to be set.
    
    Keep it simple, just use `set` command in the command prompt:
    ```
    set DATABASE_URL="mysql+mysqlconnector://myuser:mypassword@localhost:3306/my_project_db"
    ```
    * Replace `DATABASE_URL` with your database link, using the same unique credentials from creating the database.

4. **Configure Alembic:**

    * **Copy the template:** Copy the `alembic.ini.template` file to `alembic.ini`:
        ```bash
        cp alembic.ini.template alembic.ini
        ```

    * **Set the DATABASE_URL environment variable:**  You must set the `DATABASE_URL` environment variable.  This is how Alembic will know how to connect to your database.  

    ```
    set DATABASE_URL="mysql+mysqlconnector://myuser:mypassword@localhost:3306/my_project_db"
    ```

5. **Install required libraries:** 
    *Run a bash command "pip install -r requirements.txt" in your virtual environment or manually install any needed libraries from "requirements.txt"

    ```bash
    python run.py
    ```
    *manually install any needed libraries from "requirements.txt"

6. **Initialise Migrations:**
    ```bash
    alembic upgrade head
    ```

7. **Run the program:**
    ```bash
    python run.py
    ```

8. **Manage your own library system**

## To-Do List ✅

- [ ] Initialise migrations 
    * Setup models
    *Setup inits
    *Setup db connections
- [ ] Sort out the structure
- [ ] Migrate from using .json for storage to using a DB
- [ ] ~~Write a nicer~~  Update readme with instructions and pretty pictures

## Would-Be-Nice List ✅
- [ ] Add a nicer UI
- [ ] Make an adroid version
- [ ] Give an option to add a book from image (use google books API maybe)
