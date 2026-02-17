import random
random.seed(input("Enter seed... "))
characters_per_character = int(input("Enter the number of characters that represents each character "))
character_possibilities = int(input("Enter the amount of possibilities that each character can be "))
mode = input("Would you like to encode or decode text? (enter the word encode or decode) ")
valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890~!@#$%^&*()-_=+[{]}\\|;:\'\",<.>/?’ "
character_dict = {}
reverse_character_dict = {}


for i in valid_characters:
   random_strings = []
   for j in range(character_possibilities):
       random_string = ""
       for k in range(characters_per_character):
           random_string += random.choice(valid_characters)
       while random_string in reverse_character_dict:
           random_string = ""
           for k in range(characters_per_character):
               random_string += random.choice(valid_characters)
       random_strings.append(random_string)
   character_dict[i] = random_strings
   for j in random_strings:
       reverse_character_dict[j] = i


if mode == "encode":
   string = input("What text would you like to encode? ")
   encoded_string = ""
   for i in string:
       encoded_string += random.choice(character_dict[i])
   print(f"Result: {encoded_string}")
elif mode == "decode":
   string = input("What text would you like to decode? ")
   decoded_string = ""
   string_list = [string[i:i + characters_per_character] for i in range(0, len(string), characters_per_character)]
   for i in string_list:
       decoded_string += reverse_character_dict[i]
   print(f"Result: {decoded_string}")
else:
   print("Invalid option. Did you spell the word correctly?")
