import pyperclip
import re
import pprint

phoneRegex = re.compile( r'''(
    (\d{3}|\(\d{3}\))?      # Area Code
    (\s|-|\.)?              # Seperator
    (\d{3})                 # 1st 3 digits
    (\s|-|\.)               # Seperator
    (\d{4})                 # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

emailRegex = re.compile( r'''(
    [a-zA-Z0-9.-_]+         # Username
    @                       # @
    [a-zA-Z0-9.-]+          # Domain name
    \.                      # .
    [a-zA-Z]{2,4}           # TLD
)''', re.VERBOSE)

clipboardData = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(clipboardData):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(clipboardData):
    matches.append(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard and written to phoneAndEmail.txt')
    f = open("phoneAndEmail.txt", "w+")
    f.write(pprint.pformat(matches))
    f.close
else:
    print('No phone numbers or email addresses found.')\