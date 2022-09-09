
from sqlalchemy import or_
from sqlalchemy.exc import SQLAlchemyError

from db import session
from models import Notate


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args):
        try:
            return self.func(*args)
        except IndexError:
            return 'Sorry,such a note does not exist'
        except KeyError:
            return 'Sorry,user not found, try again!'
        except ValueError:
            return 'Sorry,phone number not found,try again!'


@InputError
def add(*args):
    notate = str(args[0])
    try:
        notate = Notate(
            notate=notate
            )
        session.add(notate)
        session.commit()
        return f'Notate added successful'
    except SQLAlchemyError as err:
        print(err)


@InputError
def del_notate(*args):
    _id = args[0]
    session.query(Notate).filter(Notate.id == _id).delete()
    session.commit()
    return f'Deleted notate with id {_id}'


@InputError
def del_tag(*args):
    _id = args[0]
    _ = session.query(Notate).filter(Notate.id == _id).one()
    _.tag = ''
    session.commit()
    return f'Tags deleted'


@InputError
def change_notate(*args):
    _id = args[0]
    new_notate = str(args[1])
    try:
        _ = session.query(Notate).filter(Notate.id == _id).one()
        _.notate = new_notate
        session.commit()
        return 'Notate changed successful'
    except SQLAlchemyError as err:
        return err


@InputError
def find_symb(*args):
    substring = str(args[0])
    notates = session.query(Notate).filter(or_(
        Notate.id.like(substring),
        Notate.notate.ilike(substring),
        Notate.tag.like(substring))).all()
    if notates:
        for _ in notates:
            print('_' * 88)
            print('|{:<3}|{:<100}|{:<25}|'.format(str(_.id), str(_.notate), str(_.tag)))
        print('-' * 88)
        return 'The end'
    else:
        return "Nothing find"


@InputError
def find_tags(*args):
    substring = str(args[0])
    notates = session.query(Notate).all()
    count = 0
    print('|{:^3}|{:^100}|{:^25}|'.format('id', 'notate', 'tags'))
    for _ in notates:
        if _.tag.find(substring) != -1:
            count += 1
            print('_' * 88)
            print('|{:<3}|{:<100}|{:<25}|'.format(str(_.id), str(_.notate), str(_.tag)))
    if count == 0:
        return "Nothing find"
    else:
        print('-' * 88)
        return 'The end'


@InputError
def add_tag(*args):
    _id = args[0]
    tag = ''
    for i in range(1, len(args)):
        tag += args[i] + ' '
    try:
        _ = session.query(Notate).filter(Notate.id == _id).one()
        if _.tag is None:
            _.tag = tag
        else:
            _.tag += tag
        session.commit()
        return f'Tag(s) added successful to notate id {_id}'
    except SQLAlchemyError as err:
        print(err)


@InputError
def clear(*args):
    session.query(Notate).delete()
    session.commit()
    return 'All notates deleted'


def show_notates(*args):
    print('|{:^3}|{:^100}|{:^25}|'.format('id', 'notate', 'tags'))
    for _ in session.query(Notate).all():
        print('_' * 133)
        print('|{:<3}|{:<100}|{:<25}|'.format(str(_.id), str(_.notate), str(_.tag)))
    print('-' * 133)
    return 'END'


def backing_notates(*args):
    return 'Good bye!'


def unknown_command(*args):
    return 'Unknown command! Enter again!'


def greeting(*args):
    return 'Hello! Can I help you?'


def help(*args):
    return """Commands format - Command meaning
    Command: "help" - returns a list of available commands with formatting
    Command: "hello" - returns a greeting
    Command: "add" Enter: note - adds a note to a NotateBook
    Command: "tag" Enter: number of note and tags in format 'tag1, tag2, ...'
    Command: "del notate" Enter: the number of the note you want to delete
    Command: "del tag" Enter: the number of the note whose tags you want to delete
    Command: "change" Enter: the number of the note you want to change and new note
    Command: "find notate" Enter: the text that the notes should contain
    Command: "find tag" Enter: the tag(s) that the note's tags should contain
    Command: "show"  print a book of notes
    Command: "clear"  delete a book of notes
    Command: "back" returns to the selection of work branches
    """


COMMANDS = {greeting: ['hello'], add: ['add'], backing_notates: ['back'],
            show_notates: ['show'], add_tag: ['tag'], del_notate : ['del notate'],
            del_tag : ['del tag'], change_notate: ['change'],  help: ['help'],
            find_symb: ['find notate'], clear: ['clear'], find_tags: ['find tag']}


def new_func():
    return str, list


def command_parser_not(user_command: str) -> new_func():
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                data = user_command[len(value)+1:].split(' ')
                return key, data
    else:
        return unknown_command, []




