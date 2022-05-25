
## 목차

- [프로젝트 개요](#프로젝트-개요)
- [요구사항 분석](#요구사항-분석)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [DB Diagram](#db-diagram)
    - [DB Schema](#db-schema)
- [API Document](#api-document)

<br>

## 프로젝트 개요
- 주어진 데이터 셋을 사용하여 DB 모델링 및 설계를 하고 REST API Server를 개발

<br>

## 요구사항 분석
- 주어진 데이터 셋을 분석하여 관계형 데이터베이스 설계
    - [x] 주어진 데이터 csv를 RDB에 적재
    - [x] 필요시 추가적인 모델 정의 

- REST API 개발
    - [x] 회사명 자동 완성 검색
        - [x] 일부 정보만으로 검색 가능
    - [x] 회사 이름으로 회사 검색
    - [x] 새로운 회사 등록

- 추가 기능 정의
    - [x] 모든 회사 정보 조회
        - [x] Django 내장 Pagination 적용

<br>

## Project Structure
```bash
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── company
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── test_app.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── db_uploader.py
├── manage.py
├── my_settings.py
├── wanted_lab
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── wanted_temp_data.csv

3 directories, 22 files
```

<br>

## Tech Stack

<img src="https://img.shields.io/badge/python-3.9.12-green">  <img src="https://img.shields.io/badge/Django-4.0.4-red">   <img src="https://img.shields.io/badge/djangorestframework-3.13.1-blu">   <img src="https://img.shields.io/badge/PyMySql-1.0.2-blue">

<br>

## DB Diagram
![Wanted-Lab](https://user-images.githubusercontent.com/55699007/170201140-ddc7ce5b-94ab-4b5e-b503-65e0aba5497b.png)

<br>

### DB Schema
- `company table`
    ```
    mysql> desc company;
    +-------+--------+------+-----+---------+----------------+
    | Field | Type   | Null | Key | Default | Extra          |
    +-------+--------+------+-----+---------+----------------+
    | id    | bigint | NO   | PRI | NULL    | auto_increment |
    +-------+--------+------+-----+---------+----------------+
    1 row in set (0.00 sec)
    ```

<br>

- `language table`
    ```
    mysql> desc language;
    +--------+------------+------+-----+---------+----------------+
    | Field  | Type       | Null | Key | Default | Extra          |
    +--------+------------+------+-----+---------+----------------+
    | id     | bigint     | NO   | PRI | NULL    | auto_increment |
    | code   | varchar(2) | NO   | UNI | NULL    |                |
    | in_use | tinyint(1) | NO   |     | NULL    |                |
    +--------+------------+------+-----+---------+----------------+
    3 rows in set (0.00 sec)
    ```
    - PK : 언어 고유 Id
    - code : 언어 값
    - in_use : 사용 여부

<br>

- `company_name table`
    ```
    mysql> desc company_name;
    +------------+--------------+------+-----+---------+----------------+
    | Field      | Type         | Null | Key | Default | Extra          |
    +------------+--------------+------+-----+---------+----------------+
    | id         | bigint       | NO   | PRI | NULL    | auto_increment |
    | name       | varchar(100) | YES  |     | NULL    |                |
    | code_id    | bigint       | NO   | MUL | NULL    |                |
    | company_id | bigint       | YES  | MUL | NULL    |                |
    | tags       | json         | YES  |     | NULL    |                |
    +------------+--------------+------+-----+---------+----------------+
    5 rows in set (0.00 sec)
    ```
    - name : 회사 이름
    - code_id : 회사 이름에 대한 언어 code
    - company_id : 회사 고유 Id
    - tags : 회사 tag list

<br>

## API Document
- 회사명 자동 완성 검색
    - `GET` `api/v1/companies/search/?query=링크`
    - `Request Body`
        ```json
        None
        ```
    - `Requert Header`
        ```json
        { "x-wanted-language" : "ko" }
        ```
    - `Server Response`
        ```json
        [
            { "company_name": "주식회사 링크드코리아" },
            { "company_name": "스피링크" }
        ]
        ```

- 회사 이름으로 회사 검색
    - `GET` `api/v1/companies/<str:name>/`
    - `Request Body`
        ```json
        None
        ```
    - `Requert Header`
        ```json
        { "x-wanted-language" : "ko" }
        ```
    - `Server Response`
        ```json
        {
            "company_name": "원티드랩",
            "tags": [
                "태그_4",
                "태그_20",
                "태그_16"
            ]
        }
        ```

- 새로운 회사 등록
    - `POST` `api/v1/companies/`

- 모든 회사 정보 조회
    - `GET` `api/v1/companies/`

