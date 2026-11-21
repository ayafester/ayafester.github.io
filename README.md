# Портфолио — Айаана Перелыгина

Статичный сайт: `index.html` + `styles.css`, без сборки. Макет — Figma `ayanka`, фрейм «Screen» (node `1754:11192`).

## Посмотреть локально

```bash
python3 -m http.server 4173
```

и открыть http://localhost:4173

## Деплой

GitHub Pages: сайт живёт в репозитории `ayafester/ayafester.github.io` (ветка `master`) и открывается на https://ayafester.github.io. Исходники дублируются в приватный `ayafester/personal-website`.

Опубликовать правки:

```bash
git push origin main && git push pages main:master
```

Через 1–2 минуты сайт обновится. Когда появится свой домен — добавить файл `CNAME` с доменом и прописать DNS (A-записи GitHub Pages).

## Страницы кейсов

Генерируются скриптом из данных в `tools/build_cases.py` (тексты, факты, порядок). Картинки галерей — `assets/img/cases/<кейс>/g01.jpg…`. После правок:

```bash
python3 tools/build_cases.py
```

Шоурил на карточках главной — `reel.js`, список картинок прямо в разметке карточки в `index.html`.

## Типограф, SEO, OG

- `tools/build_cases.py` в конце прогоняет типограф (`tools/typograph.py`) по главной и кейсам: неразрывные пробелы после предлогов и союзов, перед тире, между числом и словом. Поэтому после ручных правок `index.html` тоже запускайте скрипт.
- Скрипт же пишет `sitemap.xml` и `robots.txt`. Адрес сайта — константа `SITE` в начале скрипта; при подключении домена поменять там и в `<head>` главной.
- OG-картинка главной — `assets/img/og.png`, шаблон `tools/og.html`. Пересобрать:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --force-device-scale-factor=1 --window-size=1200,630 --virtual-time-budget=3000 --screenshot="$PWD/assets/img/og.png" "file://$PWD/tools/og.html"
```

## Что ещё добавить

- ссылка на hh.ru (сейчас `href="#"`, помечена `data-todo`)
- картинки для двух AI-кейсов и Quotocolo (сейчас серые заглушки `.placeholder`) и страницы AI-кейсов
- EN-версия

## Шрифты

- Vela Sans GX — SIL Open Font License 1.1, см. `assets/fonts/OFL-VelaSans.txt`
- Sexsmith — Typodermic / Ray Larabie, на 1001fonts указан как public domain, бесплатный для коммерческого использования
