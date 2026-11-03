# Mini Task Tracker

A simple, menu-driven command-line Task Tracker built with Python. It allows users to organize daily tasks, track their completion status, and save their progress using JSON file storage.

Tasks are automatically saved and loaded when the application starts, ensuring that progress is preserved between sessions.

## Features

- **Add Tasks:** Create new tasks with a title and a default `Pending` status.
- **View Tasks:** Display all tasks in a numbered list with their current status (`Pending` or `Done`).
- **Complete Tasks:** Mark existing tasks as completed.
- **Delete Tasks:** Remove tasks from the list.
- **Persistent Storage:** Automatically save and load tasks using `tasks.json`.
- **Input Validation:** Handle empty task titles, invalid menu choices, and incorrect task numbers.
- **Error Handling:** Handle missing JSON files and non-numeric task number inputs without crashing.

## Technologies Used

- **Python 3**
- **JSON:** For storing and retrieving task data.
- **Python Standard Library:** No external dependencies required.

## Getting Started

### 1. Prerequisites

Ensure Python 3.8 or newer is installed.

Check your Python version:

```bash
python --version
```

### 2. Run the Application

Open a terminal in the project directory and execute:

```bash
python mini_task_tracker.py
```

On some systems, use:

```bash
python3 mini_task_tracker.py
```

### 3. Use the Menu

The application displays the following options:

```text
--- TASK TRACKER ---
1. Add
2. View
3. Complete
4. Delete
5. Exit

Choice:
```

Enter a number from `1` to `5` to perform an action.

## Example Usage

**Adding a task:**

```text
Choice: 1
Enter task title: Complete Python assignment
Task added successfully!
```

**Viewing tasks:**

```text
--- YOUR TASKS ---
1. Complete Python assignment [Pending]
2. Read a book [Pending]
```

**Completing a task:**

```text
Choice: 3
Enter the task number to mark as completed: 1
Task completed successfully!
```

**Viewing updated tasks:**

```text
--- YOUR TASKS ---
1. Complete Python assignment [Done]
2. Read a book [Pending]
```

## Data Storage

The application uses a local JSON file named `tasks.json` to store tasks.

Each task is represented as a Python dictionary containing two fields:

```json
{
    "title": "Complete Python assignment",
    "done": false
}
```

- `title`: Stores the task description.
- `done`: Stores the completion status as a Boolean (`true` or `false`).

The application automatically creates or updates `tasks.json` whenever tasks are added, completed, or deleted.

Previously saved tasks are loaded when the program starts.

## Project Structure

```text
Mini-Task-Tracker/
├── mini_task_tracker.py  # Main Python application
├── tasks.json            # Task data (created automatically)
└── README.md             # Project documentation
```

## Error Handling

The application handles common user input errors, including:

- Empty task titles.
- Invalid menu selections.
- Task numbers outside the available range.
- Non-numeric task number inputs.
- Missing `tasks.json` files.

These checks help prevent unexpected program termination and improve usability.

## Learning Outcomes

This project demonstrates practical Python programming concepts, including:

- Functions and modular programming.
- Lists and dictionaries.
- Conditional statements.
- `while` and `for` loops.
- File handling.
- JSON serialization and deserialization.
- Exception handling using `try` and `except`.
- User input validation.

## Future Improvements

Potential enhancements include:

- Editing existing task titles.
- Adding task priorities and due dates.
- Searching and filtering tasks.
- Creating a graphical user interface (GUI).

## Project Information

**Project:** Mini Task Tracker  
**Language:** Python  
**Type:** Command-Line Application  
**Course:** AI Engineering — Week 1, Day 2

## License

Created for educational and learning purposes.