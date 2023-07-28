# This is a simple Script ro read Video files from a directory 
# and the Change their names
# based on what you want.

import os

# User-defined string to use for the file names : prefix
my_string = "dep_client_02_"

# Counter to keep track of the file names
counter = 1

# specify your path here
input_dir = "E:\Arman\My Project\Project 48 - AiMental\Artificial Intelligence\DataSet\Therapy session - Video\Depression 02\Cropped_video"

# Create output directory if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")

# Loop through all video files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith(".mp4") or file_name.endswith(".avi") or file_name.endswith(".flv"):
        # Generate a new name for the file using the user-defined string and the counter
        # user-defined string + Counter
        new_name = my_string + str(counter) + os.path.splitext(file_name)[1]
        
        # Read the video file
        video_path = os.path.join(input_dir, file_name)
        
        # Write the video file with the new name to the output directory
        output_path = os.path.join("output", new_name)
        with open(video_path, "rb") as f_in, open(output_path, "wb") as f_out:
            f_out.write(f_in.read())
        
        # Increment the counter for the next file
        counter += 1