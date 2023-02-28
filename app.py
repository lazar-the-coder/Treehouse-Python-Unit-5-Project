from flask import url_for, render_template, request, redirect
from models import Project, db, app


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/projects/new', methods=['GET', 'POST'])
def new_proj():
    if request.form:
        new_project = Project(
            title=request.form['title'], 
            date=request.form['date'], 
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
        project.date=request.form['date']
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

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')