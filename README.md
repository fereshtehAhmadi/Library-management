# Library management
This site is designed for better and easier management of the library.

## Tecnology
#### python 3.10.2
|Packages           |Version|
|--------           |-------|
|django             |3.2.13 |
|celery             | 5.2.7 |
|django-social-share| 2.2.1 |
|Faker              |13.12.0|

# How to install and run project?
1.Go into virtual environment and run the command in below:

```
$ pip install -r requirments.txt 
```

2.python manage.py runserver


# How does this project work?
Initially a list of books is displayed, and the book's search capability is based on the name of the book, the author's name and the subject in the navbar.
They can also view existing books by clicking on the author's name or topics in the category.

Click on the details button, the specific details of each book and the number of likes and comments can be seen.

Users can use features such as: bookmark, share books and ... after registering and completing information.

You can also, if you don't find your favorite book, offer it via Book request.

If users information are approved by library staff, they can borrow up to 5 books from the library simultaneously and submit their comments on them.

If the books are not returned after 30 days, it will include penalties and will not be able to receive a new book until the penalty is paid.

Library employees also have features such as adding new books, editing and deactivating books, viewing users 'list and their specifications, confirming users' membership, and so on.

The penalty calculation section is processed by celery each midnight and the amount of delay in delivery is applied for each week.

