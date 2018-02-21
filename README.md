# Regex e-mail and phone scraper
This Python script extracts e-mails and phone numbers from either the clipboard using the `pyperclip` module or to a variable that can be printed.

It follows the tutorial in the *Automate the boring stuff with Python programming* course.

## Variables
* `phoneRegex` is the regular expression to capture phone numbers in various formats 
* `emailRegex` is the regular expression to capture email addresses
* `text` is the variable that stores the text copied to the clipboard using `pyperclip`

## Use
If using the `pyperclip` option, just hit ctrl-a and ctrl-c on the document that needs scraping and then run the script. The emails and phone numbers should be stored to the clipboard.

If storing results to view in shell or copy out, comment out `pyperclip` lines and uncomment the `from otherFileWithText import variableStoringString` line as well as the final print statements 