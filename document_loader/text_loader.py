from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

loader=TextLoader('ai.txt',encoding='utf-8')

docs=loader.load()

prompt1=PromptTemplate(
    template='Write a short report on {topic} in 10 lines',
    input_variables=['topic']
)

parser=StrOutputParser()

chain=prompt1 | model | parser

print(chain.invoke({'topic':docs[0].page_content}))


