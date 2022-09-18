from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
        <html>
        <style>
            body{
            background-color:#000;
            }
            h{
            font-size:70px;
            padding:50px;
            color: #fff;
            }
            a:hover, a:active {
            color: white;
            }
            p{
            color:#ffffff;
            font-size:120px;
            text-align:center;
            }
            </style>
            <body>
            <h><i><b>Hello!</b></i></h>
            <br><br>
            <p>Secret <a href="/letter">message</a> for you.</p>
        </body>
        </html>
        """
@app.route('/letter')
def letter():
    return """
        <html>
        <style>
        body{
        font-size:100px;
        text-align:center;
        padding:100px;
        }
        </style>
        <body>
            Don't give up<br>&<br>make your dreams come true.
        </body>
        </html>
        """

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
