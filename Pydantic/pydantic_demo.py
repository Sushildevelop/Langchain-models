from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

#Schema for structured output
class Review(BaseModel):

    summary:str
    sentiment:str


structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""The hardware is great but the software has some bugs that need to be fixed.""")

print(result)