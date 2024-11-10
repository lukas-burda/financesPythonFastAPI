#Backend of Finances

## Requirements

- Python 3.10
- FastAPI
- SQLAlchemy
- Pydantic

## Suggestion - Create an virtual environment
1. Create a virtual environment
    - Windows: `python -m venv meu_ambiente_virtual`
    - Linux: `python3 -m venv meu_ambiente_virtual`
    - Mac: `python3 -m venv meu_ambiente_virtual`

2. Activate the virtual environment
    - Windows: `meu_ambiente_virtual\Scripts\activate`
    - Linux: `source meu_ambiente_virtual/bin/activate`
    - Mac: `source meu_ambiente_virtual/bin/activate`

3. Install the requirements
4. Run the application

## How to run

1. Clone the repository
2. Run `pip install -r requirements.txt`
3. Run `uvicorn src.main:app --reload --port 8080`
4. Open your browser and go to `http://127.0.0.1:8000/docs` to see the documentation
