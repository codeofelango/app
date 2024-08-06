from flask import Flask, render_template, request, jsonify, redirect, url_for
from app import app
from google.cloud import bigquery
import requests
# Replace with your BigQuery project ID and dataset ID
# PROJECT_ID = "herfy-dev"
# DATASET_ID = "foodreq"
# client = bigquery.Client(project=PROJECT_ID)
# table_ref = client.dataset('herfy-dev').table('foodOrder')
# table = client.get_table(table_ref)  # This will raise an error if the table doesn't exist

# # Check if the table has data
# if table.num_rows == 0:
#     print("Table is empty. Please insert data first.")
# else:
#     print("Table schema:", table.schema)


API_ENDPOINT = "https://script.google.com/a/macros/herfy.com/s/AKfycbxQUAKstuPpzk39YCnWz8uCzJQyiWx0vIfaOhAZvle3k2H-5qOtXdhRFeWdRHAUUc1H/exec"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        print('entry')
        print(request.form)
        form_data = request.form
        print(form_data)
        # Add validation for form data here if needed

        # Send data to API
        print("go to")
        # language = form_data['language']
        # servicetype = form_data['servicetype']
        # peopecount = form_data['peopecount']
        # eventtype = form_data['eventtype']
        # city = form_data['city']
        # neighborhood = form_data['neighborhood']
        # date = form_data['date']
        # contactno = form_data['contactno']
        # print(language)

    #    print("go to")
    #     language = form_data['language']
    #     servicetype = form_data['servicetype']
    #     peopecount = form_data['peopecount']
    #     eventtype = form_data['eventtype']
    #     city = form_data['city']
    #     neighborhood = form_data['neighborhood']
    #     date = form_data['date']
    #     contactno = form_data['contactno']
    #     print(language)

    #     data = {"language":language,"servicetype":servicetype,"peopecount":peopecount,"eventtype":eventtype,"city":city,"neighborhood":neighborhood,"date":date,"contactno":contactno}
        
        response = requests.post(API_ENDPOINT, data=form_data)
        print(response)
        if response.status_code == 200:
            # Successful submission
            result = 'Done'
            # render_template('result.html',result =result)
            # return  render_template('result.html')
            return redirect(url_for('success'))
            # return jsonify({'message': 'Thank you for your Information, We will contact you shortly. Done '})
        else:
            # Handle error
            return jsonify({'error': 'An error occurred'})
        return jsonify({'message': 'Thank you for your Information, We will contact you shortly. '})
        # return  render_template('result.html')
    except Exception as e:
        # Log the error for debugging
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'error': 'Internal server error'})    


@app.route('/success')
def success():
    return render_template('result.html')

# class foodOrder(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)
 

# @app.route("/submit", methods=['GET', 'POST'])
# def submit():
#         foodOrder = foodOrder(username=form.username.data, email=form.email.data, password=hashed_password)
#         db.session.add(foodOrder)
#         db.session.commit()
#         flash('Your account has been created! You are now able to log in', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)        