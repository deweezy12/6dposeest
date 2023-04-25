import os
from PIL import Image, ImageOps

def find_highest_difference(dir_path):
    """
    Find the highest difference between pairs of numbers in text files in a directory.
    
    Args:
        dir_path (str): The directory path containing the text files.
    
    Returns:
        float: The highest difference found.
    """
    # Append "/labels" to the directory path
    dir_path = os.path.join(dir_path, "labels")
    # Initialize a variable to store the highest difference found
    highest_diff = 0

    # Loop through each file in the directory
    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(dir_path, filename)

            # Open the file and read each line
            with open(file_path, "r") as f:
                for line in f:
                    # Split the line into a list of numbers
                    nums = [float(num) for num in line.strip().split(" ")[1:19]]

                    # Find the highest difference between all pairs of numbers
                    for i in range(len(nums)):
                        for j in range(i+1, len(nums)):
                            diff = abs(nums[i] - nums[j])
                            if diff > highest_diff:
                                highest_diff = diff

    return highest_diff

def replace_string_in_file(file_name, target_string, replacement_string):
    """
    Replace a target string with a replacement string in a given file.

    Args:
        file_name (str): Name of the file to be read and modified.
        target_string (str): String to be replaced in the file.
        replacement_string (str): String to replace the target string.

    Returns:
        None
    """
    # Read in the file
    with open(file_name, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(target_string, replacement_string)

    # Write the file out again
    with open(file_name, 'w') as file:
        file.write(filedata)

def convert_units(filename):
    with open(filename, 'r') as f:
        contents = f.readlines()

    # Find the line that specifies the vertex count
    vertex_count_line = [l for l in contents if 'element vertex' in l][0]

    # Extract the vertex count
    vertex_count = int(vertex_count_line.split()[2])

    # Find the lines that contain vertex data
    vertex_data_lines = contents[contents.index('end_header\n') + 1: contents.index('end_header\n') + 1 + vertex_count]

    # Convert the vertex data from inches to centimeters
    new_vertex_data_lines = []
    for line in vertex_data_lines:
        x, y, z = map(float, line.split()[:3])
        new_vertex_data_lines.append(f'{x * 2.54} {y * 2.54} {z * 2.54}\n')

    # Replace the old vertex data with the new vertex data
    start = contents.index('end_header\n') + 1
    end = start + vertex_count
    contents[start:end] = new_vertex_data_lines

    # Write the updated contents back to the file
    with open(filename, 'w') as f:
        f.writelines(contents)

def rename_files(folder_path):
    i = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            old_file_name = os.path.join(folder_path, filename)
            new_file_name = os.path.join(folder_path, str(i).zfill(6) + ".jpg")
            os.rename(old_file_name, new_file_name)
            i += 1


def change_format(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            img = Image.open(os.path.join(folder_path, filename))
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            new_filename = os.path.splitext(filename)[0] + '.jpg'
            img.save(os.path.join(folder_path, new_filename), 'JPEG')

def create_mask(folder_path, output_path):
    i = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):

            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            gray_image = ImageOps.grayscale(image)
            bw_image = gray_image.point(lambda x: 255 if x > threshold_value else 0, mode='1')
            mask = ImageOps.invert(bw_image)

            mask_filename = f"{i:04d}.png"
            mask_path = os.path.join(output_path, mask_filename)
            mask.save(mask_path)
            i += 1


# Example usage:
dir_path = "C:/python_work/singleshotpose/LINEMOD/legobrick1_1/"
threshold_value = 69.99

create_mask(dir_path +"JPEGImages", dir_path +"mask")


replace_string_in_file('test.txt', 'cam', 'legobrick1_1')
replace_string_in_file('train.txt', 'cam', 'legobrick1_1')

convert_units("legobrick1_1.ply")

change_format(dir_path+"JPEGImages")

rename_files(dir_path+"JPEGImages")

print("The biggest diam is:", highest_diff)
