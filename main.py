import re

home_phone = ["4987651", "123987", "4560944"]
print(home_phone)
for home_phon in home_phone:
    if re.match(r"^\d{7}$", home_phon):
        print(f"number: {home_phon} :valid.")
    else:
        print(f"number: {home_phon} :invalid.")

mobile_phone = ["+380631234567", "+380631674567", "3806236745671"]
print(mobile_phone)
for mobile_phone1 in mobile_phone:
    if re.match(r"^[+]+?\d{12}$", mobile_phone1):
        print(f"number: {mobile_phone1} :valid.")
    else:
        print(f"number: {mobile_phone1} :invalid.")

