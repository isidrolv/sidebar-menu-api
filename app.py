from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_swagger_ui import get_swaggerui_blueprint

# Swagger UI
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

# Call factory function to create our blueprint
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)

# Create an instance of our Flask app.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'S3cret!123.456'
app.config['CORS_HEADERS'] = 'Content-Type'
# Register blueprint at URL
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
# Enable CORS
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Database configuration
CREDS = 'isidrolv:7DpqCM9gJRPFCTbEOoWh0w'
URL = 'wan-shadow-1792.g8z.cockroachlabs.cloud'
DB_NAME = 'defaultdb'
app.config['COCKROACH_DB_URI'] = f'postgresql://{CREDS}@{URL}:26257/{DB_NAME}?sslmode=verify-full'


@app.route('/', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def index():
    return 'Welcome to Access API!'


# Define a handler for the /hello route, which
@app.route('/api/v1/helloWorld', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def hello_world():  # put application's code here
    return jsonify({"message": 'Hello World!', "status": 200})


# Define a handler for the /healthCheck route, which
@app.route('/api/v1/healthCheck', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def health_check():
    return {'status': 'UP', 'message': 'This guy is healthy!'}


# Define a handler for the /login route, which
@app.route('/api/v1/login', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print(request.get_json())
    if username == 'admin' and password == '4dm!n123.,':
        message = f'Login successful for {username}!'
        api_token = 'A1D2F3B4z5s6r7k8d9d0b'
        status = 'success'
    else:
        message = 'Login failed!'
        api_token = None
        status = 'failed'

    return jsonify({'userId': status, 'message': message, 'apiToken': api_token})


# Define a handler for the /menu route, which return the user menu based on the user role
@app.route('/api/v1/menu', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def menu():
    data = request.get_json()
    user_id = data['user_id']
    return [  # Dummy data for the beginning
        {"id": 1, "name": f'{user_id}->Home', "icon": 'home', "isRoot": "true", "hasChildren": "false", "route": '/home',
         "parentId": None},
        {"id": 2, "name": 'About', "icon": 'info', "isRoot": "true", "hasChildren": "false", "route": '/about',
         "parentId": None},
        {"id": 3, "name": 'Dashboard', "icon": 'contact_mail', "isRoot": "true", "route": '/dashboard',
         "parentId": None},
        {"id": 4, "name": 'Lazy', "icon": 'contact_mail', "isRoot": "true", "hasChildren": "true", "route": '/lazy',
         "parentId": None},
        {"id": 41, "name": 'Lazy Home', "icon": 'home', "isRoot": "true", "hasChildren": "false", "route": '/lazyHome',
         "parentId": 4},
        {"id": 42, "name": 'Lazy About', "icon": 'info', "isRoot": "true", "hasChildren": "false",
         "route": '/lazyAbout', "parentId": 4},
        {"id": 5, "name": 'Contact', "icon": 'contact_mail', "isRoot": "true", "route": '/contact', "parentId": None},
        {"id": 6, "name": 'Clients', "icon": 'person', "isRoot": "true", "route": '/client', "hasChildren": "true",
         "parentId": None},
        {"id": 61, "name": 'Client Home', "icon": 'home', "isRoot": "true", "hasChildren": "true",
         "route": '/clientHome',
         "parentId": 6},
        {"id": 611, "name": 'Client Personal Info', "icon": 'home', "isRoot": "true", "hasChildren": "false",
         "route": '/clientPersonalInfo',
         "parentId": 61},
        {"id": 612, "name": 'Client details', "icon": 'info', "isRoot": "true", "hasChildren": "true",
         "route": '/clientDetails', "parentId": 61},
        {"id": 6121, "name": 'Client Details home', "icon": 'home', "isRoot": "true", "hasChildren": "false",
         "route": '/clientDetailsHome', "parentId": 612},
        {"id": 6122, "name": 'Client Details Hobbies', "icon": 'info', "isRoot": "true", "hasChildren": "false",
         "route": '/clientDetailsHobbies', "parentId": 612},
        {"id": 62, "name": 'Client Professional Info', "icon": 'info', "isRoot": "true", "hasChildren": "false",
         "route": '/clientProfessionalInfo', "parentId": 6},
        {"id": 7, "name": 'Products', "icon": 'shopping_cart', "isRoot": "true", "route": '/product',
         "hasChildren": "true", "parentId": None},
        {"id": 71, "name": 'Product Home', "icon": 'home', "isRoot": "true", "hasChildren": "false",
         "route": '/productHome', "parentId": 7},
        {"id": 72, "name": 'Product Details', "icon": 'info', "isRoot": "true", "hasChildren": "false",
         "route": '/productDetails', "parentId": 7},
    ]


@app.route('/api/v1/clientes', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def clientes():
    return [
        {"id": 1, "nombre": 'Isidro', "apellidoPaterno": 'Lopez', "apellidoMaterno": 'Vazquez', "direccion": 'Diego de Montemayor 631', "telefono": '8184611746', "email": 'isidrolv@gmail.com'},
        {"id": 2, "nombre": 'Luis', "apellidoPaterno": 'Lopez', "apellidoMaterno": 'Vazquez', "direccion": 'Diego de Montemayor 631', "telefono": '8184611746', "email": 'isidro.leos@hotmail.com'}
    ]


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
