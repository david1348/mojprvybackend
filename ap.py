import psycopg2
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
# novy db_connection + obrazok
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.root_path, 'frontend.html')


def get_db_connection():
    conn = psycopg2.connect(
    host="dpg-d8labnugvqtc73anudp0-a.frankfurt-postgres.render.com",
    database="mytestingpostgres",
    user="trieda_user2",
    password="qjvfZJDGjS7o7skk06qVoBOfeBHQnMiv",
    port=5432)
    return conn


def row_to_student(row):
    return {
        "id": row[0],
        "name": row[1],
        "surname": row[2],
        "nickname": row[3],
        "image": row[4]
    }


def init_db():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                surname TEXT,
                nickname TEXT,
                image TEXT
            );
        """)

        cur.executemany("""
            INSERT INTO students (id, name, surname, nickname, image)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE SET
                name = EXCLUDED.name,
                surname = EXCLUDED.surname,
                nickname = EXCLUDED.nickname,
                image = EXCLUDED.image;
        """, [
            (
                student["id"],
                student["name"],
                student["surname"],
                student["nickname"],
                student["image"]
            )
            for student in databaza["students"]
        ])

        conn.commit()
    conn.close()


databaza = {
    "students": [
        {
            "id": 1,
            "name": "Adrián",
            "surname": "Červenka",
            "nickname": "ChillyHotPpr",
            "image": "https://store.supercell.com/_next/static/media/bs_store_preview_cta_figure.3699673f.png"
        },
        {
            "id": 2,
            "name": "Karolína",
            "surname": "Kmeťová",
            "nickname": None,
            "image": "https://sk-cars.pl/media/cache/17/6c/176c34752e75dfdb6e2f7219f2256ebd.jpg"
        },
        {
            "id": 3,
            "name": "Matej",
            "surname": "Randziak",
            "nickname": "T-34",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Tank_T-34.JPG/1280px-Tank_T-34.JPG"
        },
        {
            "id": 4,
            "name": "Milan",
            "surname": "Kokina",
            "nickname": "Lopta",
            "image": "https://www.tonerpartner.sk/userdata/products/2612/8d-545-684c34d5b985c.jpg"
        },
        {
            "id": 5,
            "name": "Dávid",
            "surname": "Škula",
            "nickname": "DVD",
            "image": "https://i.pinimg.com/736x/c2/40/5b/c2405bf0cff40535767200dccc6bf589.jpg"
        },
        {
            "id": 6,
            "name": "Janka",
            "surname": "Vargová",
            "nickname": "Gojo",
            "image": "https://y0uc4n7kn0w.com/wp-content/uploads/2021/06/gojo-4.png?w=668"
        },
        {
            "id": 7,
            "name": "Martin",
            "surname": "Deglovič",
            "nickname": "BMW",
            "image": "https://www.bmwgroup-classic.com/content/dam/grpw/websites/bmwgroup-classic_com/productcatalog2/images_pc/AF-11846-2.png/jcr:content/renditions/original"
        },
        {
            "id": 8,
            "name": "Samuel",
            "surname": "Uhrík",
            "nickname": "Pro",
            "image": "https://www.prosettings.gg/wp-content/uploads/2022/08/XANTARES-cs2-player-profile-picture-aurora-286x300.webp"
        },
        {
            "id": 9,
            "name": "Samo",
            "surname": "Martiš",
            "nickname": "Lampa",
            "image": "https://www.svet-svietidiel.sk/brilagi-led-stmievatelna-stolna-lampa-s-displejom-pelle-led-7w-230v-biela-img-bg0503-fd-2.webp"
        },
        {
            "id": 10,
            "name": "Rasťo",
            "surname": "Paták",
            "nickname": "Gotham",
            "image": "https://i.scdn.co/image/ab67616d0000b2734de7b41d063bd502bf3cedec"
        }
    ]
}

@app.route('/api')
def api():
    sort_by = request.args.get("sort_by", "id")
    order = request.args.get("order", "asc").lower()

    allowed_sort = {"id", "name", "surname", "nickname"}
    if sort_by not in allowed_sort:
        sort_by = "id"

    if order not in {"asc", "desc"}:
        order = "asc"

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(f"""
        SELECT id, name, surname, nickname, image
        FROM students
        ORDER BY {sort_by} {order.upper()}
    """)

    rows = cur.fetchall()
    cur.close()
    conn.close()

    students = [row_to_student(row) for row in rows]

    return jsonify({"students": students})

@app.route('/api/student/<int:student_id>')
def find_student(student_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, name, surname, nickname, image
        FROM students
        WHERE id = %s
    """, (student_id,))

    row = cur.fetchone()
    cur.close()
    conn.close()

    if row is None:
        return jsonify({"error": "Student not found"}), 404

    student = row_to_student(row)

    return jsonify(student)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

