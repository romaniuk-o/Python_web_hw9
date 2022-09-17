import re
from collections import UserDict
from datetime import datetime
from datetime import date
from sqlalchemy import or_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

from db import session
from models import Contact, PhoneToContact


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'


class Name(Field):
    pass


class MailExists(Exception):
    pass


class AdressExists(Exception):
    pass


class IncorrectEmailFormat(Exception):
    pass


class IncorrectAdressFormat(Exception):
    pass


class PhoneNumberError(Exception):
    pass


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.__value = None
        self.value = value

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value) -> None:
        codes_operators = ["067", "068", "096", "097", "098", "050",
                           "066", "095", "099", "063", "073", "093"]
        new_value = (value.strip().
                     removeprefix('+').
                     replace("(", '').
                     replace(")", '').
                     replace("-", ''))
        if new_value[:2] == '38' and len(new_value) == 12 and new_value[2:5] in codes_operators:
            self.__value = new_value
        else:
            raise PhoneNumberError

    def get_phone(self) -> str:
        return self.value


class Birthday(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.__value = None
        self.value = value

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value) -> None:
        if value:
            try:
                datetime.strptime(value, "%d.%m.%Y")
            except ValueError:
                raise ValueError("Incorrect data format, should be DD.MM.YYYY")
        self.__value = value


