from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

mybot = ChatBot("PizzaBot",storage_adapter="chatterbot.storage.SQLStorageAdapter")

training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()

training_data = training_data_quesans

trainer = ListTrainer(mybot)
trainer.train(training_data)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(mybot.get_response(userText))

if __name__ == "__main__":
    app.run()