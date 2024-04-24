# Word Search and Indexing Tool
### Codemonk-Assignment

REST API that takes in multiple paragraphs of text as input, and stores each paragraph and the words-to-paragraph mappings on a PostgreSQL database.

## Table of Contents
- [Word Search and Indexing Tool](#word-search-and-indexing-tool)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Installation](#installation)
  - [API Documentation](#api-documentation)
  - [API Endpoints](#api-endpoints)

## Description
Project Text Analysis and Indexing is an API designed to handle text paragraphs, index words in those paragraphs, and provide search functionality based on user queries It lets the users insert multiple paragraphs of text and save paragraphs respectively, and word mappings are performed to different classifications of a PostgreSQL database. The API converts all words to lowercase by tokenizing words by dividing them into white space and displays these words to the paragraph from which they originate. Each paragraph is defined by two additional characters.

Users can use the API to search categories for specific words and get the top 10 categories where the word is located. In addition, the API provides endpoints to manage users (requiring authentication), register all users, create new users, list all paragraphs, create new paragraphs, save paragraphing and indexing and input processing

Key features include:

  - Words require a function to retrieve paragraphs containing specific words.
  - User authentication provides secure access to API endpoints.
  - CRUD functions for managing users and distributions.
  - Automatic word indexing and paragraph storage in a PostgreSQL database.

The project aims to provide robust solutions for information analysis, indexing, and searching, facilitating various applications such as content management systems, document analysis tools, and information retrieval systems

## Features
Main key features of this project :

1. Word Search Functionality
2. User Authentication
3. User Management
4. Paragraph Management
5. Text Processing
6. Data Storage
7. API Documentation
8. RESTful API Design

## Installation

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/AkashSriv13/Codemonk-Assignment.git
$ cd Codemonk-Assignment
```


Then install the dependencies:

```sh
$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
$ set DB_PASSWORD='Enter Your Postgres Password'
```
```sh
$ python manage.py migrate
```
```sh
$ python manage.py runserver
```
After compiling the `manage.py` file navigate to the test link

Navigate to `http://127.0.0.1:8000/`.

After this you will get these URL patterns

```sh
admin/
swagger/ [name='schema-swagger-ui']
redoc/ [name='schema-redoc']
users/ [name='user-list']
paragraphs/ [name='paragraph-list']
text-input/ [name='text-input']
search/ [name='search-word']
```

## API Documentation

Navigate to the `http://127.0.0.1:8000/swagger/`

You will see the API Documentation

![WhatsApp Image 2024-01-31 at 21 45 43_8968ad33](https://github.com/AkashSriv13/Codemonk-Assignment/assets/120120817/1eb46fbf-3b4f-4e02-9c8d-9e1ba93d64ac)
![WhatsApp Image 2024-01-31 at 21 46 24_d2f6b300](https://github.com/AkashSriv13/Codemonk-Assignment/assets/120120817/f3a0dfaf-b310-4ad4-be3a-9d68676ec77f)
![WhatsApp Image 2024-01-31 at 21 50 44_65d7201c](https://github.com/AkashSriv13/Codemonk-Assignment/assets/120120817/a5309e3c-daf3-41fc-8b1b-387b550c4ca3)


## API Endpoints

All API Endpoints of this project are :-

Here are all the API endpoints provided by the project:

1. Search Word API:
   - URL: `/search/`
   - Method: GET
   - Description: Search for paragraphs containing a specific word.
   - Parameters:
     - `word` (query parameter): The word to search for in paragraphs.
   - Response: Returns a list of paragraphs containing the specified word.

2. User List API:
   - URL: `/users/`
   - Method: GET
   - Description: List all users.
   - Response: Returns a list of all users stored in the database.

3. Create User API:
   - URL: `/users/`
   - Method: POST
   - Description: Create a new user.
   - Request Body: User details (name, email, date of birth).
   - Response: Returns the newly created user with a success status.

4. Paragraph List API:
   - URL: `/paragraphs/`
   - Method: GET
   - Description: List all paragraphs.
   - Response: Returns a list of all paragraphs stored in the database.

5. Create Paragraph API:
   - URL: `/paragraphs/`
   - Method: POST
   - Description: Create a new paragraph.
   - Request Body: Paragraph content.
   - Response: Returns the newly created paragraph with a success status.

6. Text Input API:
   - URL: `/text-input/`
   - Method: POST
   - Description: Process a paragraph of text.
   - Request Body: Paragraph content.
   - Response: Returns a success message indicating that the paragraph has been processed.
