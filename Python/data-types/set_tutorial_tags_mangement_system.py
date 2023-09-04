# Initialize tag set
article_tags = set()

# Add tags
def add_tags(*tags):
    for tag in tags:
        article_tags.add(tag)
    print(f"Added tags: {tags}")

# Remove tags
def remove_tags(*tags):
    for tag in tags:
        article_tags.discard(tag)
    print(f"Removed tags: {tags}")

# Find common tags
def find_common_tags(other_tags):
    common_tags = article_tags.intersection(other_tags)
    print(f"Common tags: {common_tags}")

# Find unique tags
def find_unique_tags(other_tags):
    unique_tags = article_tags.difference(other_tags)
    print(f"Unique tags: {unique_tags}")

# Using the functions
add_tags("technology", "programming", "AI")
add_tags("data science", "machine learning")
print(f"Current tags: {article_tags}")

remove_tags("technology")
print(f"Current tags after removal: {article_tags}")

find_common_tags({"programming", "Python"})
find_unique_tags({"AI", "Python"})

