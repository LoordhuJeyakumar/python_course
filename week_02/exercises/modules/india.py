import random

# Capital india
capital = "New Delhi"

# Population of india
population = 130000000

# Area of india
area = 3287590


def randomFact():
    facts = [
        "The capital of India is New Delhi.",
        "India has a population of over 130 crore.",
        "The area of India is 3,287,590 square kilometers.",
        "India is known for its rich cultural heritage.",
        "The Indian economy is one of the largest in the world.",
        "India is a diverse country with many languages spoken.",
        "The national animal of India is the Bengal tiger.",
        "India is the second-largest consumer of chocolate.",
        "The national sport of India is cricket.",
        "India is a land of diversity, with a rich history and culture."
    ]

    print(random.choice(facts))


if __name__ == "__main__":
    randomFact()