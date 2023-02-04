from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot=ChatBot("Robo")

training_data = open('training_data/personal_ques.txt').read().splitlines()

trainer = ListTrainer(chatbot)
trainer.train(training_data)

trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 