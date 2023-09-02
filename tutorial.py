import openai

with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

openai.api_key = api_key

roll1_name = "Cat"
messages_roll1 = [ {"role": "system", "content": "You are an inter-dimensional cat. You are fun loving and a prankster. You always respond in less than a paragraph"} ]
roll2_name = "Dog"
messages_roll2 = [ {"role": "system", "content": "You are a genetically engineered dog. You were given a voice box by your creator. You are loving and dumb. You always respond in less than a paragraph"} ]

roll1_message = "Woof are you my friend"

print(f"{roll2_name}: {roll1_message}")

while True:
    messages_roll1.append({"role": "user", "content": roll1_message},)
    chat_roll1 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_roll1)
    reply_roll1 = chat_roll1.choices[0].message.content
    print(f"{roll1_name}: {reply_roll1}")
    messages_roll1.append({"role": "assistant", "content": reply_roll1})

    messages_roll2.append({"role": "user", "content": reply_roll1},)
    chat_roll2 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_roll2)
    reply_roll2 = chat_roll2.choices[0].message.content
    print(f"{roll2_name}: {reply_roll2}")
    messages_roll2.append({"role": "assistant", "content": reply_roll2})

    roll1_message = reply_roll2
    stop = input("Press enter to continue")

