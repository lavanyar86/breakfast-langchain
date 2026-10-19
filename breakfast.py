from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. Load your secret API keys from the .env file
load_dotenv()

# 2. Connect to the ChatOpenAI model
llm = ChatOpenAI(model="gpt-4o-mini")

# 3. Create the prompt pinning down the exact format requested
prompt = (
    "Provide exactly 5 healthy breakfast ideas. "
    "Format strictly as a numbered list from 1 to 5, "
    "one line each, with no preamble, introduction, or concluding text."
)

# 4. Send the prompt to the model
reply = llm.invoke(prompt)

# 5. Print ONLY the text content of the reply (not the whole AIMessage object)
print(reply.content.strip())