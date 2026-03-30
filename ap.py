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
            "nickame": "DVD"
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
    return jsonify(databaza)

@app.route('/api/student/<int:student_id>')
def find_student(student_id):
    student = databaza["students"][student_id - 1]
    return jsonify(student)

if __name__ == "__main__":
    app.run(debug=True)