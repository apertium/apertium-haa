import os
import re

# Directory where the .txt files are located
input_directory = "/Users/joeylukner/Documents/HanSentences/Input"
output_file = "output_filtered_lines.txt"

# Regex pattern to detect lines containing a colon
pattern_colon = re.compile(r":")

# Regex pattern to detect lines starting with "P-"
pattern_p_dash = re.compile(r"^P-")

# Regex pattern to remove sequences between square brackets
pattern_square_brackets = re.compile(r"\[.*?\]")

# Regex pattern to remove everything from the backtick to the end of the line
pattern_backtick_to_end = re.compile(r"`.*")

with open(output_file, 'w') as outfile:
    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_directory, filename)
            with open(file_path, 'r') as infile:
                # Process each line in the file
                for line in infile:
                    # Strip leading/trailing whitespace
                    stripped_line = line.strip()
                    
                    # Skip lines that contain a colon
                    if re.search(pattern_colon, stripped_line):
                        continue
                    
                    # Skip lines that start with "P-"
                    if re.match(pattern_p_dash, stripped_line):
                        continue
                    
                    # Remove sequences between square brackets
                    cleaned_line = re.sub(pattern_square_brackets, "", stripped_line).strip()
                    
                    # Remove sequences from backtick to the end of the line
                    cleaned_line = re.sub(pattern_backtick_to_end, "", cleaned_line).strip()
                    
                    # Write the cleaned line to the output file if not empty
                    if cleaned_line:
                        outfile.write(cleaned_line + '\n')

print(f"Filtered lines written to {output_file}")
