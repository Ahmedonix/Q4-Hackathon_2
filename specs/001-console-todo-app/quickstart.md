# Quickstart Guide: Console Todo Application

**Feature**: 001-console-todo-app
**Date**: 2026-01-02

## Getting Started

### Prerequisites
- Python 3.13+ installed
- UV package manager (optional, for environment management)

### Setup
1. Clone or create the project directory
2. Navigate to the project root
3. Install dependencies if using UV: `uv sync` (or use standard Python environment)

### Running the Application
```bash
python src/cli/main.py
```

## Available Commands

### Add a new todo item
```
add <description>
```
Example: `add Buy groceries`

### View all todo items
```
list
```
or
```
view
```

### Mark a todo item as complete
```
complete <id>
```
Example: `complete 1`

### Update a todo item description
```
update <id> <new description>
```
Example: `update 1 Buy organic groceries`

### Delete a todo item
```
delete <id>
```
Example: `delete 1`

## Sample Session

```
> add Buy groceries
Added: "Buy groceries" (ID: 1)

> add Complete project
Added: "Complete project" (ID: 2)

> list
1. [ ] Buy groceries
2. [ ] Complete project

> complete 1
Marked as complete: "Buy groceries"

> list
1. [x] Buy groceries
2. [ ] Complete project

> update 2 Complete project by Friday
Updated: "Complete project by Friday"

> list
1. [x] Buy groceries
2. [ ] Complete project by Friday

> delete 2
Deleted: "Complete project by Friday"

> list
1. [x] Buy groceries
```

## Error Handling

- Invalid commands will show an error message and return to the prompt
- Non-existent IDs will show an appropriate error message
- Empty input will prompt for valid input
- The application maintains state during the session