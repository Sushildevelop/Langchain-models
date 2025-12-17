from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnablePassthrough, RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

def word_counter(text):
    return len(text.split())

# runnable_word_counter=RunnableLambda(word_counter)

# print(runnable_word_counter.invoke('Hi there how are you'))

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

parser=StrOutputParser()

prompt=PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

joke_gen_chain=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    "word_count":RunnableLambda(lambda x :len(x.split()))
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic':'AI'}))





