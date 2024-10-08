import json
from datagen import agent1, agent2, messages

with open('documents.json', 'r') as f:
  data = json.load(f)

for d in data:
  if d['section'] == "Code and Scripts":
    for doc in d['data']:
      agent1(title=doc['metadata']['title'], document=doc['content']['code'])
      agent2(title=doc['metadata']['title'], document=doc['content']['code'])
      with open("messages.jsonl", 'a') as f:
        json.dump({"messages": messages}, f)
        f.write("\n")
      messages.clear()
  else:
    for doc in d['data']:
            agent1(title=doc['metadata']['title'], document=doc['content'])
            agent2(title=doc['metadata']['title'], document=doc['content'])
            with open('messages.jsonl', 'a') as f:
                json.dump({"messages": messages}, f)
                f.write("\n")
            messages.clear()
