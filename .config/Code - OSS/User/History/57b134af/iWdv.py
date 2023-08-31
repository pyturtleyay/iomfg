from langchain.llms import OpenAI

llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)

llm("Tell me a joke")
'\n\nWhy did the chicken cross the road?\n\nTo get to the other side.'

llm_result = llm.generate(["Tell me a joke", "Tell me a poem"]*15)
len(llm_result.generations)