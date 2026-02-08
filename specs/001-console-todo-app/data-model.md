# Data Model: Console Todo Application

**Feature**: 001-console-todo-app
**Date**: 2026-01-02
**Input**: Feature specification and implementation plan

## Core Entities

### TodoItem
Represents a single task in the todo list with properties:

- **id**: `int` - Unique identifier for the task (auto-incremented)
- **description**: `str` - Text description of the task
- **status**: `str` - Current status ("pending" or "completed")
- **created_at**: `datetime` - Timestamp when the task was created

### TodoList
Collection of TodoItem objects with operations:

- **items**: `List[TodoItem]` - List of all todo items
- **add_item(description: str)**: Adds a new todo item to the list
- **get_item(id: int)**: Retrieves a specific todo item by ID
- **update_item(id: int, new_description: str)**: Updates a todo item's description
- **complete_item(id: int)**: Marks a todo item as completed
- **delete_item(id: int)**: Removes a todo item from the list
- **get_all_items()**: Returns all todo items
- **get_pending_items()**: Returns only pending todo items
- **get_completed_items()**: Returns only completed todo items

## Data Flow

1. **Input**: User enters commands via CLI
2. **Processing**: CLI parses command and calls appropriate TodoService method
3. **Data**: TodoService operates on TodoList in memory
4. **Output**: Results formatted and displayed to user via CLI

## In-Memory Storage Structure

```python
# Internal representation in memory
todo_list = {
    1: TodoItem(id=1, description="Buy groceries", status="pending", created_at=datetime.now()),
    2: TodoItem(id=2, description="Complete project", status="completed", created_at=datetime.now()),
    # ... more items
}
```

The data structure uses a dictionary with integer keys for O(1) lookup by ID, supporting all required operations efficiently.