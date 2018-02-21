#! python3

import re, pyperclip
# from otherFileWithText import variableStoringString

'''
Psuedocode
1. Create regex for phone numbers
2. Create regex for emails
3. Get text off clipboard
4. Extract phone and email from clipboard
5. Copy extracted phone and email to clipboard

'''
# 1. Phone regex
phoneRegex = re.compile(r'''
# Number types 415-555-0000, 555-000, (415) 555-0000, 555-0000 ext 12345, ext. 1234, x12345
(((\d\d\d)|(\(\d\d\d\)))?	# area code (optional)
(\s|-)						# first separator
\d\d\d						# first three digits
-							# second separator
\d\d\d\d					# last 4 digits
(((ext(\.)?\s)|x)			# extenstion word part (optional)
(\d{2,5}))?)				# extension number part (optional)
''', re.VERBOSE)

# 2. email regex
emailRegex = re.compile(r'''
# some.thing+under_scores@something.com / .ca / .edu / .net
[a-zA-Z0-9_.+]+			# name part
@						# @ symbol
[a-zA-Z0-9_.+]+			# domain name part
''', re.VERBOSE)

# 3. Get text off clipboard
# Use one of the following
text = pyperclip.paste()  # 1. To copy from clipboard
# text = regexProjectText # 2. If text is in another file (likned above)

# 4. Extract email and phone off text
extractedPhones = phoneRegex.findall(text)
extractedEmailAddresses = emailRegex.findall(text)

# Grab the phone numbers from the first element of each tuple in the resulting list of tuples
allPhoneNumbers = [i[0] for i in extractedPhones]

# Store the emails and phone numbers on new lines and store in a single variable
results = '\n'.join(allPhoneNumbers) + '\n'.join(extractedEmailAddresses) 

# 5. Copy results to clipboard
# Either print results or copy to clipboard
# print(allPhoneNumbers)
# print(extractedEmailAddresses)
# print(results)
pyperclip.copy(results)