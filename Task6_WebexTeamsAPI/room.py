import requests

def get_all_room_ids(access_token):
    api_url = "https://webexapis.com/v1/rooms"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        rooms = response.json()["items"]
        room_ids = [room["id"] for room in rooms]
        return room_ids
    else:
        print(f"Failed to retrieve room IDs. Status code: {response.status_code}")
        print("Response:", response.text)
        return None

# Replace 'YOUR_ACCESS_TOKEN' with your actual access token
access_token = "M2IzM2U1YjYtY2RlMi00NDA5LTgxMTEtZWRiYjg4NWFjY2QzZmVjYWE4ZjctMGY5_P0A1_f385d8b4-839f-42c4-9819-c9b577f54c40"

# Get all room IDs
all_room_ids = get_all_room_ids(access_token)

if all_room_ids:
    print("All Room IDs:")
    for room_id in all_room_ids:
        print(room_id)
