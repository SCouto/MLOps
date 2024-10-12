from flask import Flask, request, render_template, redirect, url_for
import joblib
import numpy as np
from PIL import Image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load the trained model
<TODO>

# Set up a directory to save uploaded images
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configure allowed file types
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        
        if file.filename == '':
            return 'No selected file'
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

            # Process the image and make prediction
            prediction = predict_digit(file_path)
            
            return render_template('upload.html', filename=filename, prediction=prediction)
    
    return render_template('upload.html')

def predict_digit(image_path):
    # Load and preprocess the image
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img = img.resize((8, 8))  # Resize to 8x8 pixels
    img_data = np.array(img)  # Convert to array
    img_data = 16 - (img_data / 16)  # Inverse the color scale
    img_data = img_data.reshape(1, -1)  # Reshape for model input
    prediction = <TODO>
    return prediction[0]

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

# Only run if executed as a script (not imported as a module)
if __name__ == '__main__':
    app.run(debug=True)

