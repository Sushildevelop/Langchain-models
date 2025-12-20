from langchain_experimental.text_splitters import SemanticChunker

from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter=SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1,
)

sample="""
Python is a high-level, interpreted programming language known for its readability and versatility. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. JavaScript, on the other hand, is a versatile, high-level programming language primarily used for web development. It enables interactive web pages and is an essential part of web applications, alongside HTML and CSS. JavaScript supports event-driven, functional, and imperative programming styles.

Java is a class-based, object-oriented programming language designed to have as few implementation dependencies as possible. It is widely used for building enterprise-scale applications, mobile applications (especially Android apps), and large systems. Java emphasizes portability, performance, and security.

"""

chunks=text_splitter.create_documents([sample])

print(len(chunks))
print(chunks)