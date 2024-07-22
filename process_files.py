import os


def escape_string(s):
    return (
        s.replace("%", "%25")
        .replace("\n", "%0A")
        .replace("\r", "%0D")
        .replace("`", "%60")
    )


timestamp = escape_string(open("timestamp.txt").read().strip())
message = escape_string(open("message.txt").read().strip())

with open(os.environ["GITHUB_ENV"], "a") as env_file:
    env_file.write(f"TIMESTAMP={timestamp}\n")
    env_file.write(f"MESSAGE={message}\n")
