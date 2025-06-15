# job_title_generator.py

import random

adjectives = ["Certified", "Dynamic", "Innovative", "Global", "Legendary"]
roles = ["Meme", "Unicorn", "Cloud", "Blockchain", "Emoji"]
suffixes = ["Strategist", "Engineer", "Guru", "Evangelist", "Architect"]

def generate_job_title():
    adjective = random.choice(adjectives)
    role = random.choice(roles)
    suffix = random.choice(suffixes)
    return f"{adjective} {role} {suffix}"

while True:
    print("Your fake job title is:", generate_job_title())
    again = input("Want another one? (yes/no): ").strip().lower()
    if again != "yes":
        break
