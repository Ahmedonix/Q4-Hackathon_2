"""
Main application loop for the console todo application.
Provides the command-line interface and handles user input.
"""

import sys
from src.services.todo_service import TodoService
from src.lib.utils import parse_command, format_todo_item, format_error_message


def main():
    """
    Main application loop that handles user input and command processing.
    """
    print("Welcome to the Console Todo Application!")
    print("Type 'help' for available commands or 'quit' to exit.")

    # Initialize the todo service
    todo_service = TodoService()

    while True:
        try:
            # Get user input
            user_input = input("\n> ").strip()

            # Handle empty input
            if not user_input:
                print("Please enter a command. Type 'help' for available commands.")
                continue

            # Parse the command
            command, args = parse_command(user_input)

            # Process the command
            if command in ['quit', 'exit']:
                print("Goodbye!")
                break
            elif command == 'help':
                show_help()
            elif command == 'add':
                handle_add_command(todo_service, args)
            elif command in ['list', 'view']:
                handle_list_command(todo_service, args)
            elif command == 'complete':
                handle_complete_command(todo_service, args)
            elif command == 'update':
                handle_update_command(todo_service, args)
            elif command == 'delete':
                handle_delete_command(todo_service, args)
            else:
                print(format_error_message(f"Unknown command: {command}. Type 'help' for available commands."))

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


def show_help():
    """
    Display help information with available commands.
    """
    help_text = """
Available commands:
  add <description>          - Add a new todo item
  list / view               - Display all todo items
  complete <id>             - Mark a todo item as completed
  update <id> <new description> - Update a todo item description
  delete <id>               - Delete a todo item
  help                      - Show this help message
  quit / exit               - Exit the application
    """.strip()
    print(help_text)


def handle_add_command(todo_service, args):
    """
    Handle the 'add' command to add a new todo item.

    Args:
        todo_service (TodoService): The todo service instance
        args (list): List of command arguments
    """
    if len(args) < 1:
        print(format_error_message("Please provide a description for the new todo item."))
        print("Usage: add <description>")
        return

    description = " ".join(args)

    try:
        new_item = todo_service.add_item(description)
        print(f'Added: "{new_item.description}" (ID: {new_item.id})')
    except ValueError as e:
        print(format_error_message(str(e)))


def handle_list_command(todo_service, args):
    """
    Handle the 'list' or 'view' command to display todo items.

    Args:
        todo_service (TodoService): The todo service instance
        args (list): List of command arguments
    """
    all_items = todo_service.get_all_items()

    if not all_items:
        print("Your todo list is empty.")
        return

    for item in all_items:
        formatted_item = format_todo_item(item)
        status_indicator = "x" if item.status == "completed" else " "
        print(f"{item.id}. [{status_indicator}] {item.description}")


def handle_complete_command(todo_service, args):
    """
    Handle the 'complete' command to mark an item as completed.

    Args:
        todo_service (TodoService): The todo service instance
        args (list): List of command arguments
    """
    if len(args) != 1:
        print(format_error_message("Please provide the ID of the item to complete."))
        print("Usage: complete <id>")
        return

    try:
        item_id = int(args[0])

        # Check if item exists before trying to complete it
        item = todo_service.get_item(item_id)
        if item is None:
            print(format_error_message(f"No todo item found with ID {item_id}."))
            return

        success = todo_service.complete_item(item_id)
        if success:
            print(f'Marked as complete: "{item.description}"')
        else:
            print(format_error_message(f"Failed to complete item with ID {item_id}."))

    except ValueError:
        print(format_error_message("Please provide a valid ID (integer)."))
        print("Usage: complete <id>")


def handle_update_command(todo_service, args):
    """
    Handle the 'update' command to update a todo item's description.

    Args:
        todo_service (TodoService): The todo service instance
        args (list): List of command arguments
    """
    if len(args) < 2:
        print(format_error_message("Please provide an ID and new description."))
        print("Usage: update <id> <new description>")
        return

    try:
        item_id = int(args[0])
        new_description = " ".join(args[1:])

        # Check if item exists before trying to update it
        item = todo_service.get_item(item_id)
        if item is None:
            print(format_error_message(f"No todo item found with ID {item_id}."))
            return

        success = todo_service.update_item(item_id, new_description)
        if success:
            print(f'Updated: "{new_description}"')
        else:
            print(format_error_message(f"Failed to update item with ID {item_id}."))

    except ValueError as e:
        if "invalid literal" in str(e):
            print(format_error_message("Please provide a valid ID (integer)."))
            print("Usage: update <id> <new description>")
        else:
            print(format_error_message(str(e)))


def handle_delete_command(todo_service, args):
    """
    Handle the 'delete' command to remove a todo item.

    Args:
        todo_service (TodoService): The todo service instance
        args (list): List of command arguments
    """
    if len(args) != 1:
        print(format_error_message("Please provide the ID of the item to delete."))
        print("Usage: delete <id>")
        return

    try:
        item_id = int(args[0])

        # Check if item exists before trying to delete it
        item = todo_service.get_item(item_id)
        if item is None:
            print(format_error_message(f"No todo item found with ID {item_id}."))
            return

        success = todo_service.delete_item(item_id)
        if success:
            print(f'Deleted: "{item.description}"')
        else:
            print(format_error_message(f"Failed to delete item with ID {item_id}."))

    except ValueError:
        print(format_error_message("Please provide a valid ID (integer)."))
        print("Usage: delete <id>")


if __name__ == "__main__":
    main()