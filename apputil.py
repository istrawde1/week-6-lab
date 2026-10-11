class Genius:
    def __init__(self,access_token):
                self.access_token = access_token


class Genius:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_artist(self, search_term):
        genius_search_url = f"http://api.genius.com/search?q={search_term}"

        response = requests.get(
            genius_search_url,
            headers={"Authorization": "Bearer " + self.access_token}
        )

        json_data = response.json()
        json_data["response"]["hits"]["result"]["primary_artist"]["id"]