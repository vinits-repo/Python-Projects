import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your phone number with +91: ")

phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
provider = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print(phone)
print(time)
print(provider)
print(reg)