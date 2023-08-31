from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
from langchain.chains import LLMChain



os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(temperature=2.0)
#text = "What would be a good company name for a company that makes dynamic sportswear ?"
#print(llm(text))



prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

#print(prompt.format(product="cheap shoes"))
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("colorful socks"))