from db import session
from models import Contact, Notate
from faker import Faker

fake = Faker()
a = ['d', 'g', 'd', 'd']
contact = Contact(
            user_name='Oleksandr Romaniuk',
            phone='+380638854917',
            birthday='1992/09/22',
            email='o.romaniuk54@gmail.com',
            address='Vyshgorod'
        )

notate = Notate(
            notate='Сьогодні хороші погода.'
)
session.add(contact)
session.add(notate)
session.commit()

# co = Contact(
#         user_name='sasha',
#         phone='0638854917',
#         birthday='22.09.1992',
#         email='o.romaniuk54@gmail.com',
#         address='vyshgorod'
#     )
# session.add(co)
# session.commit()