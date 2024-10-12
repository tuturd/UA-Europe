from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv
import os

load_dotenv()

UA_TIMESTAMP: int = int(os.getenv('UA_TIMESTAMP', 0))
WEBHOOK_URL: int = os.getenv('WEBHOOK_URL', '')


# FONCTIONS
def send_to_discord(message: str) -> None:
    """Send a message to the Discord channel"""

    requests.post(WEBHOOK_URL, data={'content': message})


def log(message: str) -> None:
    """Log a message to main.log"""

    with open('main.log', 'a') as log_file:
        log_file.write(f'{datetime.now()} - {message}\n')


def main() -> None:
    """Main function"""

    now: datetime = datetime.now()
    time_to_ua: timedelta = datetime.fromtimestamp(UA_TIMESTAMP) - now
    hours_to_ua: int = int(time_to_ua.total_seconds() // 3600)

    if hours_to_ua < 1:
        send_to_discord('# Ils sont là ! :tada:')
        log('# Ils sont là ! :tada:')
        return

    one_week: timedelta = timedelta(weeks=1)
    days_to_ua: int = int(time_to_ua.total_seconds() // 86400)

    if time_to_ua > one_week:
        if now.hour == 16 and now.minute == 55:
            send_to_discord(f"## Plus que {days_to_ua} jours avant l'UA ! :clock:")
            log(f"## Plus que {days_to_ua} jours avant l'UA ! :clock:")
        else:
            log('nothing to do')
        return

    send_to_discord(f'Ils débarquent dans **{hours_to_ua} heures** ! :fearful:')
    log(f'Ils débarquent dans **{hours_to_ua} heures** ! :fearful:')


# MAIN
if __name__ == '__main__':
    main()
