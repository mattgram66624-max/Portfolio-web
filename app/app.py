from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For flash messages

# Sample project data
projects = [
    {
        'title': 'E-commerce Platform',
        'description': 'A full-stack online store built with React and Node.js.',
        'tech': 'React, Node.js, MongoDB',
        'link': '#',
        'image': 'project1.jpg'
    },
    {
        'title': 'Task Management App',
        'description': 'A collaborative tool for managing projects and tasks.',
        'tech': 'Vue.js, Express, PostgreSQL',
        'link': '#',
        'image': 'project2.jpg'
    },
    {
        'title': 'Portfolio Website',
        'description': 'This very website! Responsive portfolio with Flask backend.',
        'tech': 'HTML, CSS, Flask, Python',
        'link': '#',
        'image': 'project3.jpg'
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # In real app, send email or save to DB
        flash(f'Thank you {name}! Your message has been received.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html') 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
