## Создание docker-контейнера проекта. </br> [django+gunicorn] + [postgres] + [nginx]
1. Должен быть установлен и запущен Docker_compose или Docker_desktop.
2. В терминале в папке проекта выполните сборку образов и запуск контейнеров: </br>
```docker compose up -d --build```
3. После запуска контейнера осталось выполнить миграции для БД: </br>
``` docker-compose exec web python manage.py migrate ```
4. Всё готово. Проверка работы приложения(контейнеров):  http://localhost/api/v1/
5. Дополнительные команды для работы с docker compose и dockerhub:
```
docker compose stop  # Остановить запущенный контейнер
docker compose start  # Запустить остановленный контейнер
docker compose down  # Остановить и удалить запущенный контейнер
docker compose down -v  # Останов и удаление контейнера и его образов
docker compose up -d  # Сборка и запуск контейнера
docker compose up -d --build  # Запуск контейнеров с обязательной сборкой образов
docker exec -it stocks_products-nginx-1  /bin/bash  # Зайти под root в структуру образа nginx (выход exit)
docker images  # Просмотр всех образов
# DockerHub
docker tag my_local_image_name <my_login>/<my_repo_name>:<my_image_tag_name_in_my_repo>  # Создать тэг перед загрузкой образа 
docker push <my_login>/<my_repo_name>:<my_image_tag_name_in_my_repo>  # Загрузка образа на dockerhub
docker pull <user_name>/<repo_name>:<tag_image_name>  # Выгрузка образа с dockerhub
docker pull konsttt/repo1:stocks_products  # Выгрузка с dockerhub образа django-gunicorn
docker pull konsttt/repo1:postgresdb # Выгрузка с dockerhub образа с базой данных postgres
docker pull konsttt/repo1:configured_nginx  # Выгрузка с dockergub образа с настроенным nginx
docker run <user_name>/<repo_name>:<tag_image_name> # Образ можно сразу же скачать и запустить
```
6. Для загрузки образов проекта stocks_products с dockerhub, при запущенном Docker Desktop, </br>
выполнить следующие команды:
```
docker run konsttt/repo1:postgresdb
docker run konsttt/repo1:stocks_products
docker run konsttt/repo1:configured_nginx
```

######################################################################################################################

# Склады и товары

## Техническая задача: реализовать CRUD-логику для продуктов и складов, используя Django Rest Framework.

**CRUD** – аббревиатура для Create-Read-Update-Delete. Ей обозначают логику для операций создания-чтения-обновления-удаления сущностей. Подробнее: https://ru.wikipedia.org/wiki/CRUD

## Описание

У нас есть продукты, которыми торгует компания. Продукты описываются названием и необязательным описанием (см. `models.py`). Также компания имеет ряд складов, на которых эти продукты хранятся. У продукта на складе есть стоимость хранения, поэтому один и тот же продукт может иметь разные стоимости на разных складах.

Необходимо реализовать REST API для создания/получения/обновления/удаления продуктов и складов. Так как склады имеют информацию о своих продуктах (через связанную таблицу) - необходимо переопределить методы создания и обновления объектов в сериализаторе (см. `serializers.py`).

Помимо CRUD-операций необходимо реализовать поиск продуктов по названиям и описанию. И поиск складов, в которых есть определенный продукт (по идентификатору). Подробности в файле `requests-examples.http`.

Так как продуктов и складов может быть много, то необходимо реализовать пагинацию для вывода списков.

Рекомендуется обратить внимание на реализацию файлов `urls.py` (менять их не надо, просто обратить внимание и осознать).

## Подсказки

1. Вам необходимо будет задать логику во views и serializers. В места, где нужно добавлять код, включены комментарии. После того как вы добавите код, комментарии можно удалить.

2. Для обновления объектов удобно использовать метод `update_or_create`: https://docs.djangoproject.com/en/3.2/ref/models/querysets/#update-or-create

## Дополнительное задание

### Поиск складов с продуктами

Реализуйте поиск складов, в которых есть определенный продукт, но при этом указывать хочется не идентификатор продукта, а название (или его часть) или часть описания.

Пример запроса:

```
# поиск складов, где есть определенный продукт
GET {{baseUrl}}/stocks/?search=помид
Content-Type: application/json
```

## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Вам необходимо будет создать базу в postgres и прогнать миграции:

```base
manage.py migrate
```

Выполнить команду:

```bash
python manage.py runserver
```
