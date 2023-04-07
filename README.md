# sasta-chatgpt
Locally hosted ChatGPT using GPT-4 API to avoid the monthly subscription.

## What is it?
This repo explores the capabilities of ~OpenAI's~ ClosedAI's GPT-4 model using the API access. The project has been appropriately named because of how ~I~ we feel about the $20 monthly subscription for using GPT-4, which is appropriately summarized by the meme below:

![image](https://user-images.githubusercontent.com/29841730/230690323-e861158b-f09e-41de-93fa-1cd866423642.png)

## How does it work?
At the moment, the project uses Flask to host a webpage locally that uses a python script under the hood that reads user's question, calls the GPT-4 API, and returns the model's response on the webpage.
