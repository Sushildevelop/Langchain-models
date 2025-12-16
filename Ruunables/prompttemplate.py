
class DuplicatePromptTemplate:
    
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables
        
    def format(self,input_dict):
        return self.template.format(**input_dict)
    
    
    
template=DuplicatePromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['topic']
)

template.format({'length':'short','topic':'India'})
