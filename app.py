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
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('student', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    db.commit()
    return render_template('student.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/student/task1')
def task1():
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('task1', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    db.commit()
    return render_template('task1.html')

@app.route('/student/task2')
def task2():
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('task2', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    db.commit()
    return render_template('task2.html')

@app.route('/student/task3')
def task3():
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('task3', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    db.commit()
    return render_template('task3.html')

if __name__ == '__main__':
    app.run(debug=True)