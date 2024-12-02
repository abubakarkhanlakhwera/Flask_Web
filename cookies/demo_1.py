from flask import Flask, request, make_response
 
app = Flask(__name__)

@app.route('/')
def home():
    response = make_response('<h1>Hello World</h1>')
    return response

@app.route('/set_cookie')
def set_cookie():
    response = make_response('<h1>Welcome to cookies</h1>')
    response.set_cookie('cookie_name', 'cookie_value')
    return response    

@app.route('/get_cookie')
def get_cookie():
    value = request.cookies.get('cookie_name')
    response = make_response(f'<h1>Cookie Value: <i>{value}</i></h1>')
    return response
    
    
if __name__ == '__main__':
    app.run(debug=True)