class Mail(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.__value = None
        self.value = value

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(regex, value):
            self.__value = value
        else:
            raise IncorrectEmailFormat

    def get_email(self) -> str:
        return self.value


class Adress(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.__value = None
        self.value = value

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        regex = r'^([\w]([\.,]?)([\s]?)){1,60}$'
        if re.match(regex, value):
            self.__value = value
        else:
            raise IncorrectAdressFormat

    def get_adres(self) -> str:
        return self.value


def days_to_birthday(data_):
    if data_:
        start = date.today()
        birthday_date = data_
        end = date(day=birthday_date.day, month=birthday_date.month, year=start.year)
        count_days = (end - start).days
        if count_days < 0:
            count_days += 365
        return count_days
    else:
        return 'Unknown birthday'


# class Record:
#     def __init__(self, name: Name, phones=[], mails=[], adress=[], birthday: Birthday = None) -> None:
#         self.name = name
#         self.phone_list = phones
#         self.birthday = birthday
#         self.mails = mails
#         self.adress = adress
#
#     def __str__(self) -> str:
#         return f'User {self.name} - Phones: {", ".join([phone.value for phone in self.phone_list])}' \
#                f' - Birthday: {self.birthday} - Email: {", ".join([mail.value for mail in self.mails])}' \
#                f' - Adress: {", ".join([adres.value for adres in self.adress])}'
#
#     def add_phone(self, phone: Phone) -> None:
#         self.phone_list.append(phone)
#
#
#     def get_phones(self) -> str:
#         if not self.phone_list:
#             return 'No phones'
#         return ', '.join([phone.get_phone() for phone in self.phone_list])
#
#     def edit_phone(self, phone: Phone, new_phone: Phone) -> None:
#         for el in self.phone_list:
#             if el.get_phone() == phone.get_phone():
#                 self.phone_list.remove(el)
#                 self.phone_list.append(new_phone)
#                 return f"Email {phone} was changed to {new_phone}"
#
#
#     def add_email(self, mail: Mail):
#         self.mails.append(mail)
#
#     def get_emails(self) -> str:
#         if not self.mails:
#             return 'No emails'
#         return ', '.join([mail.get_email() for mail in self.mails])
#
#     def edit_email(self, mail: Mail, new_mail: Mail) -> str:
#         for el in self.mails:
#             if el.get_email() == mail.get_email():
#                 self.mails.remove(el)
#                 self.mails.append(new_mail)
#                 return f"Email {mail} was changed to {new_mail}"
#
#     def add_adresses(self, adres: Adress):
#         self.adress.append(adres)
#
#     def get_adress(self) -> str:
#         if not self.adress:
#             return 'No adress'
#         return ', '.join([adres.get_adres() for adres in self.adress])
#
#     def edit_adres(self, adres: Adress, new_adres: Adress) -> str:
#         for el in self.adress:
#             if el.get_adres() == adres.get_adres():
#                 self.adress.remove(el)
#                 self.adress.append(new_adres)
#                 return f"Address {adres} was changed to {new_adres}"
#
#
# class AddressBook(UserDict):
#     def __init__(self):
#         super().__init__()
#         self.n = None
#
#     def add_record(self, record: Record) -> None:
#         self.data[record.name.value] = record
#
#     def iterator(self, n=2, days=0):
#         self.n = n
#         index = 1
#         print_block = '-' * 50 + '\n'
#         for record in self.data.values():
#             if days == 0 or (record.birthday.value is not None and record.days_to_birthday(record.birthday) <= days):
#                 print_block += str(record) + '\n'
#                 if index < n:
#                     index += 1
#                 else:
#                     yield print_block
#                     index, print_block = 1, '-' * 50 + '\n'
#         yield print_block


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args):
        try:
            return self.func(*args)
        except IndexError:
            return 'Input formatting is not correct, make sure to check -help-!'
        except KeyError:
            return 'Sorry,user not found, try again!'
        except ValueError:
            return 'Sorry,incorrect argument,try again!'
        except MailExists:
            return "This e-mail already exists in the adress book"
        except AdressExists:
            return 'This adress already exists in the adress book'
        except IncorrectEmailFormat:
            return "Email must contain latin letters, @ and domain after . (Example: 'email@.com)"
        except IncorrectAdressFormat:
            return 'Incorrect adress! May be (Example: Kyiv,Pr.Dnipro,12'
        except PhoneNumberError:
            return "Phone number must be 12 digits, and start with 380"


def greeting(*args):
    return 'Hello! Can I help you?'


@InputError
def add(*args):
    print(args)
    user_name = (args[0])
    phone_ = str(Phone(args[1]))
    try:
        birthday = str(Birthday(args[2]))
    except IndexError:
        birthday = None
    try:
        contact = Contact(
            user_name=user_name,
            birthday=birthday
            )
        session.add(contact)
        session.commit()
        phone = PhoneToContact(
            phone=phone_,
            contact_id=contact.id
            )
        session.add(phone)
        session.commit()
        return f'Add user {user_name}, phone {phone_}, birthday {birthday}'
    except SQLAlchemyError as err:
        print(err)


@InputError
def add_mail(*args):
    _id = int(args[0])
    mail = str(Mail(args[1]))
    try:
        _ = session.query(Contact).filter(Contact.id == _id).one()
        if _.email is not None:
            return f'User with id {_id} already has email'
        else:
            _.email = mail
            session.commit()
            return f'{mail} added to user id {_id}'
    except SQLAlchemyError as err:
        return err


@InputError
def add_adress(*args):
    _id = int(args[0])
    address = str(Adress(args[1]))
    try:
        _ = session.query(Contact).filter(Contact.id == _id).one()
        if _.address is not None:
            return f'User with id {_id} already has address'
        else:
            _.address = address
            session.commit()
            return f'Address {address} added to user id {_id}'
    except SQLAlchemyError as err:
        return err


@InputError
def change_phone(*args):
    _id, old_phone, new_phone = args[0], str(Phone(args[1])), str(Phone(args[2]))
    try:
        contacts_ = session.query(PhoneToContact).filter(PhoneToContact.contact_id == _id).all()
        phone_list = [_.phone for _ in contacts_]
        if old_phone in phone_list:
            for c in contacts_:
                if c.phone == old_phone:
                    c.phone = new_phone
                    session.commit()
                    return f'User with id {_id} phone {old_phone} changed to {new_phone}'
        else:
            return f'Old phone is wrong'
    except SQLAlchemyError as err:
        return err


@InputError
def change_email(*args):
    _id, mail, new_mail = int(args[0]), str(Mail(args[1])), str(Mail(args[2]))
    try:
        _ = session.query(Contact).filter(Contact.id == _id).one()
        if _.email == mail:
            _.email = new_mail
            session.commit()
            return f'Email {mail} for user id {_id} changed to {new_mail}'
        else:
            return f'Old email for user id {_id} is wrong'
    except SQLAlchemyError as err:
        return err


@InputError
def change_adres(*args):
    _id, address, new_address = int(args[0]), str(Mail(args[1])), str(Mail(args[2]))
    try:
        _ = session.query(Contact).filter(Contact.id == _id).one()
        if _.address == address:
            _.email = new_address
            session.commit()
            return f'Address {address} for user id {_id} changed to {new_address}'
        else:
            return f'Old address for user id {_id} is wrong'
    except SQLAlchemyError as err:
        return err


@InputError
def del_contact(*args):
    _id = int(args[0])
    session.query(Contact).filter(Contact.id == _id).delete()
    session.commit()
    return f'Deleted user with id {_id}'


@InputError
def show_all(*args):
    count = 1
    for _ in session.query(Contact).options(joinedload('phones')).all():
        print('_' * 25, f'Sequence number {count}','_' * 25)
        print(f"user_id___: {str(_.id)},\n"
              f"user_name_: {str(_.user_name)},\n"
              f"birthday__: {str(_.birthday)},\n"
              f"email_____: {str(_.email)},\n"
              f"address___: {str(_.address)},\n"
              f"phone(s)__: {[f'{t.phone}' for t in _.phones]}")
        count += 1
    print('-' * 67)
    return 'END'


@InputError
def birthday(*args):
    _id = int(args[0])
    try:
        _ = session.query(Contact).filter(Contact.id == _id).one()
        if _.birthday is None:
            return f'User with id {_id} birthday is unknown '
        else:
            return f'User with id {_id} birthday is at {_.birthday}'
    except SQLAlchemyError as err:
        return err


@InputError
def show_birthday_x_days(*args):
    x = int(args[0])
    contacts = session.query(Contact).all()
    result = f'List of users with birthday in {x} days:'
    for contact in contacts:
        if contact.birthday is not None:
            birthday_date = datetime.strptime(contact.birthday, '%d.%m.%Y').date()
            if days_to_birthday(birthday_date) <= x:
                result += f'\n{contact.user_name}'
    return result


def backing(*args):
    return 'Good bye CommandBot!'


def unknown_command(*args):
    return 'Unknown command! Enter again!'


def help(*args):
    return """Commands format - Command meaning
    Command: "help" - returns a list of available commands with formatting
    Command: "hello" - returns a greeting
    Command: "add" Enter: name phone (birthday) - adds a phone to a contact, adds a birthday (optional)
    Command: "new phone" Enter: name phone new phone - changes a phone number to a new one
    Command: "show all" - displays all contacts
    Command: "birthday" Enter: name - finds a birthday for name
    Command: "soon birthday" Enter: {days} - gives a list of users who have birthday within the next {days}, where days = number of your choosing
    Command: "find" Enter: [any strings} - finds matches in the address book and returns the findings
    Command: "email" Enter: name email - adds an email for a user
    Command: "new email" Enter: name old email new email - changes old email to new email
    Command: "new adress" Enter: name old address new address - changes old address to the new address
    Command: "adress" Enter: name address - adds and address for a user, address format city,street,number
    Command: "remove contact" Enter:  name - deletes the user and all his data from the contact book
    Command: "back" - returns to the selection of work branches
    """


@InputError
def find(*args):
    substring = str(args[0])
    contacts = session.query(Contact).filter(or_(
        Contact.id.like(substring),
        Contact.user_name.ilike(substring),
        Contact.phone.like(substring),
        Contact.birthday.like(substring),
        Contact.email.like(substring),
        Contact.address.like(substring),)).all()
    if contacts:
        for _ in contacts:
            print('_' * 88)
            print('|{:<3}|{:<25}|{:<15}|{:<15}|{:<25}|'.format(str(_.id), str(_.user_name), str(_.phone), str(_.email),
                                                               str(_.address)))
        print('-' * 88)
        return 'The end'
    else:
        return "Nothing find"


COMMANDS = {greeting: ['hello'], add: ['add '], change_phone: ['new phone'],
            show_all: ['show all'], backing: ['back'],
            birthday: ['birthday '], show_birthday_x_days: ['soon birthday'],
            find: ['find', 'check'], add_mail: ['email'], add_adress: ['adress'],
            change_email: ["new email"], change_adres: ['new address', 'new adress'],
            del_contact: ['remove contact'], help: ['help']}


def new_func():
    return str, list


def command_parser(user_command: str) -> new_func():
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []




