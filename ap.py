
import psycopg2
from flask import Flask, jsonify
# novy db_connection + obrazok
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
    host="dpg-d7ng4fe7r5hc73aqr48g-a.frankfurt-postgres.render.com",
    database="trieda",
    user="trieda_user",
    password="CU76wt1voH4NyVoSvtaSeeyJyRKloMoN",
    port=5432)
    return conn

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
            "surname": "R",
            "nickname": "T-34",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Tank_T-34.JPG/1280px-Tank_T-34.JPG"
        },
        {
            "id": 4,
            "name": "Milan",
            "surname": "K",
            "nickname": "Lopta",
            "image": "https://www.tonerpartner.sk/userdata/products/2612/8d-545-684c34d5b985c.jpg"
        },
        {
            "id": 5,
            "name": "Dávid",
            "surname": "Š",
            "nickname": "DVD",
            "image": "https://i.pinimg.com/736x/c2/40/5b/c2405bf0cff40535767200dccc6bf589.jpg"
        }
    ]
}

@app.route('/api')
def api():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    students = []
    for row in rows:
        students.append({
            "id": row[0],
            "name": row[1],
            "surname": row[2],
            "nickname": row[3],
        })

    cur.close()
    conn.close()

    return jsonify({"students": students})

@app.route('/api/student/<int:student_id>')
def find_student(student_id):
    student = databaza["students"][student_id - 1]
    return jsonify(student)

if __name__ == "__main__":
    app.run(debug=True)
