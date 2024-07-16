import os

from groq import Groq
from dotenv import load_dotenv, dotenv_values
load_dotenv()


# Initialize Client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Takes the data as Input and writes the weatherforcast as a txt file
def foodgpt(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Du bist ein AI Assistent. Du erstellst mir aus dem Input ein Rezept, mit genauer Anleitung in Schritte.",
            },
            {
                "role": "user",
                "content": f"{prompt}",
            }
        ],
        model="llama3-70b-8192",
    )
    # prints the output of the llm for testing purpose
    # print(chat_completion.choices[0].message.content)
    # writes the output to gpt.txt for further data processing
    response = chat_completion.choices[0].message.content
    processed_response = ' '.join(response.split())
    processed_response = processed_response.strip('"')
    with open("gpt.txt","w") as gpt:
        gpt.writelines(processed_response)
        gpt.close()
   
    return processed_response

# Chat funktion for testing purpose
def weather_gpt():
    while True:
        prompt = input("\n> ")
        foodgpt(prompt)



if __name__ == "__main__":
    weather_gpt()