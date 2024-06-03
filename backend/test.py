from transformers import pipeline
question_answerer = pipeline("question-answering", model='distilbert-base-uncased-distilled-squad')

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

result = question_answerer(question="Who scored the first goal?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = question_answerer(question="Where was the match played?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = question_answerer(question="What was the final score?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = question_answerer(question="Who scored the winning goal?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = question_answerer(question="Who scored Fenerbahçe's first goal?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = question_answerer(question="Who scored Fenerbahçe's second goal?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = question_answerer(question="Which league is the match part of?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = question_answerer(question="Who scored Galatasaray's second goal?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = question_answerer(question="Who is Fenerbahçe's star player?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = question_answerer(question="What is the name of Galatasaray's stadium?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")
