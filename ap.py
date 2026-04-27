import psycopg2

databaza = {
    "students": [
        {"id": 1, "name": "Adrián", "surname": "Červenka", "nickname": "ChillyHotPpr"},
        {"id": 2, "name": "Karolína", "surname": "Kmeťová", "nickname": "null"},
        {"id": 3, "name": "Matej", "surname": "R", "nickname": "T-34"},
        {"id": 4, "name": "Milan", "surname": "K", "nickname": "Lopta"},
        {"id": 5, "name": "Dávid", "surname": "Š", "nickname": "DVD"},
        # ... rest of your data
    ]
}

conn = psycopg2.connect(
    host="localhost",
    database="your_db",
    user="your_user",
    password="your_password",
    port=5432
)

cur = conn.cursor()

for student in databaza["students"]:
    cur.execute(
        """
        INSERT INTO students (id, name, surname, nickname)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
        """,
        (
            student["id"],
            student["name"],
            student["surname"],
            student["nicnkame"] 
        )
    )

conn.commit()
cur.close()
conn.close()
