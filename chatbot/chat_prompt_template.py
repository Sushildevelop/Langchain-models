from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template=ChatPromptTemplate([
    ("system","You are a helpful {domain} expert."),
    ("human","Provide a simple explanation about {topic}.")
    # SystemMessage(content="You are a helpful {domain} expert."),
    # HumanMessage(content="Provide a simple explanation about {topic}.")
])

prompt=chat_template.invoke({
    "domain":"quantum computing",'topic':"quantum entanglement"})

print(prompt)





