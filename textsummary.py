import openai
import requests
import numpy as np

openai.api_key = "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"

url = "https://gist.githubusercontent.com/hackingthemarkets/e664894b65b31cbe8993e02d25d26768/raw/618afe09d07979cc72911ce79634ab5d2cc19a54/nvidia-earnings-call.txt"

def summary():
    response = requests.get(url)
    transcript = response.text
    words = transcript.split(" ")   # chunking inputs

    chunks = np.array_split(words, 6)   # splitting transcript into 6 parts for example
    sentences = ' '.join(list(chunks[0]))
    summary_responses = []

    for chunk in chunks:
        sentences = ' '.join(list(chunk))

        prompt = f"{sentences}\n\ntl;dr:"   # correct format

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.3,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=1
        )

        response_text = response["choices"][0]["text"]
        summary_responses.append(response_text)

    full_summary = "".join(summary_responses)
    return full_summary

nvidia = summary()

print(nvidia)