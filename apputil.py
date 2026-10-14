import requests
import pandas as pd
import os


class Genius:
    """Interact with the Genius API."""

    def __init__(self, access_token):
        """Initialize a Genius object with an API access token."""
        self.access_token = access_token

    def get_artist(self, search_term):
        """Return artist information for a search term."""
        genius_search_url = (
            f"https://api.genius.com/search?q={search_term}"
        )

        response = requests.get(
            genius_search_url,
            headers={"Authorization": "Bearer " + self.access_token}
        )

        json_data = response.json()

        artist_id = (
            json_data["response"]["hits"][0]["result"]["primary_artist"]["id"]
        )

        artist_url = f"https://api.genius.com/artists/{artist_id}"

        artist_response = requests.get(
            artist_url,
            headers={"Authorization": "Bearer " + self.access_token}
        )

        json_data_artist = artist_response.json()

        return json_data_artist

    def get_artists(self, search_terms):
        """Return artist information for multiple search terms as a DataFrame."""
        artists = []

        for search_term in search_terms:
            artist_data = self.get_artist(search_term)
            artist = artist_data["response"]["artist"]

            artist_row = {
                "search_term": search_term,
                "artist_name": artist["name"],
                "artist_id": artist["id"],
                "followers_count": artist.get("followers_count")
            }

            artists.append(artist_row)

        df = pd.DataFrame(artists)

        return df
        