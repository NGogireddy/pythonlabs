import openai

openai.api_key = "sk-x0000000000000000000000000000000000000000000"


def chat(prompt):
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    message = completion.choices[0].text
    return message


more_questions = True
prompt_q = "Give me a welcome message"

while more_questions:
    response = chat(prompt_q)
    print(response)
    anymore = input("Do you have any more questions (y/n) : ").lower()
    if anymore == 'n':
        more_questions = False
    else:
        prompt_q = input("Type your question and hit ENTER : ")


