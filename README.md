# coffee-bean-grinder-setting

**Coffee Bean Analyzer**

A web application that analyzes coffee bean images to recommend the optimal grinder setting based on the roast level of the beans.

## Features

- Upload an image of coffee beans.
- Analyze the image to determine the recommended grinder setting.
- View the uploaded image alongside the analysis result.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **OpenCV**: A library for computer vision tasks.
- **SQLite**: A lightweight database for storing uploaded images and settings.
- **HTML/CSS/JavaScript**: Front-end technologies for building the user interface.



## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/coffee-analyzer.git
   cd coffee-analyzer

2.  **Set up a virtual environment:**
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages**
     pip install -r requirements.txt

4. **Run the application on terminal**
    python app.py


**Usage**

1- Use the file input to upload an image of coffee beans.
2- Click the "Upload Image" button to analyze the image.
3- The recommended grinder setting will be displayed below the uploaded image.



