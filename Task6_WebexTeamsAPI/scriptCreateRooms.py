import requests

api_url = "https://webexapis.com/v1/rooms"
access_token = "M2IzM2U1YjYtY2RlMi00NDA5LTgxMTEtZWRiYjg4NWFjY2QzZmVjYWE4ZjctMGY5_P0A1_f385d8b4-839f-42c4-9819-c9b577f54c40"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

data = {
    "title": "devasc_skills_VitalTyrsu",
}

response = requests.post(api_url, headers=headers, json=data)

if response.status_code == 200:
    print("Room created successfully")
    room_info = response.json()
    print("Room ID:", room_info["id"])
else:
    print(f"Failed to create room. Status code: {response.status_code}")
    print("Response:", response.text)
