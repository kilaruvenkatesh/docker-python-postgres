import time
import psycopg2

# Wait for PostgreSQL to be ready
time.sleep(5)

try:
    conn = psycopg2.connect(
        host="my-postgres",
        database="mydb",
        user="user",
        password="pass",
        port=5432
    )
    cur = conn.cursor()

    # Create a table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS demo (
            id SERIAL PRIMARY KEY,
            message TEXT
        );
    """)
    conn.commit()

    # Insert one row
    cur.execute("INSERT INTO demo (message) VALUES ('Hello this venkatesh from PostgreSQL!') RETURNING id;")
    row_id = cur.fetchone()[0]
    conn.commit()

    # Read and print the row
    cur.execute("SELECT * FROM demo;")
    rows = cur.fetchall()

    print("Inserted Row ID:", row_id)
    print("Rows:", rows)

    cur.close()
    conn.close()

except Exception as e:
    print("Connection failed:", e)
