import os
import re


def read_and_escape(file_path):
    # Read the content of the file and escape special characters
    with open(file_path, "r") as file:
        content = file.read().strip()
    return content


def update_readme(readme_path, timestamp, message):
    # Read the README file content
    with open(readme_path, "r") as file:
        content = file.read()

    # Replace the timestamp section with the new content including backticks
    content = re.sub(
        r"<!-- start-timestamp -->.*?<!-- end-timestamp -->",
        f"<!-- start-timestamp -->\n`{timestamp}`\n<!-- end-timestamp -->",
        content,
        flags=re.DOTALL,
    )

    # Replace the message section with the new content including backticks
    content = re.sub(
        r"<!-- start-message -->.*?<!-- end-message -->",
        f"<!-- start-message -->\n```\n{message}\n```\n<!-- end-message -->",
        content,
        flags=re.DOTALL,
    )

    # Write the updated content back to the README file
    with open(readme_path, "w") as file:
        file.write(content)
        print("README.md updated successfully!")


def main():
    # Read and escape the content of timestamp.txt and message.txt
    timestamp = read_and_escape("timestamp.txt")
    message = read_and_escape("message.txt")

    # Update the README file
    update_readme("README.md", timestamp, message)


if __name__ == "__main__":
    main()
