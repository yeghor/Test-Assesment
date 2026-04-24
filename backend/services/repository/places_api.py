from typing import List


class PlacesAPI:
    def __init__(self):
        self._base_url = "https://api.artic.edu/api/v1/places"

    def check_place(self, place_id) -> bool:
        """Checks whether place exists in API"""

    def get_places(self, page: int) -> List[str]:
        pass

    def search_places(self, page: int) -> List[str]:
        pass

    