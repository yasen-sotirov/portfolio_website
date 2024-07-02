from flask import Flask, request, jsonify, session, make_response, render_template

technologies = {
    "Python": [
        "CORE: variables, scope, functions, loop, linear data structures, conditional, debugging, errors handling, file handling;",
        "DSA: linked list, hash table, stack, queue, tree, complexity, searching and sorting algorithms, recursion;",
        "OOP: class, object, methods, comprehensions, lambda, inheritance, encapsulation, polymorphism, composition, SOLID, data hiding;",
        "WEB: API, database, SQL, MVC, authentication, authorization, dependency injection;",
    ],
    "JavaScript": [  
        "CORE: variables, data types, operators, conditionals, scope, loops, functions, common methods, scope, DOM manipulation, event handling, basic debugging;"
    ],
    "HTML" :[
        "BASICS: structure, tags, attributes, lists (+ nested), tables, forms, basics meta tags;",
    ],
    "CSS": [
        "BASICS: selectors, properties, box model, styling text, basic layout, simple transitions;",
        "INTERMEDIATE: pseudo-classes/elements, positioning, flexbox;",
    ],      
    "Flask": [
        "BASICS: structure, basic routing (path query), request / response models pydantic, HTTP methods;",
    ],      
    "PostgreSQL": [
        "BASICS: basic SQL commands/querying (incl. join, union), data types, creating and managing databases/tables, relations, functions;",
    ],      
    "Linux": [
        "My personal computer runs on Linux;",
    ],

}


projects = [
    {
    "name": "Portfolio website",
    "start date": "2024-06-22",
    "start month": "05",
    "start year": "2024",
    "end date": "2024-06-25",
    "end month": "06",
    "end year": "2024",
    "description": "Dynamic portfolio website with four pages",
    "technologies": ["Python", "Flask", "HTML", "TailwindCSS"],
    "readme": "https://github.com/yasen-sotirov/portfolio_website/blob/master/README.md",
    "source code": "https://github.com/yasen-sotirov/personal_projects/tree/main/portfolio_website_2.0",  
    },
    {  
    "name": "To Do List App",
    "start date": "2024-06-14",
    "start month": "06",
    "start year": "2024",
    "end date": "2024-06-15",
    "end month": "06",
    "end year": "2024",
    "description": "Weather App: Check the weather, humidity, and wind speed for any city worldwide. Data is provided by www.openweathermap.org",
    "technologies": ["JavaScript", "HTML", "CSS"],
    "readme": "https://github.com/yasen-sotirov/todo_list/blob/main/README.md",
    "source code": "https://github.com/yasen-sotirov/todo_list",
    "run code": "https://yasen-sotirov.github.io/todo_list/"
    },
    {  
    "name": "Weather Forecast App",
    "start date": "2024-06-04",
    "start month": "06",
    "start year": "2024",
    "end date": "2024-06-05",
    "end month": "06",
    "end year": "2024",
    "description": "Weather App: Check the weather, humidity, and wind speed for any city worldwide. Data is provided by www.openweathermap.org",
    "technologies": ["JavaScript", "HTML", "CSS"],
    "readme": "https://github.com/yasen-sotirov/weather_forecast/blob/main/README.md",
    "source code": "https://github.com/yasen-sotirov/weather_forecast",
    "run code": "https://yasen-sotirov.github.io/weather_forecast/"
    },
    {
    "name": "Roll The Dice Game",
    "start date": "2024-05-16",
    "start month": "05",
    "start year": "2024",
    "end date": "2024-05-17",
    "end month": "05",
    "end year": "2024",
    "description": '''Roll the dice and add each roll to your total. 
        Stop anytime to bank your points, because if you roll a 1,
        you loos your points, and the next player goes. First to reach 100
        points wins.''',
    "technologies": ["JavaScript", "HTML", "CSS"],
    "readme": "https://github.com/yasen-sotirov/roll_the_dice_game/blob/master/README.md",
    "source code": "https://github.com/yasen-sotirov/roll_the_dice_game",
    "run code": "https://yasen-sotirov.github.io/roll_the_dice_game/",
    },
    {
    "name": "Guess the number",
    "start date": "2024-05-15",
    "start month": "05",
    "start year": "2024",
    "end date": "2024-05-16",
    "end month": "05",
    "end year": "2024",
    "description": "Uncover the secret number (1-100) within 10 attempts.",
    "technologies": ["JavaScript", "HTML", "CSS"],
    "readme": "https://github.com/yasen-sotirov/guess_the_number/blob/main/README.md",
    "source code": "https://github.com/yasen-sotirov/guess_the_number",
    "run code": "https://yasen-sotirov.github.io/guess_the_number/",
    },
    {
    "name": "Match Score",
    "start date": "2023-11-02",
    "start month": "11",
    "start year": "2023",
    "end date": "2023-11-20",
    "end month": "11",
    "end year": "2023",
    "description": "Solution that streamline the organization and management of sport events. Implemented features for one-on-one matches and tournaments. Intensive work in a group of three with a horizontal hierarchy.",
    "technologies": ["Python", "FastAPI", "MariaDB", "SQL", "Pydantic"],
    "readme": "https://github.com/yasen-sotirov/match_score/blob/main/README.md",
    "source code": "https://github.com/yasen-sotirov/match_score",
    },
    {
    "name": "Forum app",
    "start date": "2023-10-07",
    "start month": "10",
    "start year": "2023",
    "end date": "2023-10-20",
    "end month": "10",
    "end year": "2023",
    "description": "Design and implementation of a forum system. Providing a RESTfull API for use by various clients.",
    "technologies": ["Python", "FastAPI", "Pydantic"],
    "readme": "https://github.com/yasen-sotirov/forum_app/blob/main/README.md",
    "source code": "https://github.com/yasen-sotirov/forum_app",
    },
    {
    "name": "Logistics Fleet App",
    "start date": "2023-09-06",
    "start month": "09",
    "start year": "2023",
    "end date": "2023-09-18",
    "end month": "09",
    "end year": "2023",
    "description": "Designed and implemented a logistics console application for efficient management of package deliveries between hubs located in various cities. Intensive work in a group of three with a horizontal hierarchy",
    "technologies": ["Python", "FastAPI", "Pydantic"],
    "readme": "https://github.com/yasen-sotirov/logistic_fleet/blob/main/README.md",
    "source code": "https://github.com/yasen-sotirov/logistic_fleet",
    }
]

