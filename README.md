# Multilingual-Interactive-Chatbot-using-RASA-framework

A chatbot using Rasa for accessing info about languages from the [World Atlas of Languages](https://wals.info/) data. 

Dataset: https://zenodo.org/record/3731125#.YexcVv7MK3A

**Persona**: 

Chatbot Jarvis. He is a witty, funny, and charming bot. Jarvis is extremely well-educated having a specialization in language data. He is reliable and he loves helping people.

**Capabilities**:

a) List of capabilities for the chatbot - Checkpoint 8th Feb:
Greetings, Thanks, Deny, Goodbye

b) List of capabilities for the chatbot - Checkpoint 15th Feb: 
Countries where any specific language is spoken, 
Macro area  - raw->walslanguage.csv
WALS code, - id in language.csv
genus, Family of language, ISO code
Feedback with follow up conversation


#### What is Rasa?
Rasa is an open source Conversational AI framework. What I like about Rasa is you are not tied to a pre-built model or usecase (Dialogflow etc.). So you can customize it to your usecase which can be a market differentiator. Rasa is not a rule based framework (e.g. Botkit) and you don’t need to worry about putting your data in someone else’s cloud as in Dialogflow, Microsoft LUIS or Amazon Lex.

Rasa has two main components — Rasa NLU and Rasa Core.

NLU is Natural Language Understanding. Suppose the user says “I want to order a book”. NLU’s job is to take this input, understand the intent of the user and find the entities in the input. For example, in the above sentence, the intent is ordering and the entity is book. Rasa NLU internally uses Bag-of-Word (BoW) algorithm to find intent and Conditional Random Field (CRF) to find entities. 

The job of Rasa Core is to essentially generate the reply message for the chatbot. It takes the output of Rasa NLU (intent and entities) and applies Machine Learning models to generate a reply.


![image](https://user-images.githubusercontent.com/47337257/151379256-e4d342c4-4b1f-4a88-91a7-d5c1e153ddb5.png)
> Basic steps of Rasa app internally works to reply a message.

As seen in the above diagram, the input message is interpreted by an Interpreter to extract intent and entity. It is then passed to the Tracker that keeps track of the current state of the conversation. The Policy applies Machine Learning algorithm to determine what should be the reply and choses Action accordingly. Action updates the Tracker to reflect the current state.

How to run Locally
------------------ 

**Note: You need to first go to the complete_version folder in your terminal and then run the following commands.**

1. You can train the models by running:  
```rasa train```  
This will train the Rasa NLU and Core models and store them inside inside the `models/` folder of your project directory.

3. In a new terminal (or anaconda prompt if on windows) start the server for the custom action by running:  
```rasa run actions```  
This will start the server for emulating the custom action.

4. Talk to the assistant by running:  
```rasa shell```  
This will load the assistant in your terminal for you to chat.

Deploying to Slack
------------------

1. Go to your Slack app's settings page and use the **Bot User OAuth Access Token** and **Signing Secret**:

And add this in the **credentials.yml** file:

```python
slack:
  slack_token: "Bot User OAuth Access Token"
  slack_signing_secret: "Signing Secret"
  slack_channel: 
```

2. Start the action server by typing the following command in terminal:

```
rasa run actions
```

3. Start the rasa server in another terminal window:

```
rasa run -m models --enable-api --cors "*" --debug
```

This will start the server at port 5005.

6. Now you have to expose this port to the world by using ngrok, open another terminal and type:

```
ngrok http 5005
```

7. Take the above url and paste it into the **Events Subscription** page of your slack app in the following format:

```
your_url_here/webhooks/slack/webhook
```

And you should now be able to talk to your chatbot in Slack! 



And you should now be able to talk to your chatbot in Slack! 

![1_0PsFouNNE_vSX29xBc2lHQ](https://user-images.githubusercontent.com/47337257/150653289-7cd4658a-ce99-47ac-896b-af4d92c680df.gif)
