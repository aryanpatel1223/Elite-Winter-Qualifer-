import random


def generate_response(user_input):
  responses = [
    "That's What I Like To Hear!",
    "Great!",
    "Niceeee!",
    "That's Awesome!"
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'

  user_input = input("Hello, how are you?\n")
  user_input = input("how is everyone in the family doing?\n")
  user_input = input("Have a wonderful day and Happy New Year!!\n")
  user_input = input("I surely will!\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()