from flask import Flask, request, redirect, url_for, render_template_string
import jinja2, re, hashlib

app = Flask(__name__)

@app.route('/')
def index():
 
       return redirect(url_for('no_filter'))
 
@app.route('/no_filter', methods=['GET'])
def no_filter():
        
        payload = str(request.args.get('payload'))
 
        template = '<!DOCTYPE html><html> <head> <title>Welcome '+payload+'!</title> </head> <body> <h1>Welcome '+payload+'!</h1> <p>Thanks for visiting,'+payload+'!</p> <form method="get" action="/no_filter"> <label for="payload">Enter your payload:</label> <input type="text" name="payload" id="payload" value="" > <button type="submit">Submit</button> </form> </body></html>'
 
        return render_template_string(template)


@app.route('/unsafe')
def unsafe():
    first_name = request.args.get('name', '')
    return make_response("Your name is " + first_name)

@app.route('/safe')
def safe():
    first_name = request.args.get('name', '')
    return make_response("Your name is " + escape(first_name))
 
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80, debug=False)
