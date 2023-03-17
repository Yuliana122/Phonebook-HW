import Model
import View


def start():
    book = Model.read()
    while True:
        n = View.menu()
        if n == 1:
            book = Model.create_contact(book)
        if n == 2:
            View.view2(book)
        if n == 3:
            book = Model.update_contact(book)
        if n == 4:
            book = Model.del_contact(book)
        if n == 5:
            break