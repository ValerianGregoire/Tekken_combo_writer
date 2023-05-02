import tkinter as tk
from PIL import Image

# Image files
images = {
    
    # Arrows
    "f" : "f.jpg",
    "df" : "df.jpg",
    "d" : "d.jpg",
    "db" : "db.jpg",
    "b" : "b.jpg",
    "ub" : "ub.jpg",
    "u" : "u.jpg",
    "uf" : "uf.jpg",
    
    # Black Arrows
    "F" : "F.jpg",
    "DF" : "DF.jpg",
    "D" : "D.jpg",
    "DB" : "DB.jpg",
    "B" : "B.jpg",
    "UB" : "UB.jpg",
    "U" : "U.jpg",
    "UF" : "UF.jpg",
    
    # Attacks
    "1" : "1.jpg",
    "2" : "2.jpg",
    "3" : "3.jpg",
    "4" : "4.jpg",
    "12" : "12.jpg",
    "13" : "13.jpg",
    "14" : "14.jpg",
    "23" : "23.jpg",
    "24" : "24.jpg",
    "34" : "34.jpg"
    
    
    
    
    
    
    
    }

def read_word(_input:str):
    """
    Translates a sentence into an array of image files

    Parameters
    ----------
    word : str
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # Array with a list of files for each segment of a combo
    result = []
    
    # Treat each "word" separately
    for word in _input.split():
        
        # Image files that will be added to result
        output = []
        
        
        # Check each character
        i = 0
        while i < len(word):
            char = word[i]
            
            # If last char of the word
            if i < len(word) - 1:
                # Check for white diagonal directions
                if char == 'd' or char == 'u':
                    if word[i+1] == 'f' or word[i+1] == 'b':
                        char = word[i:i+2]
                        i += 1
                        
                # Check for black diagonal directions
                if char == 'D' or char == 'U':
                    if word[i+1] == 'F' or word[i+1] == 'B':
                        char = word[i:i+2]
                        i += 1
                
                # Check for multiple-presses
                if char == '1' or char == '2' or char == '3' or char == '4':
                    if word[i+1] == '+':
                        char = word[i]+word[i+2]
                        
                        # Reorder the numbers if needed
                        if int(char[0])>int(char[1]):
                            char = word[i+2]+word[i]
                        
                        i += 2
    
            # Append the current word to the output list
            try:
                output.append(images[char])
            except KeyError:
                output.append(word)
                break
            
            # Increment i
            i += 1
        
        # Append the output list to the result list
        result.append(output.copy())
    
    return result

def plot():
    pass
    return



combo = 'd4+3 d124 323'
print(read_word(combo))






















