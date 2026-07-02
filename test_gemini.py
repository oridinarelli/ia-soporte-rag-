from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

respuesta = llm.invoke(
    "Explica qué es LangChain en dos líneas."
)

print(respuesta.content)