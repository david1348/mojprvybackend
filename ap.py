from flask import Flask, jsonify, request

app = Flask(__name__)

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
            "nicnkame": "ChillyHotPpr"
        },
        {
            "id": 2,
            "name": "Karolína",
            "surname": "Kmeťová",
            "nickname": "null"
        },
        {
            "id": 3,
            "name": "Matej",
            "surname": "R",
            "nickname": "T-34"
        },
        {  
            "id": 4,
            "name": "Milan",
            "surname": "K",
            "nickname": "Lopta"
        },
        {
            "id": 5,
            "name": "Dávid",
            "surname": "Š",
            "nickname": "DVD"
        },
        {
            "id": 6,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {  
            "id": 7,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {
            "id": 8,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {
            "id": 9,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {  
            "id": 10,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {
            "id": 11,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {
            "id": 12,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {  
            "id": 13,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {  
            "id": 14,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {
            "id": 15,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {
            "id": 16,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {  
            "id": 17,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {  
            "id": 18,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {
            "id": 19,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        {
            "id": 20,
            "name": "",
            "surname": "",
            "nickname": ""
        },
        
    ]
}

@app.route('/api')
def api():
    return jsonify(databaza)

@app.route('/api/student/<int:student_id>')
def find_student(student_id):
    student = databaza["students"][student_id - 1]
    return jsonify(student)

if __name__ == "__main__":
    app.run(debug=True)
