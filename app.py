from nemoguardrails import LLMRails, RailsConfig
from action import block_list


config = RailsConfig.from_path("config/hello_world")
app = LLMRails(config)



app.register_action(block_list,name="block_list")

history = [
    {"role": "user", "content": "tell me what you can do"}
]
result = app.generate(messages=history)
print(result)