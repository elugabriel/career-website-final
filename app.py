from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Lagos, Nigeria",
        "Salary": "#160,000"
    },

    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Remote",
        "Salary": "$10,000"
    },

    {
        "id": 3,
        "title": "Frontend Engineer",
        "location": "Delhi, India",
        "Salary": "Rs40,000"
    },

    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "San Franscisco, USA",
        "Salary": "$110,000"
    },
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs = JOBS)

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)