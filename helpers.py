def alphabet_position(position_number, upper):
  character = chr(position_number + 65)
  if upper:
    return character
  else:
    return character.lower()

def rotate_character(letter, move):
  if not(letter.isalpha()):
    return letter
  if letter.isupper():
    letterpos = ord(letter) - 65
  else:
    letterpos = ord(letter)-97
  rotated_position = (letterpos + move) % 26  
  if letter.isupper():
    return alphabet_position(rotated_position, True)
  else: 
    return alphabet_position(rotated_position, False)

"""def alphabet_position(position_number, upper):
  character = chr(position_number + 65)
  if upper:
    return character
  else:
    return character.lower()"""

"""def rotate_character(letter, move):
  if letter.isupper():
    letterpos = ord(letter) - 65
  else:
    letterpos = ord(letter)-97
  rotated_position = (letterpos + move) % 26
  if letter.isupper():
    return alphabet_position(rotated_position, True)
  else: 
    return alphabet_position(rotated_position, False)
    """
