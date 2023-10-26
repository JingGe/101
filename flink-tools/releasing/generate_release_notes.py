import re
import sys

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python reformat_script.py input_file output_file")
    sys.exit(1)

# Get the input and output file paths from command-line arguments
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# Read the input text from the input file
try:
    with open(input_file_path, "r") as file:
        input_text = file.read()
except FileNotFoundError:
    print(f"Input file '{input_file_path}' not found.")
    sys.exit(1)

# Split the input text into individual sections
sections = input_text.split('\n\n')

# Initialize the output
output_text = ''

# Iterate through the sections and reformat them
for section in sections:
    # Extract relevant information using regular expressions
    match = re.match(r'"([^"]+)"\s+"([^"]+)"\s+"([^"]+)"', section)

    if match:
        issue_id, title, description = match.groups()
        
        # Reformat the section
        formatted_section = f"#### {title}\n##### [{issue_id}](https://issues.apache.org/jira/browse/{issue_id})\n{description}\n\n"
        
        # Append the formatted section to the output
        output_text += formatted_section

# Write the reformatted text to the output file
with open(output_file_path, "w") as output_file:
    output_file.write(output_text)

print(f"Reformatted text saved to {output_file_path}")
