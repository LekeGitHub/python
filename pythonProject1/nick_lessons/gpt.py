# This code is similar to chat GPT

print("Hey there, Welcome to MTN customer support")
print("Kindly fill the form below")
full_name = input("Enter your full name: ")

print("Nice to meet you " + full_name)

print(".........Products and Services FAQs............\n"
      "a. 5G Broadband Router\n"
      "b. MTN Broadband MiFi?\n"
      "c. 4G Router (Standard)\n"
      "d. BizPlus Bundles\n"
      "\n")


resp = input("Select on of the categories above to get help. ").capitalize()
if resp == 'a' or '5G Broadband Router':


