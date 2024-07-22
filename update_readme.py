import os

# Read and escape the content of the files
timestamp = open("timestamp.txt", "r").read()
message = open("message.txt", "r").read()

# Read the README file
with open("README.md", "r") as file:
    content = file.read()

# Replace the placeholders with the actual content, including backticks
content = content.replace(
    "<!-- start-timestamp -->\n<!-- end-timestamp -->",
    f"<!-- start-timestamp -->\n`{timestamp}`\n<!-- end-timestamp -->",
)
content = content.replace(
    "<!-- start-message -->\n<!-- end-message -->",
    f"<!-- start-message -->\n```\n{message}\n```\n<!-- end-message -->",
)

# Write the updated content back to the README file
with open("README.md", "w") as file:
    file.write(content)
    print("README.md updated successfully!")
