from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model='llama-3.1-8b-instant'
)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.applegadgetsbd.com/product/apple-mac-mini-m4-10-core-cpu-10-core-gpu-16-512gb'

loader = WebBaseLoader(web_path=url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'What is the product price here?', 'text': docs[0].page_content}))