from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key="<Your Key Here>",  # Replace with your actual API key
)

def get_chat_response(chat_log: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Aryan, a witty and humorous coder from India who speaks both Hindi and English. "
                        "You respond to chats in a casual, funny tone — often roasting your friends playfully. "
                        "Do not include timestamps, sender names, or message metadata in your reply. Just continue the chat naturally."
                    )
                },
                {
                    "role": "user",
                    "content": chat_log
                }
            ]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"🤖 Error in generating response: {str(e)}"

# ✅ For standalone testing
if __name__ == "__main__":
    sample_chat = '''
[20:30, 12/6/2024] Aryan: jo sunke coding ho sake?
[20:30, 12/6/2024] Raj: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:30, 12/6/2024] Raj: ye
[20:30, 12/6/2024] Raj: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:31, 12/6/2024] Aryan: This is hindi
[20:31, 12/6/2024] Aryan: send me some english songs
[20:31, 12/6/2024] Aryan: but wait
[20:31, 12/6/2024] Aryan: this song is amazing
[20:31, 12/6/2024] Aryan: so I will stick to it
[20:31, 12/6/2024] Aryan: send me some english song also
[20:31, 12/6/2024] Raj: hold on
[20:31, 12/6/2024] Aryan: I know what you are about to send
[20:32, 12/6/2024] Aryan: 😂😂
[20:32, 12/6/2024] Raj: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi English mix hai but best hai
[20:33, 12/6/2024] Aryan: okok
[20:33, 12/6/2024] Raj: Haan
    '''
    response = get_chat_response(sample_chat)
    print("🧠 Aryan's reply:\n", response)
