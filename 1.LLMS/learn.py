from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_completion_tokens=1000
)

template1 = PromptTemplate.from_template(
    "Explain to me about {topic}"
)

template2 = PromptTemplate.from_template(
    "Explain the following text in 5 lines:\n{text}"
)

parser = StrOutputParser()

chain = (
    template1
    | model
    | parser
    | RunnableLambda(lambda text: {"text": text})
    | template2
    | model
    | parser
)

response = chain.invoke({
    "topic": "LangChain"
})

print(response)