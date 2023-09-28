# Electrabot

Ai Chat bot with Python.
This project is a conversational AI chatbot with web-scraping/summary features. 
Inside the backend folder is where the magic happens, all the ai logic and web-scraping is in there.

Created in collaboration with Brandon Kaplun, Daniel Ivanov, Maria Arias Miranda, Karen Lazo, Ricardo Rodriguez at Union College of Union County NJ. 

Built with:
 Python - AI logic  
 Flask - Backend  
 React - Frontend  
 Postgres - Database  

## Installation

### BACKEND FOLDER
 
Cd into the backend folder.  
cd backend  

Start by creating a virtual enviorment.  
python3 -m venv env   

Start the venv:  
source env/bin/activate or  . env/bin/activate  

Install all libreries:  
pip install beatifulsoup4 gensim flask requests torch torchvision nltk bs4  

Run this once in your terminal:  
$ python  
>>> import nltk  
>>> nltk.download('punkt')  

### FRONTEND FOLDER
 
Cd into the frontend folder.  
cd frontend  

Install all dependencies.  
npm i or npm install  

## Usage
 
After installing everything, cd into the backend and start the sever:  

(activate virtual enviorment first)  
source env/bin/activate or  . env/bin/activate  

run: 
python train.py <- ( Most run this everytime to train the bot. )  
python chat.py <- ( Runs in your terminal )  

python main.py <- ( Runs on localhost with React UI )  

## Contributing

Have a look at intents.json Define a new tag, possible patterns, and possible responses for the chat bot. You have to re-run the training whenever this file is modified.  

You can also look at the web_scraper.py and customize to your needs.  

## PICTURES 

<img width="1417" alt="Screenshot 2023-07-30 at 2 56 18 PM" src="https://github.com/RicaRodz/AI-Chat-Bot-with-Python/assets/101608021/1eed599c-66f4-4945-9d6e-ed72d4a5a815">
<img width="1368" alt="Screenshot 2023-07-30 at 2 56 39 PM" src="https://github.com/RicaRodz/AI-Chat-Bot-with-Python/assets/101608021/f2751bdf-3f7e-4349-9025-a1a40ed86159">
<img width="1375" alt="Screenshot 2023-07-30 at 2 57 38 PM" src="https://github.com/RicaRodz/AI-Chat-Bot-with-Python/assets/101608021/65241790-78dc-4c13-b120-deaa366f7317">
