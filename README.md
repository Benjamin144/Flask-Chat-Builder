[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Benjamin144/Flask-Chat-Builder)

# Flask-Chat-Builder

##  Flask Chat Application - Introduction
To begin a Flask project, the following will gives us a starting point for our project, by creating a new Flask project.
This will be a chat application written in Flask. The purpose of which is to take data from a URL and store the information in a list.

## Basic Routes And Views
The main routes and views that we'll be using in our project. It allows us to send messages via our URLs by creating views that will handle those URLs

## Storing Our Messages
A Python list, that allows us to store our messages as strings by appending an item to the list everytime a new message is created, displaying our chats messages, 
This renders our messages in the browser, by outputting the messages as a string

## Adding Timestamps
A timestamp that will enable us to show the time at which the message was sent by using Python's datetime module

## Creating Users
I will now store Users in a session variable. It allows us to persist usernames in a browser session to automatically redirect users to their homepage, by initialising a session and a variable

## Storing Our Messages In A Dict
I am going to create a dictionary that will allows us to store data using Key/Value pairs. This can be done using the my_dict = {}

## Refactoring To Use chat.html Instead Of A Single String
Using this HTML file will display our chat messages by passing it the necessary chat messages

## Heroku Deployment
I will use Heroku to host our project by creating a new Heroku app to host our code



## Simplifying Our Code
What is it?

Code refactoring

What does it do?

Simplifies our code
How do you use it?

By making our code more understandable


## Simple Long Polling With JavaScript
I am going to use the Long polling, This method will refresh the page after a specified period of time by using JavaScript's setTimeout function and also explore a way of making the display look better

## Creating a Message Textbox
A textbox to allow us to enter a message instead of using the URL, Improves the functionality of our chat app by creating a textbox and using the POST form method