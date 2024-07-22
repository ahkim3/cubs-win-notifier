import statsapi
import datetime
from email_handler import send_email_notification

# Grab recipient from recipient.txt
with open("recipient.txt", "r") as recipient_file:
    RECIPIENT = recipient_file.read().strip()


def send_notification(message):
    recipient = RECIPIENT
    subject = "Cubs Win Notifier"
    body = message
    send_email_notification(recipient, subject, body)


def check_cubs_game():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    games = statsapi.schedule(start_date=today, end_date=today, team=112)

    for game in games:
        if game["venue_name"] == "Wrigley Field":
            opponent = game["away_name"]

            if game["status"] == "Final":
                home_score = game["home_score"]
                away_score = game["away_score"]
                if home_score > away_score:
                    message = f"The Cubs won their home game against the {opponent}. Open the CFA app for free food!"
                    send_notification(message)
                else:
                    print("The Cubs lost at home. No notification sent.")
            elif game["status"] == "In Progress":
                message = f"The Cubs are currently playing the {opponent}."
                send_notification(message)
            elif game["status"] == "Scheduled" or game["status"] == "Pre-Game":
                game_time = game["game_datetime"]

                # Get rid of date if date is today
                if game_time[:10] == today:
                    game_time = game_time[11:16]
                else:
                    game_time = game_time

                # Convert from UTC to CDT
                game_time = datetime.datetime.strptime(game_time, "%H:%M")
                cdt_timezone = datetime.timezone(datetime.timedelta(hours=-5))
                game_time = (
                    game_time.replace(tzinfo=datetime.timezone.utc)
                    .astimezone(cdt_timezone)
                    .strftime("%I:%M%p")
                )

                message = (
                    f"The Cubs will be playing the {opponent} at home at {game_time}."
                )
                send_notification(message)
            else:
                message = f"The Cubs will be playing the {opponent} at home today, but the game status is unknown. Debug info: {game['status']}"
                send_notification(message)

            print(message)
            break

        else:
            print("The Cubs are not playing at home today. No notification sent.")
            break


if __name__ == "__main__":
    print(
        "Today is "
        + datetime.datetime.now().strftime("%A, %B %d, %Y")
        + ". The time is "
        + datetime.datetime.now().strftime("%I:%M%p")
        + "."
    )
    check_cubs_game()
    print()
