from flask import url_for, render_template, request, redirect
from models import Project, db, app
import datetime


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/projects/new', methods=['GET', 'POST'])
def add():
    if request.form:
        new_project = Project(
            title=request.form['title'], 
            date=datetime.datetime.strptime(request.form['date'], "%d/%m/%Y"), 
            description=request.form['description'], 
            skills=request.form['skills-list'], 
            link=request.form['github']
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')

@app.route('/projects/<id>')
def view(id):
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project)

@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get_or_404(id)
    if request.form:
        project.title=request.form['title']
        project.date=datetime.datetime.strptime(request.form['date'], "%d/%m/%Y")
        project.description=request.form['description']
        project.skills=request.form['skills-list']
        project.link=request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editform.html', project=project)

@app.route('/projects/<id>/delete')
def delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/projects/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')