# Milestone Project 3: Bibilio Book Search Engine


This website is a search engine for books, and hosts a collection of books with a summary of what the book is about, the author's name, publication date and link to purchase the book.


## UX

User experience process is for clarity and conciseness when streaming user with information when they are utilising the application, and for an intuitive navigation. Therefore, minimalistic designs are adopted. 

User's requirements:
* As a user I want to find a book
* As a user I want to get a link to the page of the details of the book I searched for from the home page, if the book is available in the website's library
* As a user I want to know more about the book's contents, and publication details
* As a user I want to easily go back to the search engine if no results were found, or if I made a typing error
* As a user I want a link that gets me to an online store to purchase the book I looked up for
* As a user I want to see the full list of books available in the website


## Design
Minimal and straight to the point. 


## Features

User is able to search for books based on title, regardless if the string is a substring or a complete string, and search is not affected by the case of the letters. 


## Features Left to Implement

1) A working dropdown navigation bar from Bootstrap 4, JQuery. Attempt to instal resulted to the navigation button closing too quickly before user can view the navigation contents.
2) Ability for user to leave a review for the books they were looking for
3) Increase the database of books in the website, by outsourcing data from MongodB
4) Allow for user to search for the author's name in the search bar

## Technologies Used

### Python, Flask, and Jinja

Using Flask and Jinja for template inheritence to minimise coding efforts. Python was used to structure logic on how the search results page should evolve depending on user input. 

### HTML5, GoogleFonts
For minimalistic styling. 

### Bootstrap 4
Using Bootstrap 4 to allow page to be responsive on different platforms/window sizes. 



## Testing

### Manual Testing

[HTML Validation](https://www.freeformatter.com/html-validator.html)

Google Inspect

AWS Cloud9 IDE



## Development 
Scripts were written and tested in the AWS Cloud9 IDE, evolving from  static html files to platform-responsive and user interaction dependent html files, powered by Python, Flask with Jinja codes.
Intermitently, the static version of the project was saved to [my Github repository](https://github.com/farahroslend/bibliopip3) for version tracking and control. The application version of the website is deployed to Heroku and is available here: (https://biblio-flask-mongo.herokuapp.com/)

## Heroku Deployment Steps

1. Create new app in Heroku, with the IP=0.0.0.0 and PORT=8080
2. *$ heroku login -i*
2. *$ heroku apps*
3. *$ git init*
4. *$ git commit -m 'progress log here'*
5. *$ heroku git: remote-a-biblio-flask-mongo*
6. *$ git push heroku master*
7. Create requirement.txt, Procfile files as instructions for Heroku to run app
8. *$heroku ps:scale web=1*

## Content
Took inspiration from the website layout from Google Books. 

## Media
The 'Biblio' image above the search bar was created from [fontmeme](https://fontmeme.com/)
Book images and descriptions were sourced from [Amazon](https://www.amazon.com/)

