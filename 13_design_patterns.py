# Scenario: A notification service uses a simple factory to create notification objects.
class EmailNotification:
    def send(self, message):
        print("Email:", message)

class SMSNotification:
    def send(self, message):
        print("SMS:", message)

class NotificationFactory:
    @staticmethod
    def create(channel):
        if channel == "email":
            return EmailNotification()
        if channel == "sms":
            return SMSNotification()
        raise ValueError("Unsupported notification channel")

notification = NotificationFactory.create("email")
notification.send("Your order has been shipped.")
