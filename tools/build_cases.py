#!/usr/bin/env python3
"""Генерирует страницы кейсов cases/<slug>.html из данных ниже.

Запуск из папки site:  python3 tools/build_cases.py
Тексты правим здесь, потом перезапускаем скрипт — HTML пересоберётся.
"""
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASES = [
    dict(
        slug="segmentstream", title="SegmentStream",
        lead="Сайт SaaS-платформы маркетинговой аналитики, который растёт вместе с продуктом.",
        cover="case-segmentstream.jpg",
        facts=[("клиент", "SaaS-платформа маркетинговой аналитики, Великобритания"),
               ("что делала", "Страница сайта и ведение команды"),
               ("команда", "Веб-дизайнер и иллюстратор"),
               ("объём", "10+ страниц, адаптив")],
        task="Продукт вырос, а визуальный стиль за ним не успевал. Нужен был сайт, который легко расширять на новые фичи и решения.",
        role=["Сделала страницу сайта и передала проект веб-дизайнеру",
              "Дальше вела веб-дизайнера и иллюстратора: следила за работой и качеством макетов"],
        done=["Обновили key visual — глубже, премиальнее, увереннее",
              "Собрали дизайн-систему страниц: фичи, решения, цены, кейсы — под все размеры экранов и готовую к разработке",
              "Иллюстратор сделал систему иллюстраций, которая по шагам объясняет атрибуцию и incrementality-тесты"],
        result="Сайт собран как система: новые страницы делаются из готовых шаблонов — командой или AI-агентом.",
        tags=["многостраничный сайт", "тимлид", "дизайн-система"],
    ),
    dict(
        slug="fraxis", title="Fraxis",
        lead="Многостраничный сайт-каталог для производителя кабельных сборок.",
        cover="case-fraxis.jpg",
        facts=[("клиент", "Производство кабельных сборок на заказ"),
               ("что делала", "Структура и дизайн каталога, сборка на Tilda"),
               ("формат", "B2B, многоуровневый каталог"),
               ("платформа", "Tilda + кастомный код")],
        task="У компании широкая линейка продуктов и услуг для разных отраслей. Нужно было показать всё — и при этом не запутать пользователя.",
        role=["Разложила большой каталог в понятную многоуровневую структуру",
              "Спроектировала навигацию для B2B-клиентов",
              "Собрала сайт на Tilda"],
        done=["Сайт-витрина всей продукции и услуг компании",
              "Кастомный код, чтобы выйти за рамки типовых блоков Tilda",
              "Удобная навигация по сложному каталогу"],
        result="По словам директора по маркетингу клиента, после запуска выросло количество заявок и средний чек.",
        tags=["многостраничный сайт", "tilda"],
    ),
    dict(
        slug="brs", title="BRS",
        lead="Минималистичный сайт на Webflow для ремонтной компании из Дубая.",
        cover="case-brs.jpg",
        facts=[("клиент", "Ремонт полного цикла: виллы, квартиры, офисы, Дубай"),
               ("что делала", "Страница сайта и ведение веб-дизайнера"),
               ("платформа", "Webflow + CMS"),
               ("основа", "Обновлённый логотип и айдентика студии")],
        task="Компания обновила визуальный стиль и хотела масштабировать маркетинг. Нужен был простой сайт, которым клиент управляет сам.",
        role=["Сделала страницу сайта и передала проект веб-дизайнеру",
              "Дальше следила за его работой до запуска"],
        done=["Минималистичный сайт в новом стиле бренда",
              "Webflow CMS с несколькими коллекциями — клиент сам обновляет весь контент"],
        result=None,
        tags=["многостраничный сайт", "тимлид", "webflow"],
    ),
    dict(
        slug="vet-workshop", title="vet_workshop",
        lead="Редизайн сайта крупнейшей ветеринарной онлайн-школы.",
        cover="case-vet.jpg",
        facts=[("клиент", "Онлайн-школа для ветеринаров: 7000+ студентов, 17 направлений"),
               ("что делала", "Редизайн главной, каталога и шаблонов курсов"),
               ("потом", "3 года вела веб-дизайнера на поддержке"),
               ("платформа", "Tilda")],
        task="Сделать продукт понятным для пользователей и при этом передать тематику школы.",
        role=["Переделала главную: структура и современный дружелюбный дизайн",
              "Масштабировала визуальную систему на каталоги курсов и шаблоны описаний",
              "Передала проект веб-дизайнеру и три года следила за его работой на поддержке"],
        done=["Новая главная страница",
              "Каталог курсов с фильтром — давняя проблема клиента, которую раньше не мог решить никто",
              "Шаблоны страниц курсов"],
        result="По отзыву соосновательницы школы, задачи сдавались в срок или раньше, а каталог-фильтр собрали за один день.",
        tags=["многостраничный сайт", "тимлид", "tilda"],
    ),
    dict(
        slug="bravestone", title="Bravestone",
        lead="Сайт агентства недвижимости в Португалии.",
        cover="case-bravestone.jpg",
        facts=[("клиент", "Помогает покупать недвижимость в Португалии"),
               ("что делала", "Дизайн сайта"),
               ("платформа", "Webflow"),
               ("основа", "Готовая айдентика студии")],
        task="Передать на сайте премиальный и уверенный образ бренда — для нового поколения инвесторов.",
        role=["Сделала сайт на основе готовой айдентики"],
        done=["Сдержанный премиальный сайт в стиле бренда",
              "Сайт на Webflow"],
        result=None,
        tags=["многостраничный сайт", "webflow"],
    ),
    dict(
        slug="neon-insights", title="Neon Insights",
        lead="Маркетинговый сайт консалтинга по данным и AI.",
        cover="case-neon.jpg",
        facts=[("клиент", "Консалтинг по анализу данных и AI, Нидерланды"),
               ("что делала", "Дизайн сайта и сборка в Webflow"),
               ("платформа", "Webflow"),
               ("основа", "Визуальная система с неоновыми акцентами")],
        task="Сайт, который помогает компании привлекать корпоративных партнёров и клиентов.",
        role=["Сделала дизайн маркетингового сайта",
              "Сама собрала его в Webflow"],
        done=["Чистый стиль с неоновыми элементами — про современные инструменты и простые решения",
              "Сайт на Webflow"],
        result=None,
        tags=["сайт", "webflow"],
    ),
    dict(
        slug="joompro", title="ДжумПро",
        lead="Новый маркетинговый сайт сервиса закупки и доставки товаров из Китая.",
        cover="case-joompro.jpg",
        facts=[("клиент", "Логистический сервис команды маркетплейса Joom"),
               ("что делала", "Редизайн сайта"),
               ("платформа", "Tilda + CMS «Потоки»"),
               ("основа", "Брендбук ДжумПро")],
        task="Развить существующий брендбук и разложить много информации так, чтобы её было легко читать.",
        role=["Перестроила сайт на блочную систему",
              "Добавила CMS, чтобы команда сама публиковала кейсы и статьи"],
        done=["Блочная система, которая структурирует информацию",
              "Яркие иллюстрации, которые передают смысл",
              "Настроенные «Потоки» — встроенная CMS Tilda"],
        result=None,
        tags=["редизайн", "tilda"],
    ),
]

