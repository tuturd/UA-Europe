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


def main() -> None:
    """Main function"""

    now: datetime = datetime.now()
    time_to_ua: timedelta = datetime.fromtimestamp(UA_TIMESTAMP) - now
    hours_to_ua: int = int(time_to_ua.total_seconds() // 3600)

    if hours_to_ua < 1:
        send_to_discord('# Ils sont là ! :tada:')
        return

    one_week: timedelta = timedelta(weeks=1)
    days_to_ua: int = int(time_to_ua.total_seconds() // 86400)

    if time_to_ua > one_week:
        if now.hour == 18:
            send_to_discord(f"## Plus que {days_to_ua} jours avant l'UA ! :clock:")
        return

    send_to_discord(f'Ils débarquent dans **{hours_to_ua} heures** ! :fearful:')


# MAIN
if __name__ == '__main__':
    main()
