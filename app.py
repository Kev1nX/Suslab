from flask import Flask, render_template, jsonify, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host='kevinxia.mysql.pythonanywhere-services.com',
    user='kevinxia',
    password='SUSlabDBadmin',
    database='kevinxia$default'
)
cursor = db.cursor(dictionary=True)

# Index route
@app.route('/')
def index():
    db = mysql.connector.connect(
        host='kevinxia.mysql.pythonanywhere-services.com',
        user='kevinxia',
        password='SUSlabDBadmin',
        database='kevinxia$default'
    )
    cursor = db.cursor(dictionary=True)
    return render_template('index.html')

@app.route('/student')
def student():
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('student', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    db.commit()
    return render_template('student.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/task1')
def task1():
    return render_template('task1.html')

@app.route('/task2')
def task2():
    return render_template('task2.html')

@app.route('/task3')
def task3():
    return render_template('task3.html')

@app.route('/get-access-counts')
def get_access_counts():
    cursor.execute("SELECT page_name, view_count FROM page_views;")
    results = cursor.fetchall()
    return jsonify(results)


@app.route('/increment-task1-view', methods=['POST'])
def increment_task1_view():
    # Database update logic to increment the view count
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('task1', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    db.commit()
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('CNC', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    db.commit()
    return redirect(url_for('task2'))  # Assuming 'task2' is the endpoint for the next task page

@app.route('/increment-task2-view', methods=['POST'])
def increment_task2_view():
    # Database update logic to increment the view count
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('task2', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    db.commit()
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('3Dprint', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    db.commit()
    return redirect(url_for('task3'))  # Assuming 'task2' is the endpoint for the next task page

@app.route('/increment-task3-view', methods=['POST'])
def increment_task3_view():
    # Database update logic to increment the view count
    cursor.execute("INSERT INTO page_views (page_name, view_count) VALUES ('task3', 1) ON DUPLICATE KEY UPDATE view_count = view_count + 1")
    db.commit()
    return redirect(url_for('student'))  # Assuming 'task2' is the endpoint for the next task page

if __name__ == '__main__':
    app.run(debug=True)