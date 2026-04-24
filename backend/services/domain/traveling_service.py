from sqlalchemy.ext.asyncio import AsyncSession
from services.repository import PostgresService, PlacesAPI

from publicDTO import *
from database import TravelProject, TravelPlace

class TravelingService:
    def __init__(self, session: AsyncSession):
        self.postgres_service = PostgresService(session)
        self.places_api = PlacesAPI(session)

    def commit_changes(commit: bool):
        """Must be always called to keep all changes"""

    def create_project():
        

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

    def list_project_places(self, page: int):
        pass

    def update_project_place(self):
        pass
    
    def list_projects(self):
        pass

    def get_project(self):
        pass

    def get_project_place(self):
        pass