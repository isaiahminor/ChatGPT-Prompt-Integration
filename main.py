import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
  question = input("\033[35mAsk me a question.. any question, as you wish:\n\033[0m")

  if question.lower() == "exit":
    print("\033[35mSee you later, thanks for using me!\033[0m")
    break

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a very helpful assistant, who gives the best answers. Answer the given question."},
    {"role": "user", "content": question}
  ]
)

  print("\033[32m" + completion.choices[0].message.content + "\n")
