from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text="""
class Document:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
        def __repr__(self):
     
            """
            
splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0
)

chunks=splitter.split_text(text)

print(len(chunks))
print(chunks)