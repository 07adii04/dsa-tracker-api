from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "check /docs for more information"}

@app.get("/double/{number}")
def double_number(number: int):
    return {"input": number, "doubles": number * 2}

@app.get("/greet")
def greet(name: str, greeting: str = "Hello"):
    return {"message": f"{greeting}, {name}!"}

class Problem(BaseModel):
    title: str
    difficulty: str
    solved: bool

class ProblemInDB(Problem):
    id: int

# Database mock
problems_db: list[ProblemInDB] = []
next_id = 1

@app.get("/problems")
def get_problems():
    return problems_db

# We only keep THIS post route, which correctly handles the 'id'
@app.post("/problems")
def add_problem(problem: Problem):
    global next_id
    new_problem = ProblemInDB(
        title = problem.title,
        difficulty = problem.difficulty,
        solved = problem.solved,
        id = next_id
    )
    problems_db.append(new_problem)
    next_id += 1
    return new_problem  # ✅ just return, no exception

# I want to get one specific problem by its id
# if it doesnt exist return an error
@app.get("/problems/{problem_id}")
def get_problem(problem_id: int):
    for p in problems_db:
        if p.id == problem_id:
            return p
    raise HTTPException(status_code=404, detail="Problem not found")


# I want to delete a problem by its id
# if it doesnt exist return an error
@app.delete("/problems/{problem_id}")
def delete_problem(problem_id: int):
    for index, p in enumerate(problems_db):
        if p.id == problem_id:
            problems_db.pop(index)
            return {"deleted": problem_id}
    raise HTTPException(status_code=404, detail="Problem not found")

#to solve return type error in /stats i will create a new class for response
class DifficultyStats(BaseModel):
    easy: int
    medium: int
    hard: int
    #while making this class i think would be better if i cover it inside another class as well
class stat_response(BaseModel):
    total:int
    solved:int
    by_difficulty : DifficultyStats

@app.get("/stats",response_model = stat_response)
def get_stats():
    total = len(problems_db)
    solved = sum(1 for p in problems_db if p.solved)
    easy = sum(1 for p in problems_db if p.difficulty.lower()=="easy")
    medium = sum(1 for p in problems_db if p.difficulty.lower()=="medium")
    hard = sum(1 for p in problems_db if p.difficulty.lower()=="hard")
    #dictionary wasnt working pydantic kept showing error so i think best way to solve this is to wrap them up in new class 
    return stat_response(
        total = total,
        solved = solved,
        by_difficulty=DifficultyStats(
            easy=easy,
            medium=medium,
            hard=hard
        )


    )



