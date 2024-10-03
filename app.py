from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import cv2
from analyzer import analyze_image
from models import db, CoffeeBean

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/images/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coffee.db'

db.init_app(app)

# Create the database before the first request
@app.before_request
def create_tables():
    if not getattr(app, '_tables_created', False):
        db.create_all()
        app._tables_created = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Analyze the image using OpenCV
        grinder_setting = analyze_image(filepath)

        # Save to database (optional)
        bean = CoffeeBean(image=file.filename, grinder_setting=grinder_setting)
        db.session.add(bean)
        db.session.commit()

        return jsonify({"grinder_setting": grinder_setting})

if __name__ == '__main__':
    app.run(debug=True)
