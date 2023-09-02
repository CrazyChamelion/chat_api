import openai

with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

openai.api_key = api_key

def generate_hint(word, previous_guesses):
    # Generate a hint from ChatGPT based on the word and previous guesses
    prompt = f"Generate a hint for the word: '{word}'\nPrevious guesses: {', '.join(previous_guesses)}"
    #response = openai.Completion.create(
    #    engine="davinci",
    #    prompt=prompt,
    #    max_tokens=30,
    #    n = 1,
    #    stop=None,
    #    temperature=0.7
    #)
    #return response.choices[0].text.strip()
    messages =[{"role": "user", "content": prompt}]
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    return reply

def generate_word():
    # Generate a hint from ChatGPT based on the word and previous guesses
    prompt = "Generate a random word"
    #response = openai.Completion.create(
    #    engine="davinci",
    #    prompt=prompt,
    #    max_tokens=30,
    #    n = 1,
    #    stop=None,
    #    temperature=0.7
    #)
    #return response.choices[0].text.strip()
    messages =[{"role": "user", "content": prompt}]
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    return reply

def guess_the_word():
    print("Welcome to Guess the Word!")
    secret_word = generate_word()
    max_attempts = 5
    previous_guesses = []

    hint = generate_hint(secret_word, previous_guesses)
    print("\nHint:", hint)

    for attempt in range(max_attempts):
        guess = input("\nYour guess: ").lower()
        previous_guesses.append(guess)

        if guess.lower() == secret_word.lower():
            print(f"Congratulations! You guessed the word '{secret_word}' correctly.")
            break
        else:
            print("Incorrect guess. Keep trying!")

    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The secret word was '{secret_word}'.")

if __name__ == "__main__":
    guess_the_word()