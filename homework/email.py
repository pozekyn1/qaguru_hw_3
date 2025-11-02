from datetime import datetime

# 1. Создание словаря email
email = {
    "subject": "  Quarterly Report  ",
    "from": "  Alice.Cooper@Company.ru ",
    "to": "   bob_smith@Gmail.com   ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review"
    " and let me know your feedback.\n\nBest,\nAlice",
}

# 2. Добавление даты отправки
send_date = datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date

# 3. Нормализация e-mail адреса
email["from"] = email["from"].lower().strip()
email["to"] = email["to"].lower().strip()

# 4. Извлечение логина и домена отправителя
login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]

# 5. Создание сокращённой версии текста
email["short_body"] = email["body"][:10] + "..."

# 6. Создание списков личных и корпоративных доменов с неповторяющимися значениями
personal_domains = list(
    {
        "gmail.com",
        "list.ru",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "icloud.com",
        "yandex.ru",
        "mail.ru",
        "list.ru",
        "bk.ru",
        "inbox.ru",
    }
)
corporate_domains = list(
    {
        "company.ru",
        "corporation.com",
        "university.edu",
        "organization.org",
        "company.ru",
        "business.net",
    }
)

# 7. Проверка пересечений в списке личных и корпоративных доменов
has_intersection = bool(set(personal_domains) & set(corporate_domains))

# 8. Проверка «корпоративности» отправителя
is_corporate = domain in corporate_domains

# 9. Сборка «чистого» текста сообщения
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")

# 10. Формирование текста отправленного письма
email["sent_text"] = (
    f"Кому: {email["to"]}, от {email["from"]} Тема: {email["subject"].strip()},"
    f" дата {email["date"]} {email["clean_body"]}"
)

# 11. Рассчёт количества страниц печати
pages = (len(email["sent_text"]) + 499) // 500

# 12. Проверка пустоты темы и тела письма
is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

# 13. Создание «маски» e-mail отправителя
email["masked_from"] = login[:2] + "***@" + domain

# 14. Удаление из списка личных доменов значения "list.ru" и "bk.ru"
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")

# Для быстрой проверки результатов
print(email)
print(has_intersection, is_corporate, pages, is_subject_empty, is_body_empty)
