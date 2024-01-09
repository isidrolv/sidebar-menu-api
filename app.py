
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'S3cret!123.456'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/v1/helloWorld', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/v1/healthCheck', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def health_check():
    return {'status': 'UP', 'message': 'This guy is healthy!'}


@app.route('/api/v1/menu', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def menu():
    return [ # Dummy data for the beginning
        {"id": 1, "name": 'Home', "icon": 'home', "isRoot": "true", "hasChildren": "false", "route": '/home',
         "parentId": None},
        {"id": 2, "name": 'About', "icon": 'info', "isRoot": "true", "hasChildren": "false", "route": '/about',
         "parentId": None},
        {"id": 3, "name": 'Dashboard', "icon": 'contact_mail', "isRoot": "true", "route": '/dashboard',
         "parentId": None},
        {"id": 4, "name": 'Lazy', "icon": 'contact_mail', "isRoot": "true", "hasChildren": "true", "route": '/lazy',
         "parentId": None},
        {"id": 41, "name": 'Lazy Home', "icon": 'home', "isRoot": "true", "hasChildren": "false", "route": '/lazyHome',
         "parentId": 4},
        {"id": 42, "name": 'Lazy About', "icon": 'info', "isRoot": "true", "hasChildren": "false", "route": '/lazyAbout',
         "parentId": 4},
        {"id": 5, "name": 'Contact', "icon": 'contact_mail', "isRoot": "true", "route": '/contact', "parentId": None},
        {"id": 6, "name": 'Clients', "icon": 'person', "isRoot": "true", "route": '/client', "hasChildren": "true",
         "parentId": None},
        {"id": 61, "name": 'Client Home', "icon": 'home', "isRoot": "true", "hasChildren": "true", "route": '/clientHome',
         "parentId": 6},
        {"id": 611, "name": 'Client Perdonal Info', "icon": 'home', "isRoot": "true", "hasChildren": "false", "route": '/clientPersonalInfo',
         "parentId": 61},
        {"id": 612, "name": 'Client details', "icon": 'info', "isRoot": "true", "hasChildren": "true",
         "route": '/clientDetails', "parentId": 61},
        {"id": 6121, "name": 'Client Details home', "icon": 'home', "isRoot": "true", "hasChildren": "false",
         "route": '/clientDetailsHome', "parentId": 612},
        {"id": 6122, "name": 'Client Details Hobbies', "icon": 'info', "isRoot": "true", "hasChildren": "false",
         "route": '/clientDetailsHobbies', "parentId": 612},
        {"id": 62, "name": 'Client Professional Info', "icon": 'info', "isRoot": "true", "hasChildren": "false", "route": '/clientProfessionalInfo',
         "parentId": 6},
        {"id": 7, "name": 'Products', "icon": 'shopping_cart', "isRoot": "true", "route": '/product', "hasChildren": "true", "parentId": None},
        {"id": 71, "name": 'Product Home', "icon": 'home', "isRoot": "true", "hasChildren": "false", "route": '/productHome', "parentId": 7},
        {"id": 72, "name": 'Product Details', "icon": 'info', "isRoot": "true", "hasChildren": "false", "route": '/productDetails', "parentId": 7},
    ]


if __name__ == '__main__':
    app.run()
