import os
import sys

here = os.path.dirname(__file__)

sys.path.append(os.path.join(here, '..'))

from flask import Flask, render_template
from data import info



app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')


# FUNCTIONS
# def used_tech():
#     used_tech = []
#     for tech in info.soft_data.keys():
#         if tech in info.exceptions:
#             continue
#         used_tech.append(tech)
#     return used_tech



# ROUTERS
# HOME
@app.route('/')
def home():
    return render_template('home.html', tech_data=info.tech_data, soft_data=info.soft_data, page='home')


# PROJECTS
@app.route('/projects')
def projects():
    # used = used_tech()
    used = info.filters
    return render_template('projects.html', 
                           data=info.projects, 
                           tag='All', 
                           page='projects', 
                           used_tech=used)


# FILTER TECHNOLOGIES
@app.route('/filter/<current_tech>', methods=['POST'])
def button_filter(current_tech):
    # used = used_tech()  
    used = info.filters 
    filtered_projects_ls = []
    for project in info.projects:
        if current_tech in project['technologies']:
            filtered_projects_ls.append(project)
    return render_template('projects.html', 
                           data=filtered_projects_ls, 
                           tag=current_tech, 
                           page='projects', 
                           used_tech=used)


# PROJECT COMPLEXITY
@app.route('/complexity/<comp_tag>', methods=['POST'])
def button_complexity(comp_tag):
    # used = used_tech() 
    used = info.filters
    filtered_projects_ls = []
    for project in info.projects:
        if comp_tag == project['complexity']:
            filtered_projects_ls.append(project)

    return render_template('projects.html', 
                           data=filtered_projects_ls, 
                           tag=comp_tag, 
                           page='projects', 
                           used_tech=used)


# EXPERIENCE
@app.route('/experience')
def experience():
    return render_template('experience.html', data=info.experience, page='experience')



# CONTACTS
@app.route('/contacts')
def contacts():
    return render_template('contacts.html', page='contacts')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

# Run on folder
# python index.py
# flask --app index run

# pip3 freeze > requirements.txt
# debug=False след деплоиване


