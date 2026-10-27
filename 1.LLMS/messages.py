from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 
from dotenv import load_dotenv
load_dotenv()

model=ChatGroq(model="openai/gpt-oss-20b",temperature=1.5, max_completion_tokens=1000)

messages=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="tell me about langchain?")
]

response=model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(messages)
print("AI: ",response.content)
