from flask import url_for, render_template, request, redirect
from models import Project, db, app
import datetime


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/projects/new', methods=['GET', 'POST'])
def add():
    projects = Project.query.all()
    if request.form:
        new_project = Project(
            title=request.form['title'], 
            date=datetime.datetime.strptime(request.form['date'], "%Y-%m"), 
            description=request.form['desc'], 
            skills=request.form['skills'], 
            link=request.form['github']
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)

@app.route('/projects/<id>')
def view(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project, projects=projects)

@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        project.title=request.form['title']
        project.date=datetime.datetime.strptime(request.form['date'], "%Y-%m")
        project.description=request.form['desc']
        project.skills=request.form['skills']
        project.link=request.form['github']
        db.session.commit()
        return redirect(url_for('view', id=project.id))
    return render_template('editform.html', project=project, projects=projects)

@app.route('/projects/<id>/delete')
def delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/projects/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')