# import re

# home_phone = ["4987651", "123987", "4560944"]
# print(home_phone)
# for home_phon in home_phone:
#     if re.match(r"^\d{7}$", home_phon):
#         print(f"number: {home_phon} :valid.")
#     else:
#         print(f"number: {home_phon} :invalid.")

# mobile_phone = ["+380631234567", "+380631674567", "3806236745671"]
# print(mobile_phone)
# for mobile_phone1 in mobile_phone:
#     if re.match(r"^[+]+?\d{12}$", mobile_phone1):
#         print(f"number: {mobile_phone1} :valid.")
#     else:
#         print(f"number: {mobile_phone1} :invalid.")

# emeils = ["ivan.ivanov@gmail.com", "ivanivanov@gmail.com", "ivanivanov@gmailcom",
#           "ivanivanovgmailcom", "ivanivanovgmail.com", "12ivanivanovgmail.com"]
# for emeil in emeils:
#     if re.match(r"^[a-zA-Z]+[. _]?[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,}$", emeil):
#         print(f"emeil {emeil} valid")
#     else:
#         print(f"emeil {emeil} invalid")

# fio = "Kalinichenko Andrii Andriyovich"
# if re.match(r"^[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}$", fio):
#     print("Correct")
# else:
#     print("Incorrect")

# passwords = "Admin124!"
# if re.match(r"^.*(?=.{8,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!*@#$%^&+=]).*$", passwords):
#     print("Correct")
# else:
#     print("Incorrect")

