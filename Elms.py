import chatterbot.trainers
from chatterbot import ChatBot
from chatterbot import filters
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import JaccardSimilarity

import spacy

npl = spacy.load('en_core_web_sm')

bot = ChatBot(
    'Elms',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    filters=[filters.get_recent_repeated_responses],
    logic_adapters=[
        {
            "import_path": 'chatterbot.logic.BestMatch',
            'chatterbot.comparisons': 'JaccardSimilarity'
        },
        'chatterbot.logic.MathematicalEvaluation',
    ]
)

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    'chatterbot.corpus.english',
    "./PKG1.yml"
)

print("Elms: hi, i am Elms a simple chatbot")

while True:
    user = input("User: ")
    if user.lower() == "q":
        print("k see u later")
        break
    rep = bot.get_response(user)
    print("Elms:", rep)
