import statsapi
import tzlocal
from datetime import datetime, timezone, timedelta
from email_handler import send_email_notification

# Grab recipient from recipient.txt
with open("recipient.txt", "r") as recipient_file:
    RECIPIENT = recipient_file.read().strip()


def send_notification(message, CDT_TIMESTAMP):
    recipient = RECIPIENT
    subject = "Cubs Win Notifier"
    body = message
    send_email_notification(recipient, subject, body, CDT_TIMESTAMP)


def check_cubs_game(CDT_TIMESTAMP):
    today = datetime.now().strftime("%Y-%m-%d")
    games = statsapi.schedule(start_date=today, end_date=today, team=112)

    for game in games:
        if game["venue_name"] == "Wrigley Field":
            opponent = game["away_name"]

            if game["status"] == "Final":
                home_score = game["home_score"]
                away_score = game["away_score"]
                if home_score > away_score:
                    message = f"The Cubs won their home game against the {opponent}. Open the CFA app for free food!"
                    send_notification(message, CDT_TIMESTAMP)
                else:
                    print("The Cubs lost at home. No notification sent.")
            elif game["status"] == "In Progress":
                message = f"The Cubs are currently playing the {opponent}."
                send_notification(message, CDT_TIMESTAMP)
            elif game["status"] == "Scheduled" or game["status"] == "Pre-Game":
                game_time = game["game_datetime"]

                # Extract the time part from the game_time string
                game_time_extracted = game_time[11:16]

                # Convert from UTC to CDT
                game_time = datetime.strptime(game_time_extracted, "%H:%M")
                cdt_timezone = timezone(timedelta(hours=-5))
                game_time = (
                    game_time.replace(tzinfo=timezone.utc)
                    .astimezone(cdt_timezone)
                    .strftime("%I:%M%p")
                )

                message = (
                    f"The Cubs will be playing the {opponent} at home at {game_time}."
                )
                send_notification(message, CDT_TIMESTAMP)
            else:
                message = f"The Cubs will be playing the {opponent} at home today, but the game status is unknown. Debug info: {game['status']}"
                send_notification(message, CDT_TIMESTAMP)

            print(message)
            break

        else:
            print("The Cubs are not playing at home today. No notification sent.")
            break


if __name__ == "__main__":
    current_time = datetime.now()

    # Get the local timezone
    local_timezone = tzlocal.get_localzone()

    # Convert datetime to CDT if not already
    if local_timezone != "America/Chicago":
        current_time = current_time.astimezone(timezone.utc).astimezone(
            timezone(timedelta(hours=-5))
        )

    CDT_TIMESTAMP = {
        "today": current_time.strftime("%A, %B %d, %Y"),
        "time": current_time.strftime("%I:%M%p"),
    }

    print(f"Today is {CDT_TIMESTAMP['today']}. The time is {CDT_TIMESTAMP['time']}.")
    check_cubs_game(CDT_TIMESTAMP)
    print()
