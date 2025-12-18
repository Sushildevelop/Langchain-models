from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='rag_upload_sample.csv')

data = loader.load()

print(len(data))
print(data[0])