from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from . import util
import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", { # Render refers to call that index.html inside the templates/encyclopedia directory
        "entries": util.list_entries() # Entries is a variable that holds the list of entries that list_entries in util.py returns, and is meant to be referenced then in index.html
    })
def entry(request, title):
    entries = util.list_entries()
    for entry_title in entries:
        if entry_title.lower() == title.lower(): # The reason I'm using lower is to compare if both are the same even if capitalization differs, since before I had ran into an error that the text was not rendering properly.
            content = util.get_entry(entry_title)
            html_content = markdown2.markdown(content)
            return render(request, "encyclopedia/entry.html",{
                "title": title,
                "content": html_content
            })
    raise Http404("Page not found.")

def search(request):
    query = request.GET.get("q", "") # Django looks for the GET parameter called q, if q = Python, then query = Python
    if query == "":
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "results": []
        })
    entries = util.list_entries()
    for entry in entries:
        if entry.lower() == query.lower():
            return redirect("entry", title=entry) # Goes to the URL named entry and fills in the variable title with the value of entry
    matches = [entry for entry in entries if query.lower() in entry.lower()] # returns a list of partial matches
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": matches
    })
def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip() #request.POST is a dictionary in django that contains all the date the user submitted in the form, title is the key in the dictionary, and the name given in the html file
        content = request.POST.get("content", "").strip()
        if title == "" or content == "":
            return render(request, "encyclopedia/new_page.html", {
                "error":"Title and content cannot be empty."
            })
        entries = util.list_entries()
        for entry in entries:
            if entry.lower() == title.lower():
                return render(request, "encyclopedia/new_page.html", {
                    "error": "An entry with this title already exists."
                })
        util.save_entry(title, content)
        return redirect("entry", title = title)
    return render(request, "encyclopedia/new_page.html") # If is not a POST request, then it must be a GET request, show the form

def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get("content", "")
        util.save_entry(title, content)
        return redirect("entry", title = title)
    else:
        # If is a GET request, then load the existing content
        content = util.get_entry(title) # gets the content
        if content is None:
            raise Http404("Page Not Found")
        return render(request, "encyclopedia/edit_page.html", {
            "title": title,
            "content": content
        })

def random_page(request):
    entries = util.list_entries()
    if not entries:
        raise Http404("No entries available.")
    random_entry = random.choice(entries)
    return redirect("entry", title = random_entry)
