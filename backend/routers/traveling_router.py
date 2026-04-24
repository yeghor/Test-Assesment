from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from publicDTO import *

traveling = APIRouter()


@traveling.post("/", summary="Create a travel project")
async def create_travel_project(travel_object: TravelProjectCreate) -> None:
    """Create a travel project with optional imported places."""
    

@traveling.get("/", summary="List travel projects")
async def list_travel_projects() -> List[ShortTravelProjects]:
    """List all travel projects."""


@traveling.get("/{project_id}", summary="Get a single travel project")
async def get_travel_project(project_id: str) -> TravelProject:
    """Get travel project details by project_id."""


@traveling.put("/{project_id}", summary="Update a travel project")
async def update_travel_project(
    project_id: str,
    travel_project: TravelProjectUpdate
) -> None:
    """Update travel project name, description, or start date."""


@traveling.delete("/{project_id}", summary="Delete a travel project")
async def delete_travel_project(project_id: str) -> None:
    """Delete a travel project if no places are marked as visited"""


@traveling.post("/{project_id}/places", summary="Add a place to a travel project")
async def add_place_to_project(
    project_id: str,
    place_name: str
) -> None:
    """Add a place to an existing project after validating the external place ID."""


@traveling.patch("/{project_id}/places/{place_id}", summary="Update a project place")
async def update_place_in_project(
    project_id: str,
    place_id: str,
    visited: bool
) -> None:
    """Update notes or visited state for a place in a project."""

@traveling.get("/{project_id}/places", summary="List all places for a travel project")
async def list_project_places(project_id: str) -> List[TravelPlaceShort]:
    """List all places associated with a travel project."""


@traveling.get(
    "/{project_id}/places/{place_id}",
    summary="Get a single place within a travel project",
)
async def get_project_place(project_id: str, place_id: str) -> TravelPlace:
    """Get details for a single place within a project"""
