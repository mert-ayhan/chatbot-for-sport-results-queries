from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
question_answerer = pipeline("question-answering", model='./app/fine-tuned-distilbert', tokenizer='./app/fine-tuned-distilbert')

context = r"""
The much-anticipated football match between Galatasaray and Fenerbahçe took place yesterday at the Türk Telekom Stadium in Istanbul.
The match, which is part of the Turkish Süper Lig, ended with a thrilling victory for Galatasaray.
Galatasaray emerged victorious with a final score of 3-2 against their arch-rivals Fenerbahçe.
The first goal of the match was scored by Galatasaray's forward, Radamel Falcao, in the 15th minute.
Fenerbahçe quickly responded with a goal from their star player, Mesut Özil, in the 25th minute, leveling the score to 1-1.
As the game progressed, Galatasaray took the lead again with a stunning goal by Arda Turan in the 40th minute.
The second half of the match saw intense action from both teams, with Fenerbahçe's striker, Enner Valencia, equalizing the score once more at 2-2 in the 60th minute.
However, Galatasaray sealed their victory with a decisive goal from Younès Belhanda in the 75th minute.
The match was attended by thousands of fans, who witnessed an exhilarating display of football prowess from both sides.
The win places Galatasaray at the top of the league standings, further intensifying the competition in the Turkish Süper Lig.
"""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Query(BaseModel):
    question: str

greetings = {"hi": "Hello! How can I help you?"}

@app.post("/ask")
def ask_question(query: Query):
  if query.question.lower() in greetings:
    print('Greeting detected')
    print(greetings[query.question.lower()])
    return {
        "answer": greetings[query.question.lower()]
    }
  else:
    return question_answerer(question=query.question, context=context)
