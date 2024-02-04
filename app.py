import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate

st.set_page_config(page_title="Ask Eminem Anything!")

st.image("eminem.png", caption="", width=300)
st.title("Ask Eminem Anything!")

openai_api_key = st.sidebar.text_input('OpenAI API Key', type="password")

def generate_response(question):
  llm = OpenAI(openai_api_key=openai_api_key)

  # Prompt
  template = 'As a popular rapper, generate a paragraph of eminem like rap to answer the question: {question}'

  prompt = PromptTemplate(input_variables=['question'], template=template)

  prompt_query = prompt.format(question=question)

  # RUn LLM model to print out the response

  response = llm(prompt_query)

  return st.info(response)


with st.form('myform'):
  question_text = st.text_input('Enter question...', '')

  submitted = st.form_submit_button('Submit')

  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API Key')

  if submitted and openai_api_key.startswith('sk-'):
    generate_response(question_text)


st.text('👉 YouTube Tutorial: Build Ask Eminem Bot with Langchain and Streamlit')
st.link_button("Watch Tutorial", "https://www.youtube.com/watch?v=a2shHB4MRZ4", help=None, type="secondary", disabled=False, use_container_width=False)
st.link_button("Source Code", "https://github.com/strongSoda/eminembot-tutorial", help=None, type="secondary", disabled=False, use_container_width=False)
st.text("Like, Subscribe on YouTube and Follow on GitHub 🙏")






