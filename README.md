

## Маршруты (URLs)

| Страница              | URL                              |
|-----------------------|----------------------------------|
| Главная               | `/`                              |
| Новости               | `/news/`                         |
| Создать новость       | `/news/create/`                  |
| Телефонный справочник | `/phonebook/`                    |
| Редактировать контакт | `/phonebook/edit/`               |
| Шаблоны документов    | `/doc-templates/`                |
| Service Desk          | `/service-desk/`                 |
| Создать заявку        | `/service-desk/create/`          |
| Мои заявки            | `/service-desk/requests/`        |
| Kanban-доска          | `/service-desk/kanban/`          |
| Каталог услуг         | `/service-desk/catalog/`         |
| Редактировать каталог | `/service-desk/catalog/edit/`    |
| Детали заявки         | `/service-desk/ticket/<id>/`     |
| Назначить исполнителя | `/service-desk/assign/<id>/`     |
| Панель администратора | `/portal-admin/`                 |
| Django Admin          | `/admin/`                        |


## Production-режим

Для production установите в `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
SECRET_KEY = 'ваш-секретный-ключ'
```
