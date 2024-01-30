# Фреймворк Django
## Урок 1. Введение в Django
### Задание
> 1. Создайте пару представлений в вашем первом приложении:
> - главная
> - о себе.
> 2. Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.
> 3. Сохраняйте в логи данные о посещении страниц.

## Урок 2. Работа с моделями
### Задание
> **Создайте три модели Django: клиент, товар и заказ.**
> 1. Поля модели «Клиент»:
> - имя клиента
> - электронная почта клиента
> - номер телефона клиента
> - адрес клиента
> - дата регистрации клиента
> 2. Поля модели «Товар»:
> - название товара
> - описание товара
> - цена товара
> - количество товара
> - дата добавления товара
> 3. Поля модели «Заказ»:
> - связь с моделью «Клиент», указывает на клиента, сделавшего заказ
> - связь с моделью «Товар», указывает на товары, входящие в заказ
> - общая сумма заказа
> - дата оформления заказа
> 4. Допишите несколько функций CRUD для работы с моделями по желанию. 

## Урок 3. Работа с представлениями и шаблонами
### Задание
> 1. Создайте шаблон для вывода всех заказов клиента и
списком товаров внутри каждого заказа.
Подготовьте необходимый маршрут и представление.
> 
> 
> 2. Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
> - за последние 7 дней (неделю)
> - за последние 30 дней (месяц)
> - за последние 365 дней (год)
> - Товары в списке не должны повторятся.

## Урок 4. Работа с формами
### Задание
> 1. Создайте форму для редактирования товаров в базе
данных.
> 2. Измените модель продукта, добавьте поле для хранения
фотографии продукта.
> 3. Создайте форму, которая позволит сохранять фото.

## Урок 5. Работа с административной панелью
### Задание
> - Настройте под свои нужды вывод информации о клиентах, товарах и заказах на страницах вывода информации об объекте и вывода списка объектов.