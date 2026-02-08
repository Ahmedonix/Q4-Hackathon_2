"""
TodoItem model representing a single task in the todo list.

Attributes:
    id (int): Unique identifier for the task (auto-incremented)
    description (str): Text description of the task
    status (str): Current status ("pending" or "completed")
    created_at (datetime): Timestamp when the task was created
"""

from datetime import datetime
from typing import Union


class TodoItem:
    """
    Represents a single task in the todo list with properties:
    - id: Unique identifier for the task (auto-incremented)
    - description: Text description of the task
    - status: Current status ("pending" or "completed")
    - created_at: Timestamp when the task was created
    """

    def __init__(self, id: int, description: str, status: str = "pending"):
        """
        Initialize a TodoItem instance.

        Args:
            id (int): Unique identifier for the task
            description (str): Text description of the task
            status (str): Current status, defaults to "pending"

        Raises:
            ValueError: If description is empty or status is invalid
        """
        if not description or description.strip() == "":
            raise ValueError("Description cannot be empty")

        if status not in ["pending", "completed"]:
            raise ValueError("Status must be either 'pending' or 'completed'")

        self.id = id
        self.description = description.strip()
        self.status = status
        self.created_at = datetime.now()

    def complete(self):
        """Mark the todo item as completed."""
        self.status = "completed"

    def __str__(self) -> str:
        """
        Return a string representation of the todo item.

        Returns:
            str: Formatted string showing the todo item with status indicator
        """
        status_indicator = "x" if self.status == "completed" else " "
        return f"[{status_indicator}] {self.description}"

    def to_dict(self) -> dict:
        """
        Convert the TodoItem to a dictionary representation.

        Returns:
            dict: Dictionary containing all todo item properties
        """
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a TodoItem instance from a dictionary.

        Args:
            data (dict): Dictionary containing todo item properties

        Returns:
            TodoItem: New TodoItem instance
        """
        from datetime import datetime

        item = cls(
            id=data["id"],
            description=data["description"],
            status=data["status"]
        )
        item.created_at = datetime.fromisoformat(data["created_at"])
        return item