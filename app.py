from PIL import Image, ImageDraw, ImageFont
import os

# Initialize the images to be displayed
images = os.listdir('./assets/png')

# Dictionnary of images
images_dict = dict()
for file in images:
    images_dict.update( {file[:-4]:Image.open('./assets/png/'+file).copy()})

# Writing font
font = ImageFont.truetype('./assets/Arcade_Font.ttf',400)


def read_word(_input:str):
    """
    Translates a sentence into an array of image files

    Parameters
    ----------
    _input : str
        Combo inputs separated by a space for each section.

    Returns
    -------
    A list of PIL images or strings to be rendered.

    """
    # Array with a list of files for each segment of a combo
    result = []
    raw_result = []
    
    # Treat each "word" separately
    for word in _input.split():
        
        # Image files that will be added to result
        output = []
        raw_output = []
        
        
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
                
                # Check if char is a letter or a number
                try:
                    int(char)
                except ValueError:
                    # Check if char is a black arrow
                    if char == char.upper():
                        char += '_'
                
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
                output.append(images_dict[char])
                raw_output.append(char.replace('_',''))
            except KeyError:
                    
                    
                output.append(char)
                raw_output.append(char)
                i += len(char)-1
            
            # Increment i
            i += 1
        
        # Append the output list to the result list
        result.append(output.copy())
        raw_result.append(raw_output.copy())
    
    print(raw_result)
    return result , raw_result


def render(sentence:str,
           display = True,
           save = False,
           text = False):
    """
    Create a collage of the img_array

    Parameters
    ----------
    img_array : list
        List containing lists of either PIL images or strings to be rendered.

    Returns
    -------
    The final render

    """
    # Distance between two images
    separation = 20
    
    # Compute the size of the image
    if text:
        height = 1500
    else:
        height = 800
    
    x = 0
    
    # Convert the sentence into images to render
    img_array, text_array = read_word(sentence)
    
    # Check how many images will be put into the render
    for sequence in img_array:
        for button in sequence:
            if type(button) == str:
                x += 175*len(button)
            else:
                x += 800 + separation
        x += 400
    x -= 400 # Hide the last chevron
    
    # Image to display
    render = Image.new(mode = "RGBA",
                       size = (x,height))
    
    # Type text on the image
    pen = ImageDraw.Draw(render)
    
    # Add the images to the render
    x = 0
    for sequence in range(len(img_array)):
        
        for button in range(len(img_array[sequence])):
            x_ = x
            string = False
            
            # Rendering of known inputs
            try:
                render.paste(img_array[sequence][button], (x,0))
                x += 800 + separation
            # Rendering of text
            except ValueError:
                pen.text((x,200), img_array[sequence][button], font = font)
                string = True
                x += 175*len(img_array[sequence][button])
            
            # Draw the underlying text
            if text:
                offset = x-(x-x_)
                if not string:
                    offset += 250
                
                pen.text((offset,900),
                         text_array[sequence][button],
                         font = font)
            
                
        # Add a follow chevron
        render.paste(images_dict['follow'],(x,0))
        x += 400
        
    
    print(f"Size of the image: {x}px")
    
    
    
    # Save the file
    if save:
        print(f"Saving render as {sentence +'.png'}")
        render.save('./combos/'+sentence+'.png')
        
    # Display the render
    if display:
        render.show()
    
    return render
