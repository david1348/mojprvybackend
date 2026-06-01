import psycopg2

databaza = {
    "students": [
        {"id": 1, "name": "Adrián", "surname": "Červenka", "nickname": "ChillyHotPpr"},
        {"id": 2, "name": "Karolína", "surname": "Kmeťová", "nickname": "null"},
        {"id": 3, "name": "Matej", "surname": "R", "nickname": "T-34"},
        {"id": 4, "name": "Milan", "surname": "K", "nickname": "Lopta"},
        {"id": 5, "name": "Dávid", "surname": "Š", "nickname": "DVD"},
    ]
}

with psycopg2.connect(
    host="dpg-d7ng4fe7r5hc73aqr48g-a.frankfurt-postgres.render.com",
    database="trieda",
    user="trieda_user",
    password="CU76wt1voH4NyVoSvtaSeeyJyRKloMoN",
    port=5432
) as conn:
    with conn.cursor() as cur:

        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                surname TEXT,
                nickname TEXT
            );
        """)

        for student in databaza["students"]:
            nickname = student["nickname"]

            if nickname == "null":
                nickname = None

            cur.execute("""
                INSERT INTO students (id, name, surname, nickname)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """, (
                student["id"],
                student["name"] or None,
                student["surname"] or None,
                nickname
            ))

        print("Table ready and data inserted.")