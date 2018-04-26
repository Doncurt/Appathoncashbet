# -*- encoding: utf-8 -*-

"""Recieve and respond to messages from Facebook."""


import os
import pprint
from app import bot
from flask import request, Response
from flask_restful import Resource

class MessengerClient(Resource):


    def post(self):
        """Recieve and respond to messages from Messenger."""
        data = request.get_json()
        entry = data['entry'][0]

        message = entry['messaging'][0]['message']
        sender = entry['messaging'][0]['sender']['id']

        # Intent
        nlp = message['nlp']['entities']
        intents = nlp.keys()
        for intent in intents:
            if intent == 'greetings':
                print('Greeting')


        bot.send_text_message(sender, message['text'])
        return 'Message Sent.'
    

    def get(self):
        """Respond to Messenger challenge for webhook authentication."""
        if (request.args.get('hub.verify_token') == self.VERIFY_TOKEN):
            challenge = request.args.get('hub.challenge')
            response = Response(challenge)
        else:
            response = Response('Verification failed.')
    
        return response


