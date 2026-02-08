# Console Todo Application

A clean, in-memory command-line Todo application that supports the 5 core features (Add, View, Update, Delete, Mark Complete) with a modular Python structure. The application separates business logic from input/output, maintains all data in memory, and provides clear error handling and user prompts.

## Features

- Add new todo items
- View all todo items
- Mark items as completed
- Update existing item descriptions
- Delete items from the list
- Error handling for edge cases
- Clean command-line interface

## Prerequisites

- Python 3.13+ installed

## Setup

1. Clone or create the project directory
2. Navigate to the project root
3. Install dependencies: `pip install -e .` (or use standard Python environment)

## Running the Application

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

### Help and Exit
```
help          # Show available commands
quit          # Exit application
exit          # Exit application
```

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
- The application maintains state during the session"# Q4-Hackathon_2" 
