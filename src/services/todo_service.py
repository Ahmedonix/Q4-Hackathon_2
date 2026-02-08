"""
TodoList service providing business logic for todo operations.

The service maintains a collection of TodoItem objects and provides methods for:
- Adding, removing, updating, and querying items
- Maintaining auto-incrementing ID counter
- All operations are in-memory only
"""

from typing import List, Dict, Optional
from src.models.todo_item import TodoItem


class TodoService:
    """
    Service class for managing todo items in memory.
    Provides methods for adding, retrieving, updating, and deleting todo items.
    """

    def __init__(self):
        """
        Initialize the TodoService with an empty dictionary for items
        and an auto-incrementing ID counter.
        """
        self.items: Dict[int, TodoItem] = {}
        self._next_id = 1

    def add_item(self, description: str) -> TodoItem:
        """
        Add a new todo item to the list.

        Args:
            description (str): Description of the new todo item

        Returns:
            TodoItem: The newly created TodoItem

        Raises:
            ValueError: If description is empty
        """
        if not description or description.strip() == "":
            raise ValueError("Description cannot be empty")

        new_id = self._next_id
        self._next_id += 1
        item = TodoItem(new_id, description)
        self.items[new_id] = item
        return item

    def get_item(self, id: int) -> Optional[TodoItem]:
        """
        Retrieve a specific todo item by ID.

        Args:
            id (int): ID of the todo item to retrieve

        Returns:
            Optional[TodoItem]: The todo item if found, None otherwise
        """
        return self.items.get(id)

    def update_item(self, id: int, new_description: str) -> bool:
        """
        Update a todo item's description.

        Args:
            id (int): ID of the todo item to update
            new_description (str): New description for the item

        Returns:
            bool: True if the item was updated, False if item not found

        Raises:
            ValueError: If new_description is empty
        """
        if not new_description or new_description.strip() == "":
            raise ValueError("Description cannot be empty")

        if id in self.items:
            self.items[id].description = new_description.strip()
            return True
        return False

    def complete_item(self, id: int) -> bool:
        """
        Mark a todo item as completed.

        Args:
            id (int): ID of the todo item to mark as completed

        Returns:
            bool: True if the item was marked as completed, False if item not found
        """
        if id in self.items:
            self.items[id].complete()
            return True
        return False

    def delete_item(self, id: int) -> bool:
        """
        Remove a todo item from the list.

        Args:
            id (int): ID of the todo item to remove

        Returns:
            bool: True if the item was removed, False if item not found
        """
        if id in self.items:
            del self.items[id]
            return True
        return False

    def get_all_items(self) -> List[TodoItem]:
        """
        Return all todo items.

        Returns:
            List[TodoItem]: List of all todo items, sorted by ID
        """
        return sorted(self.items.values(), key=lambda x: x.id)

    def get_pending_items(self) -> List[TodoItem]:
        """
        Return only pending todo items.

        Returns:
            List[TodoItem]: List of pending todo items, sorted by ID
        """
        return sorted(
            [item for item in self.items.values() if item.status == "pending"],
            key=lambda x: x.id
        )

    def get_completed_items(self) -> List[TodoItem]:
        """
        Return only completed todo items.

        Returns:
            List[TodoItem]: List of completed todo items, sorted by ID
        """
        return sorted(
            [item for item in self.items.values() if item.status == "completed"],
            key=lambda x: x.id
        )

    def get_next_id(self) -> int:
        """
        Get the next available ID without incrementing the counter.

        Returns:
            int: The next available ID
        """
        return self._next_id