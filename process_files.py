import os

timestamp = open("timestamp.txt").read()
message = open("message.txt").read()

with open(os.environ["GITHUB_ENV"], "a") as env_file:
    env_file.write(f"TIMESTAMP={timestamp}\n")
    env_file.write(f"MESSAGE={message}\n")
