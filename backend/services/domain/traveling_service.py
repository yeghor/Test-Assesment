from sqlalchemy.ext.asyncio import AsyncSession
from services.repository import PostgresService, PlacesAPI

class TravelingService:
    def __init__(self, session: AsyncSession):
        self.postgres_service = PostgresService(session)
        self.places_api = PlacesAPI(session)

    def commit_changes(commit: bool):
        """Must be always called to keep all changes"""

    def create_project():
        pass

    def update_project():
        pass

    def delete_project():
        pass

    def add_project_place():
        pass

    def delete_project_place():
        pass

    def search_places(self):
        pass

    def get_places(self, page: int):
        pass
    
    def list_projects(self):
        pass

    def get_project(self):
        pass