experience = [
{
    "title": "Architect",
    "start date": "2016-08-01",
    "start month": "08",
    "start year": "2016",
    "end date": "2023-06-01",
    "end month": "06",
    "end year": "2023",
    "description": "Architectural design and building renovation. Experienced with public procurement and collaborating with clients, engineers, and construction teams.",
    "bullets": [
    "Leading a team of 5 engineers.",
    "Fully completed projects - 43.",
    "Mentoring 3 interns.",
    "Weekly communication with clients.",
    "Contribution: Implementing automated systems and processes reducing time by up to 70%.",
    ]
},

]

exceptions = ["Linux", "PostgreSQL", ]



app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')



def used_tech():
    used_tech = []
    for tech in technologies.keys():
        if tech in exceptions:
            continue
        used_tech.append(tech)
    return used_tech



@app.route('/')
def home():
    return render_template('home.html', data=technologies, page='home')



@app.route('/projects')
def projects():
    used = used_tech()
    return render_template('projects.html', 
                           data=projects, 
                           tag='All', 
                           page='projects', 
                           used_tech=used)



@app.route('/filter/<current_tech>', methods=['POST'])
def button_click(current_tech):
    used = used_tech()   
    filtered_projects_ls = []
    for project in projects:
        if current_tech in project['technologies']:
            filtered_projects_ls.append(project)
    return render_template('projects.html', 
                           data=filtered_projects_ls, 
                           tag=current_tech, 
                           page='projects', 
                           used_tech=used)



@app.route('/experience')
def experience():
    return render_template('experience.html', data=experience, page='experience')



@app.route('/contacts')
def contacts():
    return render_template('contacts.html', page='contacts')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


# pip3 freeze > requirements.txt
# debug=False след деплоиване