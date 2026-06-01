import os
import psycopg2
from flask import Flask, jsonify

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
            "nickame": "ChillyHotPpr"
        },
        {
            "id": 2,
            "name": "Karolína",
            "surname": "Kmeťová",
            "nickame": "null"
        },
        {
            "id": 3,
            "name": "Matej",
            "surname": "R",
            "nickame": "T-34"
        },
        {  
            "id": 4,
            "name": "Milan",
            "surname": "K",
            "nickame": "Lopta"
        },
        {
            "id": 5,
            "name": "Dávid",
            "surname": "Š",
            "nickame": "DVD",
            "image": "dvd.jpg"
        },
        {
            "id": 6,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {  
            "id": 7,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {
            "id": 8,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {
            "id": 9,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {  
            "id": 10,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {
            "id": 11,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {
            "id": 12,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {  
            "id": 13,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {  
            "id": 14,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {
            "id": 15,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {
            "id": 16,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {  
            "id": 17,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {  
            "id": 18,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {
            "id": 19,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        {
            "id": 20,
            "name": "",
            "surname": "",
            "nickame": ""
        },
        
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