
Для роботи з помічником, потрібно запустити main.py
_____________________________________________________________________________
### Description of the bot:
Бот "Cli_assistant" создан для записи,редактирования и удаления\
контактов, а также отдельных заметок. \
Теперь ваше пользование адресной книгой станет ещё проще и продуктивнее.\
Вы не забудете свои действия в адресной книге, ведь\
с помощью заметок можете записывать каждую проделанную\
работу и помечать их ~~тегами~~ ключевыми словами.


### Instructions for start working with the bot:
При запуске бота выберите с какой веткой вы хотите работать\
(подробнее в консольном окне при запуске).\
После выбора ветки своей деятельности введите: **'help'**.\
Далее вам будут доступны все команды для вашей работы.\
Для возвращения на выбор веток своей работы введите: **'back'.**\
Для закрытия бота в меню выбора веток работы введите: **'X'**.
#### **P.s. Не переживайте, вся информация сохраняется автоматически.**

### All bot commands:
#### AdressBook commands:
| Commands       |             Enter              |                                                              Description |
|----------------|:------------------------------:|-------------------------------------------------------------------------:|
| help           |               -                |                                                    Выводит список команд |
| hello          |               -                |                                                    Приветствуется с вами |
| add            |    name, phone, (birthday)     |     создаёт контакта с Телефоном и датой рождения(может быть не введена) |
| new phone      |     name, phone, new phone     |                                           Меняет старый телефон на новый |
| show all       |               -                |                                                  Показывает все контакты |
| delete         |          name, phone           |                                          Удаляет номер телефона контакта |                                                                       
| birthday       |              name              |                                           Выводит дату рождения контакта |                                                                                 
| soon birthday  |      days before birthday      | Показывает контактов, у кого день рождение в течении заданных параметров |
| find           |         any arguments          |              Находит определённых контактов по имени/номеру/почте/адресу |                                            
| email          |          name, email           |                                            Добавляет почту для контактов |                                                                                 
| new email      |   name, old email, new email   |                                             Меняет старую почту на новую |                                                        
| new adress     | name, old address, new address |                                             Меняет старый адрес на новый |                                            
| adress         |         name, address          |          Добавляет адрес для контакта, формат адреса: city,street,number |                                       
| remove contact |              name              |                    Удаляет контакта и все его данные из контактной книги |  
 | back           |               -                |                                          Возвращает в выбор веток работы |
#### Notate commands:
| Commands    |          Enter          |                                                               Description |
|-------------|:-----------------------:|--------------------------------------------------------------------------:|
| help        |            -            |                                                     Выводит список команд |
| hello       |            -            |                                                     Приветствуется с вами |
| add         |          note           |                                         Добавляет заметки в Книгу Заметок |
| tag         | number of note and tags | Добавляет ~~теги~~ ключевые слова для заметок в формате 'tag1, tag2, ...' |
| del         | the number of the note  |                                     Удаляет заметку по порядковому номеру |
| del tag     | the number of the note  |                      Удаляет ~~теги~~ ключевые слова определённой заметки |
| change      | the number of the note  |                                             Изменяет определённую заметку |
| find notate |   text of the notate    |                                    Находит заметку по тексту и выводит её |
| find tag    |  tag(s) of the notate   |                  Находит заметку по ~~тегу~~ ключевому слову и выводит её |
| show        |            -            |                                                     Выводит Книгу Заметок |
| clear       |            -            |                                                     Очищает книгу заметок |
| back        |            -            |                                           Возвращает в выбор веток работы |


