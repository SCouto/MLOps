import os
import pickle
from flask import Flask, request, render_template
from PIL import Image
import numpy as np
import shutil

app = Flask(__name__)

# Load the models
<TODO>


def preprocess_image(image_path):
    """Preprocess the uploaded image for prediction."""
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img = img.resize((64, 64))  # Resize to 64x64 to match the expected input shape
    img_array = np.array(img).flatten()  # Flatten the image to a 1D array
    upper_half = img_array[:2048]  # Get the upper half (2048 features)
    return upper_half  # Return only the upper half


def create_image_from_prediction(upper_half, prediction):
    """Combine upper half and predicted lower half into a full image."""
    # Combine the upper half and predicted lower half
    full_image_array = np.concatenate((upper_half, prediction))  # 2048 + 2048 = 4096

    # Clip values to be in range 0-255
    full_image_array = np.clip(full_image_array, 0, 255).astype('uint8')  # Ensure pixel values are valid
    return Image.fromarray(full_image_array.reshape(64, 64))  # Convert to PIL Image


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the file part is present in the request
        if 'file' not in request.files:
            return "No file part", 400

        file = request.files['file']

        # Check if the file has a valid name
        if file.filename == '':
            return "No selected file", 400

        # Ensure the uploads directory exists
        os.makedirs('uploads', exist_ok=True)
        os.makedirs('static', exist_ok=True)

        upload_path = os.path.join('uploads', file.filename)
        static_path = os.path.join('static', file.filename)

        file.save(upload_path)
        shutil.copy(upload_path, static_path)

        try:
            upper_half = preprocess_image(upload_path)

            # Make predictions and generate output images
            output_images = {}
            for name, model in models.items():
                prediction = <TODO>
                print(f"{name} prediction: {prediction}", flush=True)  # Debugging line

                output_images[name] = create_image_from_prediction(upper_half, prediction)

            # Save output images to the static folder and get their paths for rendering
            output_image_paths = {}
            for name, img in output_images.items():
                output_image_path = os.path.join('static', f"{name}_output.png")
                img.save(output_image_path)
                output_image_paths[name] = f"{name}_output.png"  # Update to just the filename

            return render_template('upload.html', output_images=output_image_paths, image=file.filename)

        except Exception as e:
            return f"An error occurred while processing the image: {str(e)}", 500

    return render_template('upload.html', output_images=None, image=None)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True, host='0.0.0.0')
