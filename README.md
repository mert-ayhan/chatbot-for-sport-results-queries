# Chatbot for Sport Results Queries

## Objective
Develop a chatbot that enables users to query sports results, player performances, and match statistics efficiently.

## Technologies Used
- **Backend:** FastAPI
- **Frontend:** React with Vite and Tailwind CSS
- **Model:** DistilBERT for Question Answering
- **Programming Languages:** Python (backend), TypeScript (frontend)

## Project Structure

### Backend
- `requirements.txt` - Lists the dependencies for the backend.
- `run.py` - Entry point to run the FastAPI application.
- `test.py` - Script to test the question-answering model.
- `app/` - Directory containing the main application files.
  - `main.py` - FastAPI application file.
  - `train.py` - Script to fine-tune the DistilBERT model.
  - `data.json` - Sample data for training the model.
  - `__init__.py` - Initialization file for the app module.
  - `fine-tuned-distilbert/` - Directory to store the fine-tuned model.

### Frontend
- `src/App.tsx` - Main React component.
- `src/App.css` - Styles for the React application.

## Setup Instructions

### Backend
1. **Create and activate a virtual environment:**
```bash
  python -m venv .venv
  source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

2. **Install the dependencies:**
```bash
  pip install -r requirements.txt
```

3. **Train the model:**
```bash
  python app/train.py
```

4. **Run the application:**
```bash
  python run.py
```

### Frontend
1. **Install the dependencies:**
```bash
  npm install
```

2. **Run the development server:**
```bash
  npm run dev
```

## Testing the Model
Run the test.py script to test the question-answering model:
```bash
  python test.py
```