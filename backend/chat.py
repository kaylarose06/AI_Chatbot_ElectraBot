import random
import json
import requests
import torch

from web_scraper import scrape_website
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
            elif tag == "weather":
                params = { 'access_key': '47be14d98287e6ea38745fbfa17d625f','query': 'New Jersey'}
                api_result = requests.get('http://api.weatherstack.com/current', params)
                api_response = api_result.json()
                return (u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']) )
            elif tag == "academics":
                url = 'https://www.ucc.edu/academics/'
                return scrape_website(url) + " For more information go to: https://www.ucc.edu/academics/ "
            elif tag == "admissions":
                url = 'https://www.ucc.edu/admissions/'
                return scrape_website(url) + " For more information go to: https://www.ucc.edu/admissions/"
            elif tag == "apply":
                url = 'https://www.ucc.edu/admissions/apply/'
                return scrape_website(url) + " For more information go to: https://www.ucc.edu/admissions/apply/"
            elif tag == "financial aid":
                url = 'https://www.ucc.edu/admissions/paying-for-college/'
                return scrape_website(url) + " For more information go to: https://www.ucc.edu/admissions/paying-for-college/"
            # elif tag == "admissions":
            #     url = 'https://www.ucc.edu/admissions/'
            #     return scrape_website(url) + " For more information go to: https://www.ucc.edu/admissions/"
            # elif tag == "admissions":
            #     url = 'https://www.ucc.edu/admissions/'
            #     return scrape_website(url) + " For more information go to: https://www.ucc.edu/admissions/"
            # elif tag == "admissions":
            #     url = 'https://www.ucc.edu/admissions/'
            #     return scrape_website(url) + " For more information go to: https://www.ucc.edu/admissions/"
            # elif tag == "admissions":
            #     url = 'https://www.ucc.edu/admissions/'
            #     return scrape_website(url) + " For more information go to: https://www.ucc.edu/admissions/"
            # elif tag == "admissions":
            #     url = 'https://www.ucc.edu/admissions/'
            #     return scrape_website(url) + " For more information go to: https://www.ucc.edu/admissions/"
    return "I do not understand..."


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)