GALLERY_DIR = {"segmentstream": "segmentstream", "fraxis": "fraxis", "brs": "brs",
               "vet-workshop": "vet", "bravestone": "bravestone",
               "neon-insights": "neon", "joompro": "joompro"}


def gallery(slug):
    d = os.path.join(ROOT, "assets/img/cases", GALLERY_DIR[slug])
    return [f"/assets/img/cases/{GALLERY_DIR[slug]}/{f}" for f in sorted(os.listdir(d)) if f.endswith(".jpg")]


MENU = """  <aside class="menu">
    <div class="menu__top">
      <a href="/"><img class="menu__avatar" src="/assets/img/avatar-menu.png" width="40" height="40" alt="На главную"></a>
      <p class="menu__name">Перелыгина Айаана<br><span>Lead Web Designer</span></p>
      <nav class="menu__nav" aria-label="Разделы">
        <a class="pill" href="/#portfolio">портфолио</a>
        <a class="pill" href="/#ai">ai-проекты</a>
        <a class="pill" href="/#experience">опыт</a>
      </nav>
    </div>
    <div class="menu__bottom">
      <p class="menu__meta">Якутск<br>удалённо или релокация</p>
      <a class="btn btn--outline" href="/cv.pdf" download>скачать cv</a>
      <a class="btn btn--dark" href="https://t.me/ayafester" target="_blank" rel="noopener">написать мне в telegram</a>
    </div>
  </aside>"""

