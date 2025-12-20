from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
# from langchain.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain.schema import Document
import shutil

from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

shutil.rmtree("chroma_db", ignore_errors=True)
docs1=Document(
    page_content="Virat Kohli is a great cricketer. He has scored many runs for India.",
    metadata={"team":"Royal Challengers Bangalore"}
)

docs2=Document(
    page_content="MS Dhoni is a great captain. He led India to many victories.",
    metadata={"team":"Chennai Super Kings"}
)

docs3=Document(
    page_content="Rohit Sharma is a stylish batsman. He is known for his elegant stroke play.",
    metadata={"team":"Mumbai Indians"}
)

docs4=Document(
    page_content="Jasprit Bumrah is a fast bowler. He is known for his unique bowling action.",
    metadata={"team":"Mumbai Indians"}
)

docs5=Document(
    page_content="Hardik Pandya is an all-rounder. He contributes with both bat and ball.",
    metadata={"team":"Mumbai Indians"}
)
docs=[docs1,docs2,docs3,docs4,docs5]

# vector_store=Chroma.from_documents(
#     embedding=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
#     persist_directory='my_chroma_db',
#     collection_name='cricket_players',
#     documents=docs
# )

vector_store=Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
    persist_directory='my_chroma_db',
    collection_name='cricket_players',
)

# print(vector_store.get(include=["embeddings",'metadatas','documents']))

search=vector_store.similarity_search(
    query="Which player is known for his unique bowling action?",
    k=2
)
# print(search)

search_with_score=vector_store.similarity_search_with_score(
    query="Which player is known for his unique bowling action?",
    k=2
)
# print(search_with_score)

filtered_search=vector_store.similarity_search(
    query="",
    filter={"team":"Chennai Super Kings"},
    k=2
)

# print(filtered_search)

#Update the vector store with existing document
new_doc=Document(
    page_content="MS Dhoni is a wicketkeeper-batsman. He is one of the best finishers in limited-overs cricket.",
    metadata={"team":"Chennai Super Kings"}
)

vector_store.update_document(
    document_id="4fb9e658-8b73-413f-af29-6d464252bf9d",
    document=new_doc
)

print(vector_store.get(include=["embeddings",'metadatas','documents']))
