import re

fio = "Kalinichenko Andrii Andriyovich"
if re.match(r"^[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}$", fio):
    print("Correct")
else:
    print("Incorrect")