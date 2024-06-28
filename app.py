from flask import Flask, request, jsonify, session, make_response, render_template
from static import info


app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')



def used_tech():
    used_tech = []
    for tech in info.technologies.keys():
        if tech in info.exceptions:
            continue
        used_tech.append(tech)
    return used_tech



@app.route('/')
def home():
    return render_template('home.html', data=info.technologies, page='home')



@app.route('/projects')
def projects():
    used = used_tech()
    return render_template('projects.html', 
                           data=info.projects, 
                           tag='All', 
                           page='projects', 
                           used_tech=used)



@app.route('/filter/<current_tech>', methods=['POST'])
def button_click(current_tech):
    used = used_tech()   
    filtered_projects_ls = []
    for project in info.projects:
        if current_tech in project['technologies']:
            filtered_projects_ls.append(project)
    return render_template('projects.html', 
                           data=filtered_projects_ls, 
                           tag=current_tech, 
                           page='projects', 
                           used_tech=used)



@app.route('/experience')
def experience():
    return render_template('experience.html', data=info.experience, page='experience')



@app.route('/contacts')
def contacts():
    return render_template('contacts.html', page='contacts')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


# pip3 freeze > requirements.txt
# debug=False след деплоиване