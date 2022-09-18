from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><style>
        body{
            background: #34ebe8;
            }
            input[type=text]{
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            }
            input[type=submit]{
            width: 100%; 
            background-color: #4b42f5;
            color: white; 
            padding: 14px 20px; 
            margin: 8px 0; 
            border: none; 
            border-radius: 4px; 
            cursor: pointer;
            }
            </style>
        <body>
            <h1>Welcome to the greeter</h1>
            <form action="/greet">
                What's your name? <input type ='text' name='username'><br>
                What's your characteristics? <input type='text' name='character'><br>
                <input type='submit' value='Continue'>
            </form>
        </body></html>
        """


@app.route('/greet')
def greet():
    username = request.args.get('username', 'World')
    character = request.args['character']
    if character == '':
        msg = 'You did not tell me your characteristics.'
    else:
        msg = username + ' is ' + character + '.'

    return """
         <html><body style="background-color: #34ebe8;">
            <h2>Hello, {0}! </h2>
            {1}
      </body></html>
      """.format(username, msg)


# Launch the Flaskpy dev server
app.run(host="localhost", debug=True)
