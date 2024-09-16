from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama.chat_models import ChatOllama

# Load environment variables from .env
load_dotenv()

# Create a ChatOllama model
model = ChatOllama(base_url='https://ollama.dealwallet.com/', model='llama3')

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequence of input messages.
# HumanMessage:
#   Message from a human to the AI model.
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain the concept of gravity."),
]

# Invoke the model with messages (alternative model interaction)
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")

# AIMessage:
#   Message from an AI.
alternative_messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain the concept of gravity."),
    AIMessage(content="Gravity is a force that attracts two bodies toward each other."),
    HumanMessage(content="Can you give me more details on how it works?"),
]

# Invoke the model with the alternative messages
result = model.invoke(alternative_messages)
print(f"Answer from AI: {result.content}")