from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to my Python Web Server!</h1><p>GitHub Portfolio Project</p>"

@app.route('/about')
def about():
    return "This is a simple backend server built with Flask."

if __name__ == '__main__':
    app.run(debug=True)
