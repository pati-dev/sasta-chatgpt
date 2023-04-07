# sasta-chatgpt
Locally hosted ChatGPT using GPT-4 API to avoid the monthly subscription.

## What is it?
This repo explores the capabilities of ~OpenAI's~ ClosedAI's GPT-4 model using the API access. The project has been appropriately named because of how ~I~ we feel about the $20 monthly subscription for using GPT-4, which can be appropriately summarized as follows:

![image](https://user-images.githubusercontent.com/29841730/230690323-e861158b-f09e-41de-93fa-1cd866423642.png)

## How does it work?
At the moment, the project uses Flask to host a webpage locally that uses a python script under the hood that reads user's question, calls the GPT-4 API, and returns the model's response on the webpage.

**Helpful commands:**
```sh
docker run -it --rm \                
    --env OPENAI_API_KEY=<YOUR-OPENAI-API-KEY> \
    -p 5000:5000 \
    babajikifauj/gpt-4:latest
```

### Sneak-peek of the (quick & dirty) webpage hosted locally:
<img width="1787" alt="Screenshot 2023-04-07 at 7 10 22 PM" src="https://user-images.githubusercontent.com/29841730/230690705-1c5a59f5-8131-47d3-b3bb-49ea9948c640.png">
