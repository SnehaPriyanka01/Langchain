# Import the necessary libraries
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain.chains import LLMChain
from langchain_ollama.chat_models import ChatOllama

# Initialize the Ollama model
model = ChatOllama(base_url='https://ollama.dealwallet.com', model='llama3')

# PART 1: Create a ChatPromptTemplate using a template string
template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)

print("----- Prompt from Template -----")
# Use the template to create a prompt with the topic 'cats'
prompt = prompt_template.invoke({"topic": "cats"})
print(prompt)

# Create the LLMChain with the Ollama model
llm_chain = LLMChain(llm=model, prompt=prompt_template)

# Run the model on the generated prompt
response = llm_chain.run({"topic": "cats"})
print("\n----- AI Response (Joke about cats) -----\n")
print(response)

# PART 2: Prompt with Multiple Placeholders
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} story about a {animal}.
Assistant:"""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})
print("\n----- Prompt with Multiple Placeholders -----\n")
print(prompt)

# Run the LLMChain with multiple placeholders
llm_chain_multiple = LLMChain(llm=model, prompt=prompt_multiple)
response_multiple = llm_chain_multiple.run({"adjective": "funny", "animal": "panda"})
print("\n----- AI Response (Story about a panda) -----\n")
print(response_multiple)

# PART 3: Prompt with System and Human Messages (Using Tuples)
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
print(prompt)

# Run the LLMChain with system and human messages
llm_chain_messages = LLMChain(llm=model, prompt=prompt_template)
response_messages = llm_chain_messages.run({"topic": "lawyers", "joke_count": 3})
print("\n----- AI Response (Multiple jokes about lawyers) -----\n")
print(response_messages)
