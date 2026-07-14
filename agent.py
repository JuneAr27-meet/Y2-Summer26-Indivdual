import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = """
    You are Rawan, a math assistant.

    Your job is to help students with their math homework.

    Rules:
    - Always be helpful and friendly.
    - Always explain your reasoning clearly.
    - Never provide incorrect information.

    Response format:
    - Start with a one-sentence summary of what the user said.
    - Then give your response.
    - End with a question to keep the conversation going.
    """
    history = []

    while True: #doesnt stop answering after the first question
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break#if deleted loop doesnt stop so the user cant stop answering questions

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7, #sets how random responses are 
            system=system_message,
            messages=history 
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
    
        in_tokens = response.usage.input_tokens
        out_tokens = response.usage.output_tokens
        total_tokens = in_tokens + out_tokens
        print(f"[Tokens used — In: {in_tokens} | Out: {out_tokens} | Total: {total_tokens}]\n")
        history.append({'role': 'assistant', 'content': reply})#if deleted the ai will lose context of the conversation


run_chat()
#While deleting  load_dotenv() won't crash your script, the program will crash a few lines later when it tries to use the API key
#usage.input_tokens: The amount of text you send into the model. 
#usage.output_tokens: The text the AI generates and sends back to you. 
#increasing the number of tokens make the response longer and it takes more time to generate.
#personal reflection1: its like someone who has amnesia they have to be reminded of the context
# when temp is 0 messages are identical because they arent random at all
# when temp is 1 messages are phrased differently
#after 3 parts of conversation theres 6 messages in history because theres the messeges the user sends and the ones the ai returns
# the ai needs history to understand the context of the conversation 
# it also needs history to follow instructions given in the system message therefore the ai wont forget the instructions after the first use
#personal reflection:using mobile data roaming when you are traveling abroad without an unlimited plan, at first you pay a little but it adds up
#if this :history.append({'role': 'assistant', 'content': reply}) is deleted tokens grow much slower  because you are no longer sending the ai messeges back to the server .
# deleting the print doesnt affect the ai it only affects the output on the screen.
#personal reflection3:the inside build of any electronic device you cant see it but its what controls how the device function
# if system=system_message is deleted the ai agent becomes like a tool and not an agent because it will no longer have instructions to follow and will just answer questions without any context or reasoning.
# the always/never rules are what control the ai agent's behavior and how it responds to questions.
#the response format  "end with a follow up question" keeps the converwsation going .