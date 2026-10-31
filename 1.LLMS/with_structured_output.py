
from typing import TypedDict
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


# 1. Define the output structure
class ResumeInfo(TypedDict):
    name: str
    skills: list[str]


# 2. Initialize the LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


# 3. Enable structured output
structured_llm = llm.with_structured_output(ResumeInfo)


# 4. Provide resume text
resume = """
Ramesh R is an Information Science graduate.
He knows Python, SQL, Pandas, Power BI,
Machine Learning, and LangChain.
"""


# 5. Extract the information
result = structured_llm.invoke(
    f"""
    Extract the person's name and technical skills
    from the following resume.

    Resume:
    {resume}
    """
)


# 6. Display the result
print("Name:", result["name"])
print("Skills:", result["skills"])
print("Complete result:", result)
print ("hello world")