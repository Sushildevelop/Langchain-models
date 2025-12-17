from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnablePassthrough
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

passthrough=RunnablePassthrough()

prompt=PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='explain the following joke  {text}',
    input_variables=['text']   
)

parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination':RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic':'cricket'}))

