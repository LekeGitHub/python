# This oython is about MTN Support
import time

print("Products & Services FAQ's\n"
      "")
products = ["a. 5G Broadband Router", "b. MTN Broadband MiFi", "c. 4G Router (Standard)", "d. BizPlus Bundles"]

# For Loop
for each_product in products:
    print(each_product)
    time.sleep(1)

print("")
resp = input("Select from the categories above for support: ").capitalize()
if resp == 'A' or resp == "5G Broadband Router":
    print("Here are some frequently asked question:")
    print("_____________________________________;)")
    print("What is the benefit of using the MTN 5G router?\n"
          "5G offers higher internet speed and faster downloads than 4G and other bands,\n"
          " it can also connect up to 32-64 devices simultaneously for home and office use.\n"
          "")
    print("Does the 5G router come with any data bonus?\n"
          "Yes, you enjoy multiple data bonus as seen below,\n"
          "The 5G broadband router is bundled with 100GB data accessible upon activation and valid for 30 days.")

elif resp == 'B' or resp == "MTN Broadband MiFi":
