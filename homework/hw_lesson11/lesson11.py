def calculate_total(price, tax_percent):
    if price < 0 or tax_percent > 20:
        return 'Ошибка'
    return price * (tax_percent/100 + 1)


def get_level(points):
    if points >= 100:
        return "Эксперт"
    if points >= 50:
        return "Продвинутый"
    if points >= 20:
        return "Начинающий"
    return "Новичок"


def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"
