# Портфолио — Айаана Перелыгина

Статичный сайт: `index.html` + `styles.css`, без сборки. Макет — Figma `ayanka`, фрейм «Screen» (node `1754:11192`).

## Посмотреть локально

```bash
python3 -m http.server 4173
```

и открыть http://localhost:4173

## Деплой

Cloudflare Pages, подключённый к этому репозиторию на GitHub:
- Framework preset: **None**
- Build command: *(пусто)*
- Build output directory: `/`

Каждый пуш в `main` публикуется автоматически.

## Страницы кейсов

Генерируются скриптом из данных в `tools/build_cases.py` (тексты, факты, порядок). Картинки галерей — `assets/img/cases/<кейс>/g01.jpg…`. После правок:

```bash
python3 tools/build_cases.py
```

Шоурил на карточках главной — `reel.js`, список картинок прямо в разметке карточки в `index.html`.

## Что ещё добавить

- `cv.pdf` — резюме, на него ведёт кнопка «скачать cv»
- ссылки на LinkedIn и hh.ru (сейчас `href="#"`, помечены `data-todo`)
- картинки для двух AI-кейсов и Quotocolo (сейчас серые заглушки `.placeholder`) и страницы AI-кейсов
- EN-версия

## Шрифты

- Vela Sans GX — SIL Open Font License 1.1, см. `assets/fonts/OFL-VelaSans.txt`
- Sexsmith — Typodermic / Ray Larabie, на 1001fonts указан как public domain, бесплатный для коммерческого использования
