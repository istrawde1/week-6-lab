import requests


class Genius:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_artist(self, search_term):
        genius_search_url = f"https://api.genius.com/search?q={search_term}"

        response = requests.get(
            genius_search_url,
            headers={"Authorization": "Bearer " + self.access_token}
        )

        json_data = response.json()

        artist_id = json_data["response"]["hits"][0]["result"]["primary_artist"]["id"]

        artist_url = f"https://api.genius.com/artists/{artist_id}"

        artist_response = requests.get(
            artist_url,
            headers={"Authorization": "Bearer " + self.access_token}
        )

        json_data_artist = artist_response.json()

        return json_data_artist
    