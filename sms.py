from twilio.rest import Client
import keys

def send_twilio_message(message_body, to_phone_numbers, location=None):
    client = Client(keys.account_sid, keys.auth_token)

    for to_phone_number in to_phone_numbers:
        if location:
            # Format the location as a clickable map link
            map_link = f"https://www.google.com/maps?q={location}"
            message_body_with_location = f"{message_body}\nLocation: {map_link}"
        else:
            message_body_with_location = message_body

        message = client.messages.create(
            body=message_body_with_location,
            from_=keys.twilio_number,
            to=to_phone_number,
        )

        # You can print or log the message details if needed
        print(f"Message sent to {to_phone_number}. SID: {message.sid}")

    # Optionally, return a list of message SIDs or any other information
    return [message.sid for _ in to_phone_numbers]


