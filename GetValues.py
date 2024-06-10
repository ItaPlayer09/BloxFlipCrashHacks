import time
import os
from datetime import datetime

os.system('title GetValuesScript')
oggi = datetime.today().strftime('%Y%m%d')
oggiSlashs = datetime.today().strftime('%d-%m-%Y')

def find_and_read_next(file_path, search_text, output_file):

    with open(output_file, 'w') as out_f:
        out_f.write("")  # Write an empty string to truncate the file



    with open(file_path) as f:
        file_contents = f.read()
        index = file_contents.find(search_text)
        while index != -1:
            next_chars = file_contents[index + len(search_text):index + len(search_text) + 4]

            if "an" in next_chars:
                result = next_chars[:2]
            else:
                result = next_chars

            with open(output_file, 'a') as out_f:
                out_f.write(result + '\n')
            
            index = file_contents.find(search_text, index + 1)

# Example usage:
file_path = 'log.log'
search_text = 'game end with '
output_file = f"Valori{oggi}.txt"
while True:
    time.sleep(1)
    os.system('cls')
    print(f"Script is running on: {oggiSlashs}")
    find_and_read_next(file_path, search_text, output_file)

