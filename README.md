## A Useful Reddit Bot

This program allows for a reddit user to communicate through a reddit developer app to send sms notifications when a certain upvote threshold is passed.
It is written in python 2 with the use of praw and twilio.

## Motivation

Created originally to help with the problem of missing potential deals on certain subreddits, this progam solves this problem by sending sms directly to one's phone when a post recieves a certain amount of upvotes.

## Installation

Clone this repository to get started. Once it is cloned you must download both praw and twilio into python. Once that is done, you also need to create a reddit developer app. Once you have created the developer app on reddit you must edit the config file with the username, password, client_id, and client_secret. After doing this you must create a twilio account to use their api. Add your twilio account_sid, auth_token, to_phone, and from_phone to the config file. Once this is done, edit the main program's file to suit your needs. Next run the program and enjoy!
