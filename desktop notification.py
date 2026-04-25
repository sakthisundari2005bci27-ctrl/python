from plyer import notification
import time

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None, # Path to .ico file
        timeout=10,    # Seconds the notification stays
    )

if __name__ == "__main__":
    send_notification("Break Time!", "You've been working hard. Stretch for 5 minutes!")
