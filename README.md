# CLI To-Do App

A simple command-line to-do app written in Python. Tasks are saved to a local JSON file, so they are still there the next time you run it.

## Features

- Add, list, complete and delete tasks
- Tasks persist between runs (`tasks.json`)
- Input validation: invalid input shows a message instead of crashing
- No external dependencies, only the Python standard library

## Requirements

- Python 3.8 or newer

## Usage

```bash
python main.py
```

Example session:

```
=== To-Do App ===
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Quit
Choose an option: 1
New task: Buy groceries
Added: Buy groceries
```

## Project structure

```
cli-todo-app/
├── main.py       # the app
├── tasks.json    # created automatically on first save
└── README.md
```

## Roadmap

- [ ] Task priorities
- [ ] Due dates
- [ ] Search and filter
- [ ] Unit tests

## License

MIT
