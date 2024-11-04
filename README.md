# LOGOSBOOK
Book-reading app with AI features

# Installation

P. S. Чтобы просмотреть доп. задание нужно в запущенном приложении зайти в чат, выбрать степень сокращения и отправить свой тест

## Stack
Python, NodeJS, VueJS

## Clone repo
`git clone --recurse-submodules https://github.com/NightyStudios/Logosbook_Back`

## Install necessary libraries
`pip install -r requirements.txt`

## Setup model
Download and unzip archive from `https://drive.google.com/file/d/1Zvc7CdEC6u3kogj2PxPo7Qz9NNZL6PJn/view`

## Run BackEnd
`uvicorn main:app --reload`

## Setup FrontEnd

```bash
cd Logosbook_Front
npm install
```
## Run FrontEnd
`npm run dev`

## Enjoy!


## Описание файлов 
- /model.py - скрипт-адаптер модели для сжатия текста
- /model - веса модели и токенизатора
- /requirements.txt - список библиотек к установке
- /main.py - BackEnd сайта
- /SiteZv - FrontEnd сайта

## Описание решение
Изначально, мы собрали 3 тыс. кратких содержаний с брифли, а так же найдя их оригиналы на lib.ru. В попытках дообучать модель mt5-small на данном датасете, оказалось очень неэфективным решениям, из-за достаточно маленького датасета. К сожалению в попытках использования уже готовых датасетов из huggingface (200 тыс. объём текстов), мы столкнулись со второй проблемой - нехватка вычеслительных мощностей (предварительно 1 эпоха нам обходилась бы 4-мью сутками. А желательно хотя бы 3 эпохи). Поэтому мы использовали уже готовую модель с [huggingface](https://huggingface.co/cointegrated/rut5-base-absum), под которой стоит модель mt5-base, и на трех датасет суммарным объёмом в 300 тыс. текстов. 
