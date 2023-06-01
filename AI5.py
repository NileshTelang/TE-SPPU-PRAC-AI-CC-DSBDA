import random

# Define a dictionary of predefined prompts and their corresponding responses

prompts = {

    "hi": ["Hello!", "Hi there!", "Hey!"],

    "how are you": ["I'm good, thanks!", "I'm doing well!", "All is well!"],

    "bye": ["Goodbye!", "See you later!", "Take care!"],

    "default": ["I'm sorry, I didn't understand that.", "Can you please rephrase that?", "I'm still learning. Please bear with me."],

    "what do you do": ["I am a customer serive chatbot!"],

}

# Function to generate a response based on user input

def generate_response(user_input):

    # Convert user input to lowercase for case-insensitive matching

    user_input = user_input.lower()

    # Check if user input matches any predefined prompts

    for prompt, responses in prompts.items():

        if user_input in prompt:

            return random.choice(responses)

    # If no matching prompt is found, return a default response

    return random.choice(prompts["default"])

# Main interaction loop

while True:

    # Get user input

    user_input = input("User: ")

    # Generate and display bot response

    bot_response = generate_response(user_input)

    print("ChatBot:", bot_response)

    # Exit the loop if the user says goodbye

    if "bye" in user_input.lower():

        break
