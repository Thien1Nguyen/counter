from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "porkchop and cheese"

@app.route('/')
def index():
    print("User Log")

    if not 'visit' in session:
        session['visit'] = 0

    if not 'count' in session:
        session['count'] = 0
    

    session['visit'] += 1
    return render_template("index.html")

@app.route('/add_count')
def add_count():
    session['count'] += 2

    return redirect('/')

@app.route('/destroy_session')
def destroy_session ():
    session.clear()
    return redirect('/')

@app.route('/input_count', methods=['POST'])
def input_route():
    custom_add = int(request.form['input_count'])
    session['count'] += custom_add 
    return redirect('/')

if __name__== "__main__":
    app.run(debug=True)