import tiktoken

TOKENIZER = tiktoken.get_encoding("cl100k_base")

# if set to True, it will use chatgpt model ("gpt-3.5-turbo") for all the completions
CHATGPT = True

# COMPLETION_MODEL - only applicable if CHATGPT is set to False
COMPLETION_MODEL = "text-davinci-003"  # "text-ada-001",


