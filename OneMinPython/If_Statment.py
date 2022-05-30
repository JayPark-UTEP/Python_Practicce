weather = input("What is the weather? ")

if weather == "Rain" or weather == "Snow":
    print("Get your umbrella")
elif weather == "Hot":
    print("Get and drink water")
else:
    print("Nothing to prepare")

temp = int(input("What is the temperature?"))
if temp >= 100:
    print("Too hot, stay inside")
elif 100 > temp >= 20:
    print("Have a great day!")
else:
    print("Too cold, stay inside")