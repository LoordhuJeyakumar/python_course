country_capitals ={
    "USA": "Washington D.C",
    "France": "Paris",
    "Japan": "Tokyo"
}

print(country_capitals)
print("capital of france:", country_capitals["France"])
print("capital of germany:", country_capitals("Germany","Not found"))


2
country_capitals ={
    "USA": "Washington D.C",
    "France": "Paris",
    'Japan': "Tokyo"
}

print("Initial Dictionary:", country_capitals)
country_capitals["India"]= "New Delhi"
print("After adding India:", country_capitals)

country_capitals["USA"]="Washington, D.C"
print("Updating USA captial:", country_capitals)

del country_capitals["france"]
print("removing France:", country_capitals)


3
item_prices = {"apple": 1.0, "banana": 0.5, "Orange": 0.8, "grape": 2.5}
print("keys:", list(item_prices()))
print("values:", list(item_prices.values()))
print("items:", list(item_prices.items()))
removed_price = item_prices.pop("banana")
print("Banana price remove:", removed_price)
item_prices.clear()
print("Clear Dict:", item_prices)


4
student_grades = {"Alice":85, "Bob":92, "Charlie":78, "David":90}
print("student grade:")
for name, grade in student_grades.items():
    print(f"{name}: {grade}")


5
library ={
    "Fiction": [ 
        {"Title": "Harry Potter", "Author": "J.K Rowling", "Year":'1997'},
        {"Title": "The Alchemist", "Author": "Paulo Coelho", "Year": "1988" }

    ],
    "Science": [
    
        {"Title": "The orgin of spices", "Author":"Charles Darwin", "Year": "1859"},
        {"Title":"The Gene", "Author":"Siddhartha Mukherjee", "Year": "2010" }
    ]

}

print("Library Dictionary:")
print(library)
print("\nFirst Fiction Book title:")
print(library["Fiction"]["Title"])
print("\nScience Books:")
for book in library["Science"]:
    print(f"Title:{book['title']}, Author: {book["Author"]}")

