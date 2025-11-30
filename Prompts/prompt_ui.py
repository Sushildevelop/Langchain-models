from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

st.header("Research Assistant using Google Gemini-2.5")

# user_input=st.text_input("Enter your research question here:")
paper_input=st.selectbox("Select your research topic:", 
                         ["Quantum Computing", "Climate Change", "Artificial Intelligence", "Renewable Energy", "Space Exploration"])   
style_input=st.selectbox("Select the writing style:", 
                         ["Formal", "Informal", "Technical", "Narrative", "Persuasive"])

length_input=st.selectbox("Select the length of the output (in words):", ["short (100-200)", "medium (200-500)", "long (500-1000)"])

template=PromptTemplate(
    template="Write a {style_input} research paper on the topic of {paper_input} in a {length_input} length.",
    input_variables=["paper_input", "style_input", "length_input"]
)

#fill the placeholders in the template
prompt=template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

if st.button("Sumbit"):
    result=model.invoke(prompt)
    st.write(result.content)
    # st.write("Hello")
    
template.save("research_assistant_template.json")
    
    

