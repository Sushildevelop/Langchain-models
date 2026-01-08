import random
class Duplicate:
    
    def __init__(self):
        print('LLM created')
        
    def predict(self,prompt):
        response_list=[
            "Delhi is the capital of India",
            "Ipl is a cricket league",
            "AI stands for artificial intelligence"
        ]
        
        return {'response':random.choice(response_list)}
    

llm=Duplicate()




llm.predict('What is the capital of India')
