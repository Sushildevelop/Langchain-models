from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

parser=StrOutputParser()

class FeedBack(BaseModel):
    sentiment:Literal['positive','negative']=Field(description='Give the sentiment of the feedback')

parser2=PydanticOutputParser(pydantic_object=FeedBack)

prompt1=PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instructions} ',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}   
)



classifier_chain=prompt1 | model | parser2

# print("classifier ---------> ",classifier_chain.invoke({'feedback':"this is wonderful phone"}))

# result=classifier_chain.invoke({'feedback':"this is a wonderful smartphone"}).sentiment
# print(result)

prompt2=PromptTemplate(
    template='Write an appropriate response to this postive feedback \n {feedback} ',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback} ',
    input_variables=['feedback']
)

# branch_chain=RunnableBranch(
#     (condition,chain),
#     (condition2,chain2),
#     default chain
# )
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2 | model | parser),
    (lambda x:x.sentiment=='negative',prompt3 | model | parser),
    RunnableLambda(lambda x:"could not find sentiment") 
)

chain=classifier_chain | branch_chain

result=chain.invoke({"feedback":"This is a terrible phone"})

print(result)


