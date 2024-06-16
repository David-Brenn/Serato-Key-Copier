import os
import glob
import xml.etree.ElementTree as ET

# Boolean for key format
# True: Camelot
# False: Open Key
CAMELOT_FORMAT = True


# Zero Width Space character
zero_width_space = "\u200B"

# Object for key format conversion
open_key_to_camelot = {
    "G#m": "1A",
    "Abm": "1A​",
    "D#m": "2A",
    "Ebm": "2A",
    "A#m": "3A",
    "Bbm": "3A",
    "Fm": "4A",
    "Cm": "5A",
    "Gm": "6A",
    "Dm": "7A",
    "Am": "8A",
    "Em": "9A",
    "Bm": "10A",
    "F#m": "11A",
    "C#m": "12A",
    "B": "1B",
    "F#": "2B",
    "Gb": "2B",
    "C#": "3B",
    "Db": "3B",
    "G#": "4B",
    "Ab": "4B",
    "D#": "5B",
    "Eb": "5B",
    "A#": "6B",
    "Bb": "6B",
    "F": "7B",
    "C": "8B",
    "G": "9B",
    "D": "10B",
    "A": "11B",
    "E": "12B"
}

camelot_key_to_open = {
    "1A": "G#m",
    "2A": "D#m",
    "3A": "A#m",
    "4A": "Fm",
    "5A": "Cm",
    "6A": "Gm",
    "7A": "Dm",
    "8A": "Am",
    "9A": "Em",
    "10A": "Bm",
    "11A": "F#m",
    "12A": "C#m",
    "1B": "B",
    "2B": "F#",
    "3B": "C#",
    "4B": "G#",
    "5B": "D#",
    "6B": "A#",
    "7B": "F",
    "8B": "C",
    "9B": "G",
    "10B": "D",
    "11B": "A",
    "12B": "E"
}


def copy_key_to_comments(xml_file_path):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    # Find the Key and Comments elements
    key_element = root.find('Key')
    comments_element = root.find('Comments')

    # Check if file was already processed
    if comments_element.text and zero_width_space in comments_element.text:
        print("Key value already copied to Comments.")
        return
    
    if key_element is not None and comments_element is not None:
        # Get the value of the Key element
        key_value = key_element.text
        
        # Convert the key value to Camelot format if necessary
        if key_value:
            if CAMELOT_FORMAT:
                key_value = open_key_to_camelot.get(key_value, key_value)
        print(CAMELOT_FORMAT)
        print("Key Value: " + key_value)
        # Append the key value to the Comments element
        if key_value:
            if comments_element.text:
                comments_element.text = f'{key_value}{zero_width_space} {comments_element.text}'
            else:
                comments_element.text = f' {key_value}{zero_width_space}'
        
        # Write the modified XML back to the file
        tree.write(xml_file_path)
        print("Key value has been copied to Comments successfully.")
    else:
        print("Key or Comments element not found in the XML.")

def process_folder(folder_path):
    # Find all XML files in the given folder
    xml_files = glob.glob(os.path.join(folder_path, '*.xml'))
    
    # Apply the copy_key_to_comments function to each XML file found
    for xml_file in xml_files:
        copy_key_to_comments(xml_file)

# Get the folder path and user preference for key format
folder_path = input("Enter the path to the folder containing XML files: ")
user_input = input("Choose Key Format: Camelot (1) or Open Key (2): ")
if user_input == '1':
    CAMELOT_FORMAT = True
elif user_input == '2':
    CAMELOT_FORMAT = False
else:
    print("Invalid input. Defaulting to Camelot format.")
    CAMELOT_FORMAT = True


# Path to your XML file
xml_file_path = '/Users/davidbrenn/Music/_Serato_/Metadata/SoundCloud/'

process_folder(folder_path)

