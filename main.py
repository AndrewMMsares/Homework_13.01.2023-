import re

emeils = ["ivan.ivanov@gmail.com", "ivanivanov@gmail.com", "ivanivanov@gmailcom",
          "ivanivanovgmailcom", "ivanivanovgmail.com", "12ivanivanovgmail.com"]
for emeil in emeils:
    if re.match(r"^[a-zA-Z]+[. _]?[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,}$", emeil):
        print(f"emeil {emeil} valid")
    else:
        print(f"emeil {emeil} invalid")