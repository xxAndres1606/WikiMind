# WikiMind

## Overview

This Wiki project is a Wikipedia-style web application built using Django. It allows users to view, search, create, and edit encyclopedia entries, all stored as Markdown files.

The application converts Markdown content into HTML for display, providing a dynamic and interactive browsing experience.

---

## Features

- **Index Page**
  - Lists all encyclopedia entries as clickable links


- **Entry Page**
  - Displays the content of a requested encyclopedia entry
  - Converts Markdown to HTML for proper formatting

- **Search Functionality**
  - Supports exact match searches
  - Displays partial matches if no exact match is found

- **Create New Page**
  - Allows users to create a new encyclopedia entry
  - Prevents overwriting an existing entry

- **Edit Page**
  - Enables editing existing entries
  - Pre-fills form with the current Markdown content for easy updates

- **Random Page**
  - Redirects the user to a randomly selected entry
 
---

## Technologies Used

- Python 3
- Django
- HTML5
- CSS3
- Markdown2 library

---

## How to Run

1. Clone this repository:

    '''bash
   
     pip install django markdown2
   
     '''

2. Install dependencies (optional if using a venv (virtual environment)):

   '''bash
   
   pip install django markdown2
   
   '''

4. Run the Django development server:
   
     '''bash
   
     python manage.py runserver
   
     '''

5. Open your browser and go to the given URL by the terminal
   
    '''
  
    http://127.0.0.1:8000/
  
    '''
---

## File Structure

- "encyclopedia/" --> Django app containing views, urls, and templates
- "entries/" --> Folder where Markdown files for each entry are stored
- "wiki/" --> Django protect settings and configurations
- "templates/" --> HTML templates for different pages
- "static/" --> CSS styling files

---

## Notes

- All content is stored as Markdown files and converted to HTML for rendering.
- Project was built to fulfill the specifications of CS50W Project 1.

---

## Author

Andres Alejandro Andrade Fierro

aaandrade0408@gmail.com

https://github.com/xxAndres1606?tab=repositories

---

## Acknowledgments

- Harvard CS50 Web Programming with Python and JavaScript
