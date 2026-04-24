from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey

from datetime import datetime


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "user"

    user_id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()
    password_hash: Mapped[str] = mapped_column()

    projects: Mapped[list[TravelProject]] = relationship(back_populates="user", lazy="selectin")


class TravelProject(Base):
    __tablename__ = "travel_project"

    project_id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.user_id"))

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)
    start_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    note: Mapped[str] = mapped_column(default="")

    user: Mapped[Users] = relationship(back_populates="projects")
    places: Mapped[list[TravelPlace]] = relationship(back_populates="project", lazy="selectin")


class TravelPlace(Base):
    __tablename__ = "travel_place"

    place_id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("user.user_id"))
    project_id: Mapped[str] = mapped_column(ForeignKey("travel_project.project_id"))
    visited: Mapped[bool] = mapped_column(default=False)

    project: Mapped[TravelProject] = relationship(back_populates="places")
    notes: Mapped[list[TravelPlaceNote]] = relationship(back_populates="place", lazy="selectin")


class TravelPlaceNote(Base):
    __tablename__ = "travel_place_note"

    note_id: Mapped[str] = mapped_column(primary_key=True)
    place_id: Mapped[str] = mapped_column(ForeignKey("travel_place.place_id"))

    place: Mapped[TravelPlace] = relationship(back_populates="notes")
