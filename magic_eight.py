import random
def ask_question():
	question = input("What is your question?")
        if question[-1] != "?":
            print("Sorry, I can only answer a question")
        else:
            return question
print(ask_question())

answers = ["It is certain", "It is decidedly so", "Without a doubt",
"Yes definitely", "You may rely on it", "As I see it, yes", "Most likely",
"Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later",
"Better not tell you now", "Cannot predict now", "Concentrate and ask again",
"Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def get_answer():
	randnum = random.randrange(0,19)
	return answers[randnum]
print(get_answer())
