import requests

def add_users_to_room(access_token, room_id, user_emails):
    api_url = "https://webexapis.com/v1/memberships"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    for email in user_emails:
        data = {
            "roomId": room_id,
            "personEmail": email,
        }

        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            print(f"User {email} added to the room successfully")
        else:
            print(f"Failed to add user {email} to the room. Status code: {response.status_code}")
            print("Response:", response.text)

# Replace 'YOUR_ACCESS_TOKEN' with your actual access token
access_token = "M2IzM2U1YjYtY2RlMi00NDA5LTgxMTEtZWRiYjg4NWFjY2QzZmVjYWE4ZjctMGY5_P0A1_f385d8b4-839f-42c4-9819-c9b577f54c40"

# Replace 'ROOM_ID' with your actual room ID
room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMzdhNTExODAtYjU1MC0xMWVlLWJhNjgtYWJiNzQ4NDcyODRm"

# Replace the list with the emails of the users you want to add
user_emails = ["yvan.rooseleer@biasc.be", "vital.tyrsu@student.odisee.be"]

# Add the users to the room
add_users_to_room(access_token, room_id, user_emails)
