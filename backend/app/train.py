from transformers import DistilBertForQuestionAnswering, DistilBertTokenizerFast, Trainer, TrainingArguments
import json
from datasets import Dataset

# Load your data
with open('data.json') as f:
    data = json.load(f)

# Convert your data to the Dataset format
contexts = []
questions = []
answers = []
answer_starts = []

for entry in data['data']:
    context = entry['context']
    for qa in entry['qas']:
        contexts.append(context)
        questions.append(qa['question'])
        answers.append(qa['answers'][0]['text'])
        answer_starts.append(qa['answers'][0]['answer_start'])

dataset = Dataset.from_dict({
    'context': contexts,
    'question': questions,
    'answers': answers,
    'answer_starts': answer_starts
})

# Load pre-trained model and tokenizer
model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased-distilled-squad')

# Tokenize the data
def preprocess_function(examples):
    encodings = tokenizer(examples['context'], examples['question'], truncation=True, padding=True)
    encodings.update({'start_positions': examples['answer_starts'], 'end_positions': [start + len(ans) for start, ans in zip(examples['answer_starts'], examples['answers'])]})
    return encodings

tokenized_dataset = dataset.map(preprocess_function, batched=True)

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    eval_dataset=tokenized_dataset
)

# Train the model
trainer.train()

# Save the model
model.save_pretrained('fine-tuned-distilbert')
tokenizer.save_pretrained('fine-tuned-distilbert')
