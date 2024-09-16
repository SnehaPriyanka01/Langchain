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






 

