from tkinter import *
import backend

def add_command():
    """Insert entry via button."""
    backend.insert(title_text.get(),
                    author_text.get(),
                    year_text.get(), 
                    isbn_text.get())
    listing.delete(0, END)
    listing.insert(END, 
                    (title_text.get(), 
                    author_text.get(), 
                    year_text.get(), 
                    isbn_text.get()))

def view_command():
    """View entries via button."""
    listing.delete(0, END)
    for row in backend.view():
        listing.insert(END, row)

def update_command():
    """Update entry via button."""
    backend.update(selected_tuple[0], 
                    title_text.get(), 
                    author_text.get(), 
                    year_text.get(), 
                    isbn_text.get())

def delete_command():
    """Delete entry via button."""
    backend.delete(selected_tuple[0])

def search_command():
    """Search entry via button."""
    listing.delete(0, END)
    for row in backend.search(title_text.get(), 
                                author_text.get(), 
                                year_text.get(), 
                                isbn_text.get()):
        listing.insert(END, row)

def get_selected_row(event):
    """Pre-fill fields for selected entry."""
    global selected_tuple
    index = listing.curselection()[0]
    selected_tuple = listing.get(index)

    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])

    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])

    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])

    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])

window = Tk()

window.wm_title("Book Directory")

# Labels for entry fields.
label1 = Label(window, text = "Title")
label1.grid(row = 0, column = 0)

label2 = Label(window, text = "Author")
label2.grid(row = 0, column = 2)

label3 = Label(window, text = "Year")
label3.grid(row = 1, column = 0)

label4 = Label(window, text = "ISBN")
label4.grid(row = 1, column = 2)

# Entry Fields.
title_text = StringVar()
entry1 = Entry(window, textvariable = title_text)
entry1.grid(row = 0, column = 1)

author_text = StringVar()
entry2 = Entry(window, textvariable = author_text)
entry2.grid(row = 0, column = 3)

year_text = StringVar()
entry3 = Entry(window, textvariable = year_text)
entry3.grid(row = 1, column = 1)

isbn_text = StringVar()
entry4 = Entry(window, textvariable = isbn_text)
entry4.grid(row = 1, column = 3)

# List all data.
listing = Listbox(window, height = 6, width = 35)
listing.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

# Scrollbar.
scroller = Scrollbar(window)
scroller.grid(row = 2, column = 2, rowspan = 6)

# Configure scrollbar for Listbox.
listing.configure(yscrollcommand = scroller.set)
scroller.configure(command = listing.yview)

listing.bind('<<ListboxSelect>>', get_selected_row)

# Buttons for various operations on data.
button1 = Button(window, 
                text = "View All", 
                width = 12, 
                command = view_command)
button1.grid(row = 2, column = 3)

button2 = Button(window, 
                text = "Search Entry", 
                width = 12, 
                command = search_command)
button2.grid(row = 3, column = 3)

button3 = Button(window, 
                text = "Add Entry", 
                width = 12, 
                command = add_command)
button3.grid(row = 4, column = 3)

button4 = Button(window, 
                text = "Update Selected", 
                width = 12, 
                command = update_command)
button4.grid(row = 5, column = 3)

button5 = Button(window, 
                text = "Delete Selected", 
                width = 12, 
                command = delete_command)
button5.grid(row = 6, column = 3)

button6 = Button(window, 
                text = "Close", 
                width = 12, 
                command = window.destroy)
button6.grid(row = 7, column = 3)

# Keep window open until closed.
window.mainloop()