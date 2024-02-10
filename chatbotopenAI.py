import openai


openai.api_key=""

def chatbot_tool(prompt):
    res= openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{'role':'user', 'content':prompt}]
    )

    return res.choices[0].message.content.strip()

if __name__=="__main__":
    while True:
        user_in=input('user:' )
        if user_in.lower() in ['bye', 'exit','stop','close']:
            break

        ans = chatbot_tool(user_in)
        print("Ai-parther: ", ans)