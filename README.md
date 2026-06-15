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
python3 hello.py
```

---

## How it works

| Component | What it does |
|-----------|-------------|
| `greet(name)` | Returns a greeting string. Defaults to `"there"`. |
| `main()` | Clears the screen, fills it dark, and centers the greeting. |
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
