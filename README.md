#AI Reporting Sample Project, built with Python Django and OpenAI.

The project allows users to upload a file and run queries on top of it. The application leverages the power of OpenAI's natural language processing to provide answers to the user's queries based on the contents of the uploaded file.

``Installation``
To run AI Reporting, you will need Python 3.x installed on your system. You can install it from the official Python website.

``Clone the repository:``
git clone https://github.com/yourusername/ai-reporting.git

``Create a virtual environment and activate it:``
cd ai-reporting
python -m venv venv
source venv/bin/activate  # for Linux/MacOS
venv\Scripts\activate.bat  # for Windows

``Install the required packages:``
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

``Usage``
To use AI Reporting, follow these steps:

Update OpenAI API key in nlr\utils.py

Open your web browser and go to http://localhost:8000/.

Click on the "Upload File" button and select the file you want to analyze.

Once the file has been uploaded, you will be taken to the query page. Here, you can enter your query in natural language.

Click on the "Submit" button to run the query. AI Reporting will analyze the contents of the uploaded file and provide an answer to your query.

You can run multiple queries on the same uploaded file, and AI Reporting will provide answers based on the context of the previous queries.

``License``
AI Reporting is released under the MIT License. See LICENSE.txt for more information.
