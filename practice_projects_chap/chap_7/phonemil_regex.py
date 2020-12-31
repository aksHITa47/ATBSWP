import re, pyperclip
phoneRegex=re.compile(r'''(
(\(\d{2}\)|\d{2}|\(\d{4}\)|\d{4})?
(\s|-)?
(\d{10})
)''',re.VERBOSE)

emailRegex=re.compile(r'''(
[a-zA-Z0-9_.%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2-4})
)''',re.VERBOSE)

text=str(pyperclip.paste())
matches=[]
for i in phoneRegex.findall(text):
    phone='-'.join([i[1],i[5]])
    matches.append(phone)
for i in emailRegex.findall(text):
    matches.append(i[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
