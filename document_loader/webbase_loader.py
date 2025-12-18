from langchain_community.document_loaders import WebBaseLoader

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

url='https://www.flipkart.com/motorola-edge-60-fusion-5g-pantone-amazonite-256-gb/p/itm9218b12ff853f'

loader=WebBaseLoader(url)

docs=loader.load()

parser=StrOutputParser()

prompt=PromptTemplate(
    template='Answer the following question \n {question} from the following text =\n {text}',
    input_variables=['question','text']
)

# print(len(docs))

# print(docs[0].page_content)

chain=prompt | model | parser

print(chain.invoke({'question':"what is price of product?",'text':docs[0]}))










