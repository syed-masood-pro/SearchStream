import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

#Initializing the Arxiv tool to search for academic papers
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

#Initializing the Wikipedia tool to search for articles
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

#Initializing the DuckDuckGo search tool for general web searches
search = DuckDuckGoSearchRun(name="Search")

st.title("Search Stream")

st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your GROQ API key: ", type="password")

#Initializing chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assisstant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

#Displaying existing chat messages from the history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

if prompt := st.chat_input(placeholder="What is machine learning?"):
    #Adding the user's message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    #Displaying the user's message in the chat
    st.chat_message("user").write(prompt)

    #Initializing the Groq Chat LLM with the provided API key and desired model
    llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.3-70b-versatile", streaming=True)

    #Defining the list of tools available to the agent
    tools = [search, arxiv, wiki]

    #Initializing the LangChain agent with the tools, LLM, and agent type
    search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                                    handling_parsing_errors=True)

    with st.chat_message("assistant"):
        #Using a Streamlit callback handler to display the agent's thought process
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=True)
        #Running the agent with the user's query and get the response
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        #Adding the assistant's final response to the chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)

