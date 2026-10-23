# 🛡️ Python Port Scanner (Async)

A modern, asynchronous port scanner written in Python 3.11+. 

## 🎯 Purpose
This project was created to demonstrate modern Python practices (type hints, `asyncio`, and logging) by refactoring a legacy sequential pentesting script.

## ✨ Features
- **Asynchronous:** Uses `asyncio` to scan multiple ports simultaneously (non-blocking).
- **Safe:** Implements a `Semaphore` to limit concurrent connections and avoid overwhelming the target.
- **Professional Logging:** Uses Python's `logging` module instead of `print()`.
- **Type Hints:** Fully typed for better maintainability and IDE support.

## 🚀 Usage
```bash
python scanner.py -t 127.0.0.1 -p 1-1000
