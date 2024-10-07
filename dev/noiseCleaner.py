import os
import re

# Directory where the .txt files are located
input_directory = "/Users/joeylukner/Documents/HanSentences"
output_file = "output_cleaned_lines_with_all_filters.txt"

# List of keywords to remove lines containing them (case insensitive)
keywords = [
    "Perfective", "Imperfective", "Dh-Perfective", "Customary",
    "semeliterative", "Inceptive", "Construction", "Future"
]

# Compile regex patterns
pattern_backtick_singlequote = re.compile(r"`.*?'")
pattern_backtick_to_end = re.compile(r"`.*")
pattern_angle_brackets = re.compile(r"<.*?>|<")
pattern_parentheses = re.compile(r"\(.*?\)")
pattern_colon = re.compile(r"^.*?:")
pattern_zero = re.compile(r'\bzero\b', re.IGNORECASE)
pattern_and = re.compile(r'\band\b', re.IGNORECASE)
pattern_3o = re.compile(r'.*?3o.*?')
pattern_p_dash = re.compile(r'P-')

with open(output_file, 'w') as outfile:
    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_directory, filename)
            with open(file_path, 'r') as infile:
                # Process each line in the file
                for line in infile:
                    # Skip lines containing any of the keywords (case insensitive)
                    if any(keyword.lower() in line.lower() for keyword in keywords):
                        continue
                    
                    
                    # Remove text between the backtick (`) and single quote (')
                    cleaned_line = re.sub(pattern_backtick_singlequote, "", line).strip()
                    # Remove text from the backtick (`) to EOL
                    cleaned_line = re.sub(pattern_backtick_to_end, "", cleaned_line).strip()

                    # Skip lines with < > or just <
                    if re.search(pattern_angle_brackets, cleaned_line):
                        continue
                    
                    # Remove everything before and including the colon if it exists
                    cleaned_line = re.sub(pattern_colon, "", cleaned_line).strip()
                    # Remove parentheses but keep the content inside
                    cleaned_line = re.sub(pattern_parentheses, "", cleaned_line).strip()
                    # Remove "zero"
                    cleaned_line = re.sub(pattern_zero, "", cleaned_line).strip()
                    # Remove "and"
                    cleaned_line = re.sub(pattern_and, "", cleaned_line).strip()
                    # Remove "3o" and any characters it is touching
                    cleaned_line = re.sub(pattern_3o, "", cleaned_line).strip()
                    # Remove "P-" but keep the rest of the line
                    cleaned_line = re.sub(pattern_p_dash, "", cleaned_line).strip()
                    
                    # Write to the output file, if non-empty
                    if cleaned_line:
                        outfile.write(cleaned_line + '\n')

print(f"written to {output_file}")
