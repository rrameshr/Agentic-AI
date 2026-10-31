from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 

from dotenv import load_dotenv
load_dotenv()

parser=StrOutputParser()

prompt1=PromptTemplate(
  template='generate a detailed report on {topic}',
  input_variables=['topic'])

prompt2=PromptTemplate(
  template='summarize the following text in 5 lines:\n{text}',input_variables=['text'])

model=ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=1.5,
    max_tokens=1000 )

chain=prompt1|model|parser|prompt2|model|parser

result=chain.invoke({"topic":"unemployement"})

print(result)

print(chain.get_graph().print_ascii())  