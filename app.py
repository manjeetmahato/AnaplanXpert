#IMPORT SECTION
import os
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import DuckDuckGoSearchResults 
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
import requests
import pytesseract
from PIL import Image

# Set the Tesseract-OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text.strip()

# 🟢 Load environment variables
load_dotenv()
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
if not GOOGLE_API_KEY or not SERPER_API_KEY:
    st.error("GOOGLE_API_KEY or SERPER_API_KEY not set in environment. Please configure them in your .env file.")
    st.stop()

# Optional if needed for other queries
duckduckgo_search_tool = DuckDuckGoSearchResults()

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    top_p=0.95,
    top_k=40
)

# Prompt Templates
classification_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""Classify the following user input into one of three categories: "greeting", "anaplan question", or "other".

Input: {user_input}
Answer:"""
)

greeting_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""Respond warmly to the following greeting.
User: {user_input}
Bot:"""
)

anaplan_expertise_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""You are an Anaplan Certified Professional with over 15 years of experience. Respond concisely and effectively to any questions related to Anaplan. Provide clear, actionable steps based on official Anaplan documentation and best practices.

User: {user_input}
Answer:"""
)

fallback_response = "I can only answer questions related to Anaplan. Please ask something about Anaplan."

# Conversation Memory
memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history", return_messages=True)

def search_anaplan_docs(query):
    url = "https://google.serper.dev/search"  
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": query, "num": 5}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json() 
    else:
        return None

def get_anaplan_answer(question):
    try:
        response = agent.run(question)
        return response
    except Exception as e:
        return f"Error generating answer: {str(e)}"

def get_response(user_input):
    try:
        classification = llm.invoke(classification_prompt.format(user_input=user_input)).strip().lower()
        # Check classification and choose branch accordingly
        if "greeting" in classification:
            response = llm.invoke(greeting_prompt.format(user_input=user_input))
        elif "anaplan question" in classification:
            if "documentation" in user_input.lower() or "how to" in user_input.lower():
                search_results = search_anaplan_docs(user_input)
                if search_results and "organic" in search_results and search_results["organic"]:
                    top_result = search_results["organic"][0]
                    snippet = top_result.get("snippet", "")
                    combined_prompt = (
                        f"Based on the following documentation snippet:\n\n"
                        f"{snippet}\n\n"
                        f"Provide a complete, detailed answer to this question:\n\n"
                        f"{user_input}"
                    )
                    response = llm.invoke(combined_prompt)
                else:
                    response = "No relevant documentation found."
            else:
                response = get_anaplan_answer(user_input)
        else:
            response = fallback_response
        
        return response
    except Exception as e:
        return f"Error processing request: {str(e)}"

tools = [duckduckgo_search_tool]
# Initialize the agent without verbose logging so that the full answer is returned only to the frontend.
agent = initialize_agent(
    tools=tools,
    agent_type=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    llm=llm,
    memory=memory,
    verbose=True
)

# ------------------- UI Code -------------------

# Sidebar
with st.sidebar:
    st.title("🔹 Anaplan Expert Assistant")
    st.caption("💡 Ask me anything about Anaplan modeling, formulas, or troubleshooting!")
    st.markdown("### **🔍 What Can I Do?**")
    st.markdown("✅ Debug Anaplan formula errors\n\n✅ Explain best modeling practices\n\n✅ Fetch real-time Anaplan docs")
    st.markdown("### **📌 Data Sources**")
    st.markdown(
        """
        - [Anaplan Official Website](https://www.anaplan.com/)
        - [Anaplan Help Center](https://help.anaplan.com/)
        - [Anaplan Community](https://community.anaplan.com/)
        - [Anaplan Login Portal](https://id.anaplan.com/)
        - [Anaplan All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3)
        - [Anaplan Product Overview](https://product.anaplan.com/)
        - [Anaplan Support Center](https://support.anaplan.com/)
        - [Anaplan Planual](https://support.anaplan.com/planual-5731dc37-317a-49fa-a5ff-7fc3926972de)
        - [Anaplan Release-notes](https://help.anaplan.com/release-notes-f0a5a653-4b25-42bf-a4c1-e0e453541191)
        """
    )
    
    #image uploader in the sidebar 
    uploaded_image = st.file_uploader("Upload an image 📸 (optional)", type=["png", "jpg", "jpeg"], key="sidebar_image_uploader")
    st.markdown("Made in India ❤️")

# Main UI Chat window and other content
st.title("💬 Anaplan Expert Chat")
st.caption("🚀 Get real-time, expert Anaplan guidance powered by AI.")

# Process image upload from sidebar if available
if uploaded_image:
    image = Image.open(uploaded_image)
    extracted_text = extract_text_from_image(image)
    if extracted_text:
        st.write("**Extracted Text from Image:**")
        st.code(extracted_text)
    else:
        st.error("No text detected in the uploaded image.")

# Chat History Storage
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input: Ask your question here
user_question = st.chat_input("Enter your Anaplan question:")
if user_question:
    st.session_state.chat_history.append({"role": "user", "content": user_question})
    with st.spinner("Processing your query..."):
        answer = get_response(user_question)
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])



 











