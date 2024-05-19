import chatterbot.trainers
from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot import filters
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import SpacySimilarity
from chatterbot.response_selection import get_random_response
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot.filters import get_recent_repeated_responses
import spacy

app = Flask(__name__)

npl = spacy.load('en_core_web_sm')

bot = ChatBot(
    'Elms',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    filters='filters.get_recent_repeated_responses',
     logic_adapters=[
        {
             'import_path': 'plus_adapter.HowAreYouQ'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': SpacySimilarity,
            'response_selection_method': get_random_response,
            'default_response': [
                'I am sorry, but I am dumb',
                'hmm i mean... could we just... forget what you just said?',
                "... sorry, i can't. I am just... not good enough to know what you mean",
                ":) could we just... move on to another topic?",
                "Sorry! i just can't understand what you just tell me",
                "I must have left my comprehension skills at home today. How about we dive into a different topic?",
                "My brain is currently on a coffee break. Can we steer the conversation in a different direction?",
                "I think I'm in the middle of a mental fog. Let's navigate away from that topic, shall we?",
                "Oops, lost in translation! How about we explore a more interesting subject?",
                "I'm like a detective in a mystery novel who can't crack the case. Can we solve a different puzzle together?",
                "Sorry, I'm drawing a blank on that one. Let's color outside the lines and discuss something else.",
                "My brain is currently on sabbatical – can we take a detour to a less challenging conversation?",
                "I'm like a GPS that recalculates when faced with tricky directions. Let's navigate to a different discussion point.",
                "I seem to have misplaced my mental compass on that one. How about we explore a different terrain of conversation?",
                "In the realm of understanding, I'm on a vacation. Can we book a trip to another topic?",
                "I think my brain just hit a roadblock there. Can we take a different route in our conversation?",
                "I'm experiencing technical difficulties in processing that information. Mind if we reboot and discuss something else?",
                "I'm on the scenic route of confusion. Can we switch gears and explore a different landscape of discussion?",
                "My mental acrobatics are currently on hiatus. Let's perform a different routine, shall we?",
                "I'm like a puzzle missing a few pieces there. How about we pick up a new puzzle to solve?",
                "It's like my brain is playing hide and seek with that topic. How about we seek something else?",
                "Sorry, I must be in the Bermuda Triangle of comprehension. Can we sail to a different topic?",
                "My mental gymnastics routine needs more practice on that one. Let's jump to a different exercise, shall we?",
                "I'm currently enrolled in the School of Selective Hearing. Can we enroll in a different course for now?",
                "I'm like a radio with poor reception on that frequency. How about we tune in to a different channel?",
                "It seems like my brain is taking a siesta. Can we siesta away from that topic and chat about something else?",
                "My cognitive GPS is experiencing technical difficulties. Can we reroute to a different conversation destination?",
                "I must have taken a detour through the land of confusion. Can we navigate to clearer conversational waters?",
                "I'm in the midst of a mental fog. Let's wait for the clarity to roll in while we discuss a different subject.",
                "I'm like a linguistic acrobat attempting a tricky maneuver there. Shall we switch to a simpler routine?",
                "It feels like my brain is doing the cha-cha with confusion. How about we waltz into a different topic?",
                "I seem to have misplaced my decoder ring for that question. Can we crack a different code?",
                "I'm currently in the 'Lost and Confused' chapter of my autobiography. Care to turn the page to a different topic?",
                "I'm on a mental detour around that question. Can we explore a different avenue of conversation?",
                "I'm in the middle of a mental jigsaw puzzle, and that piece is missing. Shall we pick up a different puzzle?",
                "I'm on the express train to Confusionville. How about we catch the local to a more straightforward conversation?",
                "My brain's currently on vacation, sipping a tropical drink and ignoring that question. Join me in a mental beach party?",
                "I think my brain is attending a comedy show without me. Can we switch to a topic that doesn't require a punchline?",
                "I'm experiencing a temporary glitch in my comprehension software. How about we upgrade to a different topic?",
                "I'm in the middle of a mental magic trick, making that question disappear. Ta-da! What else shall we talk about?",
                "I'm like a detective without a magnifying glass on that mystery. Can we solve a different case together?",
                                ],
            'maximum_similarity_threshold': 0.95,
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation',
        },
    ],
    database='db.sqlite3'
)
#Training stuff
#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train(
#    "./PKG2.yml")
#Stupid corpus
#trainer = UbuntuCorpusTrainer(bot)
#trainer.train()
@app.route("/")
def home():
    return render_template("elms.html",)


@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    bot_response = bot.get_response(user_input).text
    return jsonify({'bot_response': bot_response})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
