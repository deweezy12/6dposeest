import os

# Directory containing the .txt files
directory = 'C:/python_work/singleshotpose/LINEMOD/4klegomix4_2/labels'

# Loop through each .txt file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        
        # Read the contents of the .txt file
        with open(file_path, 'r') as file:
            content = file.read().strip()
            
        # Split the content by spaces to get individual numbers
        numbers = content.split(' ')
        
        # Delete the 2nd to 5th number
        # del numbers[1:5]

        # Delete the 8th and 9thrd number
        # del numbers[6:8]

        # Delete the 12th and 13th number
        # del numbers[9:11]
        
        # Delete the 16th and 17th number
        # del numbers[12:14]

        del numbers[1]
        del numbers[1]
        del numbers[1]
        del numbers[1]
        del numbers[3]
        del numbers[3]
        del numbers[5]
        del numbers[5]
        del numbers[7]
        del numbers[7]

        
        # Join the remaining numbers back into a string
        content = ' '.join(numbers)
        
        # Write the updated content back to the .txt file
        with open(file_path, 'w') as file:
            file.write(content)
            
        print(f'Successfully updated {filename}.')