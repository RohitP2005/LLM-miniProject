import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain

# Set the API key
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY'] = api_key

llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.7)

def gen_shopName_Products(sport):
      # Define the prompt template for generating a shop name
    prompt_template_name = PromptTemplate(
        input_variables=["sports"],
        template="I wanna open a {sports} shop, suggest a single name only"
    )

    nameSeqChain = LLMChain(
        llm=llm,  # Replace with your LLM instance
        prompt=prompt_template_name,
        output_key='name'
    )

    # Define the prompt template for generating a product list
    prompt_template_list = PromptTemplate(
        input_variables=["name"],
        template="Suggest a product list for the {name} shop and return it as a comma-separated list."
    )

    listSeqChain = LLMChain(
        llm=llm,  # Replace with your LLM instance
        prompt=prompt_template_list,
        output_key='products'
    )
    

    chain = SequentialChain(
        chains=[nameSeqChain, listSeqChain],
        input_variables=['sports'],  # Input for the first chain
        output_variables=['name','products'],  # Adjust according to the outputs
        verbose=True
    )
    return chain({'sports':sport})