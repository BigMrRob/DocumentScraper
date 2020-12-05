#! python3

import re, pyperclip

# **This program uses VERBOSE mode for simplication of REGEX/Inclusion of Comments

# Regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))? # With/Without Parenthese on Area Code (optional)
(\s|-)                   # First Separator
\d\d\d                   # Second Three Digits
-                        # Second Separator
\d\d\d\d                 # Last Four Numbers
(((ext(\.)?\s)|x)        # Extension Word Part (optional)
(\d{2,5}))?              # Extension Number Part (optional)
)
''', re.VERBOSE)

# Regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ # Name 
@               # @ Symbol
[a-zA-Z0-9_.+]+ # Domain Name
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from the text
extractedNumber = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for item in extractedNumber:
    allPhoneNumbers.append(item[0])

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