FOOTER = """    <section class="col footer">
      <ul class="links">
        <li><a href="https://t.me/ayafester" target="_blank" rel="noopener">Telegram</a></li>
        <li><a href="#" data-todo="linkedin">LinkedIn</a></li>
        <li><a href="#" data-todo="hh">hh.ru</a></li>
        <li><a href="mailto:ayanka_m@mail.ru">почта</a></li>
        <li><a class="muted" href="https://www.instagram.com/ayafester/" target="_blank" rel="noopener">Instagram</a></li>
      </ul>
    </section>

    <figure class="photo">
      <img src="/assets/img/yakutia.jpg" alt="Якутия, Булуус: наледь и вода среди камней" loading="lazy">
      <figcaption class="display">Якутия, Булуус</figcaption>
    </figure>"""


def ul(items):
    return "\n".join(f"          <li>{escape(i)}</li>" for i in items)


def page(c, nxt):
    e = escape
    facts = "\n".join(f'        <div><dt class="label">{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in c["facts"])
    shots = "\n".join(f'      <img src="{src}" alt="{e(c["title"])} — экран {i}" loading="lazy">'
                      for i, src in enumerate(gallery(c["slug"]), 1))
    result = ""
    if c["result"]:
        result = f"""
    <section class="col story">
      <div class="story__item">
        <p class="label">результат</p>
        <p class="story__lead">{e(c["result"])}</p>
      </div>
    </section>
"""
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(c["title"])} — кейс · Перелыгина Айаана</title>
  <meta name="description" content="{e(c["lead"])}">
  <meta property="og:image" content="/assets/img/{c["cover"]}">
  <link rel="icon" href="/assets/img/avatar-menu.png">
  <link rel="preload" href="/assets/fonts/VelaSans-GX.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="preload" href="/assets/fonts/Sexsmith.otf" as="font" type="font/otf" crossorigin>
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
<!-- Сгенерировано tools/build_cases.py — правьте тексты там -->

{MENU}

  <main class="page">

    <section class="col case-hero">
      <a class="back" href="/#portfolio">← все кейсы</a>
      <h1 class="display case-hero__title">{e(c["title"])}</h1>
      <p class="story__lead">{e(c["lead"])}</p>
      <ul class="tags">{"".join(f"<li>{e(t)}</li>" for t in c["tags"])}</ul>
      <dl class="facts">
{facts}
      </dl>
    </section>

    <img class="case__img" src="/assets/img/{c["cover"]}" alt="{e(c["title"])} — обложка">

    <section class="col story">
      <div class="story__item">
        <p class="label">задача</p>
        <p class="story__lead">{e(c["task"])}</p>
      </div>
      <div class="story__item">
        <p class="label">моя роль</p>
        <ul class="story__list">
{ul(c["role"])}
        </ul>
      </div>
      <div class="story__item">
        <p class="label">что сделали</p>
        <ul class="story__list">
{ul(c["done"])}
        </ul>
      </div>
    </section>

    <div class="shots">
{shots}
    </div>
{result}
    <section class="col next">
      <p class="label">следующий кейс</p>
      <a class="display next__link" href="/cases/{nxt["slug"]}.html">{e(nxt["title"])} →</a>
    </section>

{FOOTER}

  </main>

  <script src="/menu.js"></script>
</body>
</html>
"""


def main():
    os.makedirs(os.path.join(ROOT, "cases"), exist_ok=True)
    for i, c in enumerate(CASES):
        nxt = CASES[(i + 1) % len(CASES)]
        with open(os.path.join(ROOT, "cases", c["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(page(c, nxt))
        print("cases/%s.html  (%d картинок)" % (c["slug"], len(gallery(c["slug"]))))


if __name__ == "__main__":
    main()
