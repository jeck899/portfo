from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
@app.route('/index.html')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def my_pages(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:  # mode = a - is to append
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:  # mode = a - is to append
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])  # needs to be list


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try Again!'


# @app.route('/favicon.ico')

#app.run(port=5000)