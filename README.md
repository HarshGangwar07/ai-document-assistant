# AI Document Assistant

A minimal FastAPI service that currently exposes a single health-style root endpoint returning the project name.

## What It Does

- Starts a FastAPI application
- Serves `GET /`
- Returns a JSON response:

```json
{"message": "AI Document Assistant"}
```

## Project Structure

```text
app/
  main.py
README.md
```

## Requirements

- Python 3.10+ recommended
- `fastapi`
- `uvicorn`

## Running Locally

Install the dependencies:

```bash
pip install fastapi uvicorn
```

Start the development server:

```bash
uvicorn app.main:app --reload
```

Then open:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

## Example Response

```json
{
  "message": "AI Document Assistant"
}
```

## Notes

This repository currently contains only the API entrypoint. If you add document upload, processing, or retrieval features later, this README is the right place to document them.
