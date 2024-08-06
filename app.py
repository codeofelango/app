from flask import Flask, render_template, request, jsonify, redirect, url_for
# from app import app
from google.cloud import bigquery
import requests

app = Flask(__name__)


API_ENDPOINT = "https://script.google.com/a/macros/herfy.com/s/AKfycbxQUAKstuPpzk39YCnWz8uCzJQyiWx0vIfaOhAZvle3k2H-5qOtXdhRFeWdRHAUUc1H/exec"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        print(request.form)
        form_data = request.form
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

if __name__ == '__main__':
    app.run( debug=True) #host='0.0.0.0', port=5001 ,