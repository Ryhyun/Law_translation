from project import app


from flask import render_template, request


@app.route('/', methods=['GET'])
def start():
    return render_template('index.html')



