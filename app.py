from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host='kevinxia.mysql.pythonanywhere-services.com',
    user='kevinxia',
    password='SUSlabDBadmin',
    database='kevinxia$default'
)
cursor = db.cursor()
views = {
    "student": 0,
    "task1":0,
    "task2":0    
}

# Index route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student')
def student():
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('your-page', 1)")
    db.commit()
    return render_template('student.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)