# sequence iterators

# way to dynamically print all blog posts in list?
blog_posts = [
    "",
    "The 20 coolest math functions in Python",
    "How HTTP works in Python",
    "A tutorial about data types",
    "",
]

for post in blog_posts:
    # do not print empty posts
    if post == "":
        continue
    else:
        print(post)  # print each element in list
print("--------------------")

# print each character in a string
myString = "this is my string "
for char in myString:
    print(char)
print("--------------------")

# define a specific number of iterations
for x in range(0, 10):
    print(x)

# loop through dictionary
print("--------------------")

person = {"Name:": "Karen Smith", "Age:": 25, "Gender:": "Female"}
for key in person:
    print(key, ":", person[key])  # nameOfDictionary[key variable]

# all of these can be nested

print("--------------------")

# creating a dictionary with nested list of keys and properties "languages and blog posts"
blog_posts = {
    "Python": [
        "The 20 coolest math functions in Python",
        "How HTTP works in Python",
        "A tutorial about data types",
    ],
    "Javascript": ["Namespaces in Javascript", "Foundational languages in Coding"],
}

# for in loop iterates through properties in a key and combinations thereof
# iterate through each category
for category in blog_posts:
    print("\nPosts about:", category)
    # iterate over list of each post
    for post in blog_posts[category]:
        print(post)