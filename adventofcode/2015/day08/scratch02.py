import re

text = "Please contact support@example.com for assistance or info@domain.co for information."

# Define a regular expression pattern to match email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Use re.findall to find all email addresses in the text
matches = re.findall(pattern, text)

if matches:
    print("Found email addresses:")
    for match in matches:
        print(match)
else:
    print("No email addresses found.")
