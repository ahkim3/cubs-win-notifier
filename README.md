# Cubs Win Notifier

Sends a text message whenever the Cubs win a home game. Usually indicative of a free Chick-fil-A sandwich in the Chicagoland area.

This project is completely automated with GitHub Actions, and can be manually triggered for a live update.

<br/>

# Latest Game Status

<!-- start-timestamp -->
`Last updated on Tuesday, July 23, 2024 at 08:05PM CDT`
<!-- end-timestamp -->

<!-- start-message -->
```
The Cubs will be playing the Milwaukee Brewers at home at 01:20PM.
```
<!-- end-message -->

---

<br/><br/>

# Self-Hosting Instructions

## Prerequisites

1. Set up a Google Cloud Console project with the Gmail API enabled
2. Set up the OAuth consent screen
3. Create credentials for an OAuth 2.0 client ID
4. Download the OAuth client secret and token JSON files
5. Find your phone number's [text email address](https://when2work.com/help/emp/find-text-address/)

## Local Setup

1. Clone the repository
2. Place the client secret and token JSON files in the root directory of the project
3. Rename the client secret file to `client_secret.json`
4. Rename the token file to `token.json`
5. Create a file named `sender.txt` in the root directory with the email address of the sender
6. Create a file named `receiver.txt` in the root directory with the receiving phone number's [text email address](https://when2work.com/help/emp/find-text-address/)
7. Run `pip install -r requirements.txt` to install the required Python packages
8. Run `python run.py`
9. (Optional) Set up a cron job to run the script at specific intervals

## GitHub Actions Setup

1. Fork this repository
2. Go to the repository's settings
3. Go to the "Secrets" tab
4. Add the following secrets:
   - `GMAIL_CREDENTIALS`: The contents of the client secret JSON file
   - `GMAIL_TOKEN`: The contents of the token JSON file
   - `SENDER`: The email address of the sender
   - `RECEIVER`: The receiving phone number's [text email address](https://when2work.com/help/emp/find-text-address/)
5. Customize the cron schedule in the `.github/workflows/cubs_win_notifier.yml` file
