# Text To MP3 Converter 🎶

An online tool for effortlessly converting text to MP3. Designed for precision and user-friendliness, users can instantly upload their text and download it as an MP3 file. Ideal for both professionals and personal use.

## Beneficiaries 🎯

- Users Seeking Quick Audio Conversion: For those in need of rapid text-to-MP3 conversions.
- Good First Commit Project For New Django Developers

## Features 🛠️

- Convert Text to MP3 in One Click and Download it
- Fast Processing
- Easy To Use (just upload your text)
- User-Friendly UI
- No Ads or Lags
- Flexible API: 
  Whether you're on a desktop, mobile or any other platform, our API endpoint ``api/convert-to-mp3/`` ensures you can fetch your MP3 files anytime, anywhere.
- Efficient Workflow: 
  Each day, the initial 50 operations are driven by an efficient text-to-MP3 API. Our reliable Python backend seamlessly steps in, guaranteeing unlimited, consistent, and flawless service.

## Getting Started with Development 🚀

### Prerequisites
Ensure you have Python - version 3.11.5 recommended - and pip installed on your machine.

### Installation

#### Steps:

1. **Clone the repository.**
   ``
   git clone git@github.com:Thanoon12k/text-to-mp3-converter.git
   ``
2. **Navigate to the project directory.**
   ``
   cd path-to-project-directory
   ``
3. **Create a virtual environment.**
   ``
   python -m venv venv        
   ``
4. **Activate the virtual environment.**
   - On Windows:
     ``
     venv\Scripts\activate
     ``
   - On macOS and Linux:
     ``
     source venv/bin/activate
     ``

5. **Install the required packages.**
   ``
   pip install -r requirements.txt
   ``
6. **Run the Django server.**
   ``
   python manage.py runserver
   ``
Visit http://localhost:8000 in your browser to see the website in action!

## Developer Usage 🛠️

For those interested in integrating our text-to-MP3 conversion service into their applications, we offer a straightforward API endpoint.

### Accessing the API

**Endpoint**: ``api/convert_to_mp3/``

To use our API:

1. **POST Request**: Send a POST request to the endpoint with your text attached.
    ### Parameters

    `text`

    - **Type**: String
    - **Required**: Yes
    - **Description**: The string of text you wish to convert to MP3.

2. **Response**: You will receive the processed MP3 file.

### Example using `curl`:

   ``
   curl -X POST -F "text=@path_to_your_text.txt" http://127.0.0.1:8000/api/convert-to-mp3/
   ``

## Contributing 🤝

Open to developers and enthusiasts who'd like to collaborate and enhance this project. Let's make this even more fantastic together!

## Acknowledgments:

- Thanks to  [gTTS Python package](https://github.com/pndurette/gTTS) that power convert operation.

For live demonstrations, visit our website [Live-WebSite](http://txt2mp3.pythonanywhere.com/)
