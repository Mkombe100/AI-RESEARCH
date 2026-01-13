from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)
app.secret_key = "superkey"

myClient = OpenAI(api_key=("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"))

@app.route("/", methods=["GET", "POST"])
def theBot():
    reply_bot = ""
    input_user = ""

    if request.method == "POST":
        input_user = request.form.get("message")

        if input_user:
            response = myClient.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "your name is ORION 5.0 ,You are the best bot in the world"},
                    {"role": "user", "content": input_user}
                ]
            )
            reply_bot = response.choices[0].message.content

    return render_template("index.html",
                           input_user=input_user,
                           reply_bot=reply_bot)

if __name__ == "__main__":
    app.run()
