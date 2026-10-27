from langchain_core.prompts import PromptTemplate



template=PromptTemplate.from_template(
    " {topic} in simple words with an example, "
    "as I am {years} years old."
)
template.save("template.json")