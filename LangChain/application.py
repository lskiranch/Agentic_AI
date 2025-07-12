import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

load_dotenv()




llm = ChatOpenAI(model='o1-mini')
print(llm)
result = llm.invoke('what is the llm model you used to answer this query')
print(result)
print(result.content)


