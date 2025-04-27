from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
claude_llm = ChatAnthropic(model = "claude-3-5-sonnet-latest")
deepseek_llm = ChatDeepSeek(model="deepseek-chat")
openai_llm = ChatOpenAI(model="o3-mini")
groq_llm = ChatGroq(model="deepseek-r1-distill-llama-70b")