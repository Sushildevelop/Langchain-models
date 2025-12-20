from langchain.text_splitter import CharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('Artificial_Intelligence_Complete_Guide.pdf')

docs=loader.load()

text="""
LangChain is an open-source framework designed to simplify the development of applications powered by language models. It provides a suite of tools and abstractions that facilitate the integration of large language models (LLMs) into various applications, enabling developers to build sophisticated AI-driven solutions with ease.
One of the core features of LangChain is its ability to manage and manipulate text data effectively. The framework includes various text splitting strategies that allow developers to break down large documents into smaller, more manageable chunks. This is particularly useful when working with LLMs, as it helps to ensure that the input size remains within the model's token limits while preserving the context and meaning of the original text.
LangChain offers several text splitting techniques, including character-based, word-based, and sentence-based splitting. Each method has its own advantages and use cases, allowing developers to choose the most appropriate strategy based on their specific requirements. For instance, character-based splitting is useful for fine-grained control over chunk sizes, while sentence-based splitting helps maintain the coherence of the text.
In addition to text splitting, LangChain provides tools for chaining together multiple LLM calls, managing prompts, and handling outputs. This enables developers to create complex workflows that can process and analyze text data in a structured manner. The framework also supports integration with various LLM providers, making it versatile and adaptable to different use cases."""


splitter=CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    separator=' '
    
)

# result=splitter.split_text(text)

result=splitter.split_documents(docs)

print(result)