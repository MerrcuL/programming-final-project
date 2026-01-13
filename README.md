# FastAPI Task Management System

A RESTful API backend for managing tasks, using a plain text file (tasks.txt) for persistent storage.

## Project Structure

fastapi-tasks/  
├── main.py # Application logic and API endpoints  
├── tasks.txt # Data storage (JSON Lines format)  
├── utily.py # Helper/Controler Functions  
└── README.md # Project documentation  

## Setup & Installation

- Install Dependencies:  
    You need FastAPI and Uvicorn.  
    `pip install fastapi uvicorn`  

- Ensure Storage File Exists:  
    Make sure `tasks.txt` exists in the same folder.  

## Running the Application

Run the server using Uvicorn:

python -m uvicorn main:app --reload

- The API will be available at: <http://127.0.0.1:8000>
- **Interactive Documentation**: <http://127.0.0.1:8000/docs>

## API Endpoints

| **Method** | **Endpoint** | **Desciption**                                  |
|------------|--------------|-------------------------------------------------|
| GET        | /            | Check if API is running                         |
| GET        | /tasks       | Get all tasks.  Optional ?completed=true param. |
| GET        | /tasks{id}   | Get a task by specified ID.                     |
| POST       | /tasks       | Create a new task.                              |
| PUT        | /tasks{id}   | Completely update a task by ID.                 |
| DELETE     | /tasks{ID}   | Delete a task by ID.                            |
| DELETE     | /tasks       | Delete all tasks.                               |
| GET        | /tasks/stats | Get statistics (total, completed, percentage).  |

## Data Format

Tasks are stored in tasks.txt in **JSON Lines** format:

{"id": 1, "title": "Build FastAPI Project", "description": "Read docs, watch tutorial on YouTube", "completed": true}  
{"id": 2, "title": "Build home server", "description": "Instal OMV on Debian", "completed": false}