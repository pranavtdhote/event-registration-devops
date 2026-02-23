from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']

        return f"""
        <h2 style='color:green;text-align:center;margin-top:50px;'>
        ✅ Registration Successful! Welcome {name}
        </h2>
        """

    return render_template('register.html')


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)