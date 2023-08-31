from langchain.llms import OpenAI
import os



os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(temperature=0.9)
text = "What would be a good company name for a company that makes dynamic sportswear ?"
print(llm(text))