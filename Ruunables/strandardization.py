from abc import ABC,abstractmethod
import random

class Runnable(ABC):
    
    @abstractmethod
    def invoke(self,input_data):
        pass
    

class Duplicate(Runnable):
    
    def __init__(self):
        print('LLM created')
        
    def invoke(self,prompt):
        response_list=[
            "Delhi is the capital of India",
            "Ipl is a cricket league",
            "AI stands for artificial intelligence"
        ]
        
        return {'response':random.choice(response_list)}
        
        
    def predict(self,prompt):
        response_list=[
            "Delhi is the capital of India",
            "Ipl is a cricket league",
            "AI stands for artificial intelligence"
        ]
        
        return {'response':random.choice(response_list)}
    

  
class DuplicatePromptTemplate(Runnable):
    
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables
        
    def invoke(self,input_dict):
        return self.template.format(**input_dict)
        
    def format(self,input_dict):
        return self.template.format(**input_dict)
    
template=DuplicatePromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['topic']
) 

template1=DuplicatePromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

template2=DuplicatePromptTemplate(
    template='explain the following joke {response}',
    input_variables=['response']
)

llm=Duplicate()

class DuplicateStrOutputParser(Runnable):
    def __init__(self):
        pass
    
    def invoke(self,input_data):
        return {'response': input_data['response']}
    
parser=DuplicateStrOutputParser()
    
class RunnableConnector(Runnable):
    
    def __init__(self,runnable_list):
        self.runnable_list=runnable_list
        
    def invoke(self,input_data):
        
        for runnable in self.runnable_list:
            input_data=runnable.invoke(input_data)
            
        return input_data
        
chain=RunnableConnector([template,llm,parser])

chain1=RunnableConnector([template1,llm,parser])

chain2=RunnableConnector([template2,llm,parser])

final_chain=RunnableConnector([chain1,chain2])

print(final_chain.invoke({'topic':'cricket'}))


# print(chain1.invoke({'topic':'AI'}))

# print(chain.invoke({'length':'long','topic':'India'}))









