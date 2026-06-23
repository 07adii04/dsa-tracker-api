
```markdown
# DSA Tracker API

A REST API to log and track LeetCode problems as I solve them.  
Built as my first FastAPI project to learn backend fundamentals before building Indic Lens V2.

## What it does

- Log problems with title, difficulty, and solved status
- Fetch all problems or search by ID
- Delete problems by ID
- Get live stats — total solved, breakdown by difficulty

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/problems` | Get all problems |
| POST | `/problems` | Add a new problem |
| GET | `/problems/{id}` | Get one problem by ID |
| DELETE | `/problems/{id}` | Delete a problem by ID |
| GET | `/stats` | Get solving stats by difficulty |

## Tech Stack

- Python 3.12
- FastAPI
- Pydantic

## Run locally

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Then open `http://127.0.0.1:8000/docs` for the interactive API explorer.

## What's next

This project was a learning step. Next up is **Indic Lens V2** — an OCR and translation app for Indian scripts built with FastAPI and Google Vision API.
```

Create a `README.md` file in your project folder, paste this in, then:

```bash
git add README.md
git commit -m "docs: add README"
git push
```
