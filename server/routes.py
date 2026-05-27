
import subprocess

from flask import request, render_template, make_response

from server.webapp import flaskapp, cursor
from server.models import Book


@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = bool(request.args.get('read'))

    if name:
        cursor.execute(
            "SELECT * FROM books WHERE name LIKE %s", name
        )
        books = [Book(*row) for row in cursor]

    elif author:
        cursor.execute(
            "SELECT * FROM books WHERE author LIKE :author", {'author': f"%{author}%"}

        )
        books = [Book(*row) for row in cursor]

    else:
        cursor.execute("SELECT name, author, read FROM books")
        books = [Book(*row) for row in cursor]
        
    return render_template('books.html', books=books)


@flaskapp.route('/codeql-demo/command-injection')
def codeql_demo_command_injection():
    # Intentionally vulnerable for CodeQL training/demo purposes.
    # This endpoint is isolated from normal app functionality.
    user_text = request.args.get('text', '')
    return subprocess.check_output(
        f"echo Demo output: {user_text}",
        shell=True,
        text=True,
    )
