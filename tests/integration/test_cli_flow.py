"""
Integration tests for complete user flows in the console todo application.
"""

import io
import sys
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import patch
from src.cli.main import main
from src.services.todo_service import TodoService


def test_add_and_list_flow():
    """
    Test the basic flow of adding items and listing them.
    """
    service = TodoService()

    # Add a few items
    item1 = service.add_item("Buy groceries")
    item2 = service.add_item("Complete project")

    # Verify they were added with correct IDs
    assert item1.id == 1
    assert item2.id == 2
    assert item1.description == "Buy groceries"
    assert item2.description == "Complete project"
    assert item1.status == "pending"
    assert item2.status == "pending"

    # Verify we can retrieve all items
    all_items = service.get_all_items()
    assert len(all_items) == 2
    assert all_items[0].id == 1
    assert all_items[1].id == 2

    print("PASSED: Add and list flow test passed")


def test_complete_item_flow():
    """
    Test the flow of adding an item and marking it as complete.
    """
    service = TodoService()

    # Add an item
    item = service.add_item("Test completion")
    assert item.status == "pending"

    # Complete the item
    success = service.complete_item(item.id)
    assert success is True

    # Verify the item is now completed
    retrieved_item = service.get_item(item.id)
    assert retrieved_item.status == "completed"

    print("PASSED: Complete item flow test passed")


def test_update_item_flow():
    """
    Test the flow of adding an item and updating its description.
    """
    service = TodoService()

    # Add an item
    item = service.add_item("Original description")
    assert item.description == "Original description"

    # Update the item
    success = service.update_item(item.id, "Updated description")
    assert success is True

    # Verify the item was updated
    retrieved_item = service.get_item(item.id)
    assert retrieved_item.description == "Updated description"

    print("✓ Update item flow test passed")


def test_delete_item_flow():
    """
    Test the flow of adding an item and deleting it.
    """
    service = TodoService()

    # Add an item
    item = service.add_item("Item to delete")
    assert len(service.get_all_items()) == 1

    # Delete the item
    success = service.delete_item(item.id)
    assert success is True

    # Verify the item is gone
    assert len(service.get_all_items()) == 0
    assert service.get_item(item.id) is None

    print("✓ Delete item flow test passed")


def test_edge_cases():
    """
    Test edge cases like invalid IDs, empty descriptions, etc.
    """
    service = TodoService()

    # Try to get a non-existent item
    assert service.get_item(999) is None

    # Try to update a non-existent item
    assert service.update_item(999, "New description") is False

    # Try to complete a non-existent item
    assert service.complete_item(999) is False

    # Try to delete a non-existent item
    assert service.delete_item(999) is False

    # Try to add an empty item (should raise ValueError)
    try:
        service.add_item("")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    # Try to add an item with only whitespace
    try:
        service.add_item("   ")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    print("✓ Edge cases test passed")


if __name__ == "__main__":
    print("Running integration tests for console todo application...")

    test_add_and_list_flow()
    test_complete_item_flow()
    test_update_item_flow()
    test_delete_item_flow()
    test_edge_cases()

    print("\n✓ All integration tests passed!")