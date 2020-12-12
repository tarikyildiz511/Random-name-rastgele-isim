
import random
def generate_name():
    adlar = ["Bill","Jeff","Elon","Mark","Grant","Gary","Jack","Gaben"]
    soyadlar = ["Gates","Musk","Bezos","Zuckerberg","Cardone","Vaynerchuk","Ma","Newell"]

    return "{} {}".format(random.choice(adlar),random.choice(soyadlar))

for x in range(5):
    print(generate_name())