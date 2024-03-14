from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client= OpenAI(api_key  = os.getenv('OPENAI_API_KEY'))


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


text = f"""
Hello everyone,
If you've been experiencing 503 status code errors when trying to access your app deployed on our platform fly.io , below is step-by-step guide to help you troubleshoot and resolve the issue:

1.Review your app's configuration, including any settings specific to the deployment on Fly.io.also make sure you have configured the regions correctly and that there are no typos or errors in the configuration files.

2.Take a look at the application logs for any potential errors or warnings, These logs can provide valuable insights into what is causing the 503 errors. Look for error messages, or warnings that might indicate the root cause.

3.Ensure that your app's resource usage, such as memory and CPU, are within acceptable limits. High resource usage can lead to poor performance and errors.

4.If your app relies on external services like databases, APIs, etc., check their availability and responsiveness. Sometimes, 503 errors can be caused by issues related to dependencies.

5. you can checkout our documentation and community forums which can be incredibly helpful in addressing common issues. there have been similar problems posted at https://community.fly.io and solutions were suggested. There might be posts that correlate with your situation.

6. you can also use network monitoring tools to track the flow of traffic to your app. This can help you identify spikes that might correlate with the 503 errors.

"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)