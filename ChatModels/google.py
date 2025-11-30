from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
result=model.invoke("Explain the theory of relativity in simple terms.")
print(result.content)