import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import AGENT1_SYSTEM, AGENT1_USER, AGENT2_SYSTEM
load_dotenv()

client = OpenAI()
# Below we use the openrouter client to access the o1-preview model as this script is before
# I have gained access to o1-preview through OpenAI. You can change it as you need.
openrouter = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY")

messages = []

def agent1(title: str, document):
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": AGENT1_SYSTEM.format(title=title, docs=document},
              {"role": "user", "content": AGENT1_USER.format(title=title, docs=document}] + messages
  ).choices[0].message.content
  messages.append({"role": "user", "content": response})
  return response

def agent2(title: str, document):
  response = openrouter.chat.completions.create(
    model="o1-preview",
    messages=[{"role": "system", "content": AGENT2_SYSTEM.format(title=title, docs=document)}] + messages
  ).choices[0].message.content
  message.append({"role": "assistant", "content": response})
  return response
