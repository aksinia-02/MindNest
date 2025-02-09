import psycopg2
from psycopg2 import errors


def save_user_in_database(user_name, hashed_password):
    """Inserts user details into the database, avoiding SQL injection vulnerabilities."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="postgres",
            user="postgres",
            password="flower16",
            port="5435"
        )
        cur = conn.cursor()

        # Ensure the user table exists
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) UNIQUE NOT NULL,
                password TEXT NOT NULL
            );
        """)

        # Insert user safely using parameterized queries
        cur.execute("""
            INSERT INTO users (name, password) VALUES (%s, %s)
            RETURNING id;
        """, (user_name, hashed_password))

        conn.commit()
        cur.close()
        return {"success": True, "message": "User registered successfully"}

    except errors.UniqueViolation:
        print("Error saving user:", errors.UniqueViolation)
        return {"success": False, "message": "Error: Username already exists"}

    except Exception as e:
        print("Error saving user:", e)
        return {"success": False, "message": f"Error saving user: {e}"}
    finally:
        conn.close()


def get_password_from_database(user_name):
    """Retrieves the stored hashed password for the given username."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="postgres",
            user="postgres",
            password="flower16",
            port="5435"
        )
        cur = conn.cursor()

        cur.execute("SELECT password FROM users WHERE name = %s;", (user_name,))
        result = cur.fetchone()

        cur.close()
        return result[0] if result else None  # Return hashed password or None
    except Exception as e:
        print("Error retrieving password:", e)
        return None
    finally:
        conn.close()


def save_current_session_in_database(user_name):
    """Inserts user details into the database, avoiding SQL injection vulnerabilities."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="postgres",
            user="postgres",
            password="flower16",
            port="5435"
        )
        cur = conn.cursor()

        # Ensure the user table exists
        cur.execute("""
            CREATE TABLE IF NOT EXISTS current_session (
                id PRIMARY KEY,
                name VARCHAR(255) UNIQUE NOT NULL
            );
        """)

        cur.execute("""
            INSERT INTO current_session (username) VALUES (%s)
            ON CONFLICT (id) DO UPDATE SET username = EXCLUDED.username;
        """, (user_name,))

        conn.commit()
        cur.close()
    except Exception as e:
        print("Error saving user:", e)
    finally:
        conn.close()


def new_user():

    """Returns True if no user is currently logged in (empty current_session table),
    False if the table doesn't exist or any error occurs."""

    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="postgres",
            user="postgres",
            password="flower16",
            port="5435"
        )
        cur = conn.cursor()

        # Check if the table exists and get the count of entries
        try:
            cur.execute("SELECT COUNT(*) FROM current_session;")
            result = cur.fetchone()
            cur.close()
            return result[0] == 0
        except errors.UndefinedTable:  # Handle if the table doesn't exist
            print("Error: The 'current_session' table does not exist.")
            return False
    except Exception as e:
        print("Error checking new user status:", e)
        return False
    finally:
        if conn:
            conn.close()
