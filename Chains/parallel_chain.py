from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

model1=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

prompt1=PromptTemplate(
    template="Generate a short and simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt2=PromptTemplate(
    template="Generate 5 short questions answers from the following text \n {text}",
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

parralel_chain=RunnableParallel({
    'notes':prompt1 | model | parser,
    'quiz':prompt2 | model1 | parser
})

merge_chain=prompt3 | model | parser

chain = parralel_chain | merge_chain

text="""
Retrieval-Augmented Generation (RAG) is an AI technique that improves large language model (LLM) responses by combining information retrieval with text generation. Instead of relying only on the model’s training data, RAG first searches external knowledge sources (such as documents, PDFs, or databases) using embeddings and vector search. The most relevant information is then provided as context to the LLM, which generates an accurate and up-to-date answer. RAG reduces hallucinations, supports private or domain-specific data, and is widely used in chatbots, question-answering systems, enterprise search, and AI assistants.

"""
result=chain.invoke({'text':text})

print(result)






