# cc-sandbox

> A friendly full-screen greeting for your terminal — in dark mode.

---

## Demo

```
 _   _      _ _         _   _
| | | | ___| | | ___   | |_| |__   ___ _ __ ___
| |_| |/ _ \ | |/ _ \  | __| '_ \ / _ \ '__/ _ \
|  _  |  __/ | | (_) | | |_| | | |  __/ | |  __/
|_| |_|\___|_|_|\___/   \__|_| |_|\___|_|  \___|
```

Clears your terminal, paints it **black**, and displays a bright white bold greeting — centered on screen.

---

## Usage

```bash
python3 hello.py                  # greets "there" (default)
python3 hello.py --name Sam       # greets a specific name
python3 hello.py --help           # show usage info
```

---

## How it works

| Component | What it does |
|-----------|-------------|
| `--name NAME` | Optional CLI argument. Defaults to `"there"` if omitted. |
| `greet(name)` | Returns a greeting string for the given name. |
| `main()` | Parses args, clears the screen, fills it dark, and centers the greeting. |
| ANSI codes | Drive the full-screen black background + bright white bold text. |

You can also import `greet` from another module:

```python
from hello import greet
print(greet("Sam"))
# Hello, Sam! Hope you're having a great day.
```

---

## Requirements

- Python 3.6+
- A terminal that supports ANSI escape codes (macOS Terminal, iTerm2, VS Code terminal, etc.)
