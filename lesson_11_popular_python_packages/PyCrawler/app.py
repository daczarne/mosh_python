import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")
questions = soup.select(".question-summary")

# questions is an instance of class bs4.element.ResultSet (a list)
print("type:", type(questions))

# each item on the list is an instance of class bs4.element.Tag
print("type:", type(questions[0]))

# class attrs are stored in a dictionary
print("attrs type:", type(questions[0].attrs))
print("attrs:", questions[0].attrs)

# We don't need to use the .attrs attribute, we can use []
print("attr id:", questions[0].get("id", 0))

# Now we need to get the title for each question

# The tag object also has a select method.
# We use it to select the .question-hyperlink CSS selector
print(questions[0].select(".question-hyperlink"))

# This selects the anchor tag in the HTML
# Since we know that each question has only one title, we don't need a list
print(questions[0].select_one(".question-hyperlink"))

# Now we need to get the acctual title of the question
print("qst title:", questions[0].select_one(".question-hyperlink").getText())

print("##### QUESTIONS #####")
# Now we need to iterate over each question and get their titles
for question in questions:
    print(question.select_one(".question-hyperlink").getText())

print("##### VOTES #####")
# The last step is to get the votes for each question
for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())

# To get all pages, first you'll need to find the pagination component
# For it, you'll extract the number of the last page and use it as range
# Then you'll run the same logic, inside of a loop
