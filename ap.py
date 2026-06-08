from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# test route
@app.route('/')
def home():
    return "Vitajte!"

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

# GET ALL STUDENTS
@app.route('/api')
def api():
    return jsonify(databaza)

# GET ONE STUDENT (SAFE VERSION)
@app.route('/api/student/<int:student_id>')
def find_student(student_id):
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
