                        **LANGCHAIN**
                        
Create a folder like LC

Now open terminal python -m venv myenv .
Then it will the environment at left after LC.

Next run this code myenv\Scripts\activate

Thenit will activate the scripts.

Next create a requirements.txt Which contains this code 

chatollama==0.1.5
langchain==0.2.16
python-dotenv==1.0.1
load-dotenv==0.1.0
langchain-community==0.2.16

Now run this command in terminal as pip install -r requirements.txt

If not running anything directly install each one like 

Pip install chatollama
Pip install langchain
 And so on,….

Now 

Create chat_models.py and enter the code as

from dotenv import load_dotenv
from langchain_ollama.chat_models import ChatOllama


#load environment variables from .env
load_dotenv()


print("load env")
#create a chatollama model
model = ChatOllama(base_url='https://ollama.dealwallet.com/',model = 'llama3')
print ("llama3 model created")
#invoke the model with a message
result = model.invoke("what is 81 divided by 9?")
print("full result")
print(result)
print("contentonly")
print(result.content)

Run this in terminal Python chat_models.py

**OUTPUT**

(base) PS C:\Users\sneha\OneDrive\LChain> python chat_models.py
load env
llama3 model created
full result
content='Easy one!\n\n81 divided by 9 is:\n\n9 ÷ 81 = 9.00' response_metadata={'model': 'llama3', 'created_at': '2024-09-13T12:58:54.925386745Z', 'message': {'role': 'assistant', 'content': ''}, 'done_reason': 'stop', 'done': True, 'total_duration': 2582122587, 'load_duration': 1019808, 'prompt_eval_duration': 125654000, 'eval_count': 21, 'eval_duration': 2326653000} id='run-e4cebf7e-a08b-4e1e-8153-1d53c808dae6-0'
contentonly
Easy one!

81 divided by 9 is:

9 ÷ 81 = 9.00

            **REGARDING FIREBASE_ADMIN and SDK setup**
Here’s a step-by-step guide on how to set up Firebase for your project, configure Firestore, and generate the Firebase credentials file (firebase-adminsdk.json).

Step 1: Create a Firebase Project
Go to Firebase Console: Open your browser and navigate to Firebase Console.

Create a New Project:

Click on the Add Project button.
Name your project: Enter a name for your project (e.g., "ChatBotApp").
Enable Google Analytics (optional): You can enable or disable Google Analytics based on your preference.
Click Create Project and wait for Firebase to set up the project.
Step 2: Set Up Firestore Database
Open the Firebase Project: After your project is created, you'll be directed to the project dashboard.

Go to Firestore Database:

In the left-hand sidebar, click on Firestore Database under the Build section.
Create a Firestore Database:

Click on Create Database.
Choose your mode: For development purposes, you can select Start in test mode (allows easier read/write access).
Select a location: Choose a location for your Firestore database, which should align with your project’s region.
Click Enable to complete the setup.
At this point, your Firestore database is ready to store data.

Step 3: Generate Firebase Credentials (firebase-adminsdk.json)
To allow your Python project to communicate with Firebase, you need to authenticate it by using a service account credential file.

Go to Project Settings:

In the Firebase Console, click the gear icon next to Project Overview in the left sidebar.
Select Project settings.
Generate a Service Account Key:

Navigate to the Service accounts tab (scroll down if needed).
Under Firebase Admin SDK, click on Generate new private key.
A confirmation dialog will appear—click Generate key. This will download a JSON file to your computer.
Save the Credentials File:

The JSON file you just downloaded contains your Firebase project’s credentials. It will have a name similar to firebase-adminsdk-xxxxx.json.
Move this file into your Python project directory. You'll use this file to authenticate Firebase when you interact with it through Python.
Step 4: Add Firebase to Your Python Project
Install Firebase Admin SDK:

In your terminal or command prompt, install the Firebase Admin SDK for Python:
bash
Copy code
pip install firebase-admin
Initialize Firebase in Your Python Code:

In your Python script, import the Firebase Admin SDK and initialize the app using the credentials file you just downloaded:
python
Copy code
import firebase_admin
from firebase_admin import credentials, firestore

# Path to your firebase-adminsdk.json file
cred = credentials.Certificate('path/to/your/firebase-adminsdk.json')
firebase_admin.initialize_app(cred)

# Access Firestore
db = firestore.client()
Access Firestore Database:

After initializing Firebase, you can now interact with your Firestore database in your code by reading from or writing to collections.
Recap:
Create Firebase Project: Go to Firebase Console and set up a project.
Set Up Firestore: Create a Firestore database to store data like chat history.
Generate Credentials: Download the service account JSON (firebase-adminsdk.json) and place it in your project directory.
Initialize Firebase in Python: Use Firebase Admin SDK to authenticate and access Firestore in your Python application.
This setup allows your Python project to communicate securely with Firebase and store data, such as chat history, in the Firestore database.




 

