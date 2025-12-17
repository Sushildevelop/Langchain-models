from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

prompt=PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='explain the following joke  {text}',
    input_variables=['text']   
)

parser=StrOutputParser()

chain=RunnableSequence(prompt,model,parser,prompt2,model,parser)

print(chain.invoke({"topic":'AI'}))