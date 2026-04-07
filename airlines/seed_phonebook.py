from django.core.management.base import BaseCommand
from portal.models import Employee

EMPLOYEES = [
    dict(full_name="Александров Иван Петрович",   position="Генеральный директор",    department="exec",    phone="10-01", email="ceo@technogroup.ru",         floor="4", office="401", initials="АП", laboratory=""),
    dict(full_name="Лебедев Александр Николаевич", position="Зам. генерального директора", department="exec", phone="10-02", email="deputy@technogroup.ru",    floor="4", office="401", initials="ЛА", laboratory=""),
    dict(full_name="Базанов Дмитрий Сергеевич",   position="IT-директор",             department="it",      phone="20-99", email="it@technogroup.ru",          floor="3", office="305", initials="БД", laboratory=""),
    dict(full_name="Егоров Алексей Игоревич",      position="Системный администратор", department="it",      phone="21-00", email="sysadmin@technogroup.ru",    floor="3", office="307", initials="ЕА", laboratory=""),
    dict(full_name="Жуков Павел Андреевич",        position="Разработчик",             department="it",      phone="21-05", email="dev@technogroup.ru",         floor="3", office="308", initials="ЖП", laboratory=""),
    dict(full_name="Морозов Кирилл Дмитриевич",    position="DevOps-инженер",          department="it",      phone="21-10", email="devops@technogroup.ru",      floor="3", office="309", initials="МК", laboratory=""),
    dict(full_name="Николаева Юлия Сергеевна",     position="HR-директор",             department="hr",      phone="10-51", email="hr-director@technogroup.ru", floor="2", office="209", initials="НЮ", laboratory=""),
    dict(full_name="Васильева Елена Андреевна",     position="HR-менеджер",             department="hr",      phone="10-50", email="hr@technogroup.ru",          floor="2", office="210", initials="ВЕ", laboratory=""),
    dict(full_name="Зайцева Наталья Игоревна",      position="Рекрутер",                department="hr",      phone="10-52", email="recruit@technogroup.ru",     floor="2", office="211", initials="ЗН", laboratory=""),
    dict(full_name="Григорьев Михаил Олегович",    position="Финансовый директор",     department="finance", phone="10-75", email="finance@technogroup.ru",     floor="4", office="402", initials="ГМ", laboratory=""),
    dict(full_name="Иванов Сергей Владимирович",   position="Бухгалтер",               department="finance", phone="10-77", email="accounting@technogroup.ru",  floor="4", office="403", initials="ИС", laboratory=""),
    dict(full_name="Орлов Дмитрий Петрович",       position="Финансовый аналитик",     department="finance", phone="10-78", email="analyst@technogroup.ru",     floor="4", office="404", initials="ОД", laboratory=""),
    dict(full_name="Дмитриева Ольга Викторовна",   position="Маркетолог",              department="marketing", phone="10-88", email="marketing@technogroup.ru", floor="2", office="215", initials="ДО", laboratory=""),
    dict(full_name="Козлова Анна Михайловна",       position="SMM-менеджер",            department="marketing", phone="10-90", email="smm@technogroup.ru",      floor="2", office="216", initials="КА", laboratory=""),
]

class Command(BaseCommand):
    help = 'Заполняет телефонный справочник начальными данными'

    def handle(self, *args, **options):
        if Employee.objects.exists():
            self.stdout.write('Справочник уже содержит данные, пропускаем.')
            return
        for data in EMPLOYEES:
            Employee.objects.create(**data)
        self.stdout.write(self.style.SUCCESS(f'Создано {len(EMPLOYEES)} сотрудников'))
