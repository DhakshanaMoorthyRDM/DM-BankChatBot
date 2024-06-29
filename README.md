
# Bank Chatbot - DM Bot - BUDDY

BUDDY is an intelligent chatbot designed to provide informative answers to a wide range of bank-related inquiries. Leveraging advanced machine learning techniques, BUDDY is built using a custom dataset of customer questions and responses. It is fine-tuned with deep learning models (powered by PyTorch) to understand the nuances of natural language. By employing NLP methods like stemming, tokenization, and lemmatization, BUDDY can effectively process and interpret customer queries, resulting in an exceptional accuracy rate in addressing their banking needs.

## Folder Structure

To deploy this project run

```bash
  Bank-Chatbot/
│
├── app.py
├── chat.py
├── data.pth
├── intents.json
├── model.py
├── nltk_utils.py
├── train.py
├── trial.py
└── requirements.txt

```

## Project Overview

The primary goal of BUDDY is to assist customers with their banking-related questions by providing accurate and timely responses. This is achieved through the following key steps:

Data Preparation: Load and preprocess the dataset containing customer questions and responses.
Model Training: Train a deep learning model using PyTorch on the prepared dataset.
Natural Language Processing: Utilize NLP techniques such as stemming, tokenization, and lemmatization to process customer queries.
Chatbot Deployment: Deploy the trained model using Flask to interact with customers and provide responses based on their inquiries.

## Libraries Used

This project utilizes the following libraries:

Pandas: For data manipulation and analysis

NumPy: For numerical computations

PyTorch: For building and training the deep learning model

NLTK (Natural Language Toolkit): For text processing

word_tokenize: For tokenizing text

WordNetLemmatizer: For lemmatizing words

stopwords: For removing stop words

Flask: For building the web application

JSON: For handling JSON data

## Getting Started

To get started with the project, follow these steps:

1.Clone the repository:
```bash
git clone https://github.com/yourusername/Bank-Chatbot.git
cd Bank-Chatbot
```

2.Install the required libraries:
```bash
pip install -r requirements.txt

```
3.Prepare the dataset by placing your intents.json file in the project directory.

4.python train.py

```bash
python train.py
```

5.Run the Flask application:

```bash
export FLASK_APP=app.py
flask run
```

Alternatively, on Windows, use:

```bash
set FLASK_APP=app.py
flask run
```

6.Open your web browser and navigate to http://127.0.0.1:5000/ to interact with BUDDY.

## Files Description
app.py: Contains the Flask application code to run the chatbot.

chat.py: Handles the chat interface and interactions.

data.pth: Stores the trained model parameters.

intents.json: Contains the dataset of customer questions and responses.

model.py: Defines the neural network architecture.

nltk_utils.py: Includes utility functions for text processing using NLTK.

train.py: Script for training the model.

trial.py: A script for testing and debugging purposes.

requirements.txt: Lists all the dependencies required to run the project.

## Acknowledgements

The developers and maintainers of the libraries used in this project.

The contributors to the custom dataset of customer questions and responses.

Feel free to explore, contribute, and provide feedback!

