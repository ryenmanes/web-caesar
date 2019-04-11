from helpers import alphabet_position, rotate_character

def main():
  message = input("What do you need encrypted? ")
  rotate = input("How encrypted would you like it? With 1 being the least. ")
  print(encrypt(message,int(rotate)))
 

def encrypt(string, move):
  encrypted_text = ""
  for i in list(string):
    if i.isalpha():
      encrypted_text += rotate_character(i, move)
    else:
      encrypted_text += i 
  return encrypted_text




if __name__ == "__main__":
  main()
