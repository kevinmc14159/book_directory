# Book Directory
*Book Directory* is a database app built with Python, Tkinter, and SQLite.

## How to Use
To launch the GUI, open the *frontend.py* script via the console. To add an entry into the database, fill in the Title, Author, Year, and ISBN fields and click the *Add Entry* button. To view all database entries, click the *View All* button. To search if a particular entry exists, type the text to search in its corresponding field and click the *Search Entry* button. To update an entry, click the *View All* button, then click on the entry to update, fill in the new fields, and click the *Update Selected* button. To delete an entry, click the *View All* button, then click on the entry to delete and click the *Delete Selected* button. Lastly, to close the app, click the *Close* button.

## Technologies Utilized
* Tkinter
* SQLite

## Key Concepts Applied
* Data Types
* Operators
* Looping
* Functions
* Modules
* Files & I/O

## What I Learned
* The main steps for working with a SQLite database are connecting to a database, creating a cursor object, writing an SQL query, commiting changes, and closing the database connection.
* GUIs can be built with Tkinter windows and widgets. Tkinter arranges label, entry, and button widgets in a window using a grid layout. The button widgets can be linked to functions and the data in entry widgets can be extracted for use elsewhere.
* Various Python files can interact with each other as modules. This allows for the principle of abstraction, where code can be used without knowing precisely how it was implemented. For this project, the frontend and backend were developed independently and later connected.