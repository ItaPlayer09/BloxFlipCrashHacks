import time
import os
from datetime import datetime

os.system('title GetValuesScript')
oggi = datetime.today().strftime('%Y%m%d')
oggiSlashs = datetime.today().strftime('%d-%m-%Y')

def calculate_statistics(numbers):
    total = 0.0
    length = 0
    below_1_1 = 0
    cifre_Media = 0
    
    for amount in numbers:
        total += amount
        length += 1
        
        if amount < 1.1:
            below_1_1 += 1

    

    average = total / length
    rate = length / below_1_1
    return average, below_1_1, rate

def main():
    try:
        filename = f"Valori{oggi}.txt"  # Ask for filename once

        while True:  # Infinite loop
            time.sleep(1)
            os.system('clear')

            with open(filename, 'r') as infile:
                numbers = [float(line) for line in infile]

            average, below_1_1, rate = calculate_statistics(numbers)
            
            length = rate*below_1_1

            # Store results in separate files
            with open('Numbers.txt', 'w') as count_file:
                count_file.write(f'{len(numbers)}')

            with open('Media.txt', 'w') as avg_file:
                avg_file.write(f'Media: {average:.2f}')

            with open('Failed.txt', 'w') as below_file:
                below_file.write(f'{below_1_1}')


            if length > 99:
                if below_1_1 > 9 :
                    print(f'Numeri: {len(numbers)} (Best: Inf, Must be: 99+)')
                else:
                    print(f'Numeri: 0{len(numbers)} (Best: Inf, Must be: 99+)')
            else:
                if below_1_1 > 9:
                    print(f'Numeri: 0{len(numbers)} (Best: Inf, Must be: 99+)')
                else:
                    print(f'Numeri: {len(numbers)} (Best: Inf, Must be: 99+)')

            if length > 99:
                if below_1_1 > 9:
                    print(f'Media: {round(average, 2)} (Best: Any, Must be: Any)')
                else:
                    print(f'Media: {round(average, 1)} (Best: Any, Must be: Any)')
            else:
                if below_1_1 > 9:
                    print(f'Media: {round(average, 2)} (Best: Any, Must be: Any)')
                else:
                    print(f'Media: {round(average, 1)} (Best: Any, Must be: Any)')

            if length > 99:
                if below_1_1 > 9:
                    print(f'Falliti: {below_1_1} (Best: Any, Must be: Any)')
                else:
                    print(f'Falliti: 0{below_1_1} (Best: Any, Must be: Any)')
            else:
                if below_1_1 > 9:
                    print(f'Falliti: {below_1_1} (Best: Any, Must be: Any)')
                else:
                    print(f'Falliti: {below_1_1} (Best: Any, Must be: Any)')

            if length > 99:
                if below_1_1 > 9:
                    print(f'Rate: {round(rate, 2)} (Best: 7.5, Must be: 7-8)')
                else:
                    print(f'Rate: 0{round(rate, 2)} (Best: 7.5, Must be: 7-8)')
            else:
                if below_1_1 > 9:
                    print(f'Rate: 0{round(rate, 2)} (Best: 7.5, Must be: 7-8)')

                else:
                    print(f'Rate: 0{round(rate, 1)} (Best: 7.5, Must be: 7-8)')


            print(f'')
            print(f'Play mode: 1/8')
            print(f'Safe: 1-5')
            print(f'Risk: 6')
            print(f'Loss: 7-8')
            print(f'')
            print(f'Running on: {oggiSlashs}')
        
    except FileNotFoundError:
        filename = f'Valori{oggi}.txt'
        with open(filename, 'w') as file:
            file.write("")
        print(f"File '{filename}' created successfully.")

    except ValueError:
        print('Non-numeric data found in the file.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    while True:
        main()

