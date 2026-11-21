#!/usr/bin/env python3
"""Собирает сайт на двух языках из данных ниже.

Запуск из папки site:  python3 tools/build_cases.py

Что делает:
- cases/<slug>.html (RU) и en/cases/<slug>.html (EN) — страницы кейсов из CASES;
- в index.html (RU) обновляет меню, шоурилы, футер, галерею фото и прогоняет типограф;
- en/index.html собирает из index.html, заменяя тексты по словарю INDEX_EN;
- пишет sitemap.xml, robots.txt, llms.txt.

Главную на русском правим руками в index.html, английские тексты главной — в INDEX_EN,
тексты кейсов — здесь в CASES (поле en — английская версия).
"""
import json
import os
import re
import sys
from html import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from typograph import typo_html  # noqa: E402

SHOW_AI = False  # блок AI-проектов: True — показать на главной и в меню
SITE = "https://ayafester.github.io"  # при подключении домена поменять здесь и в <head> index.html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LINKEDIN = "https://www.linkedin.com/in/ayafester/"
TELEGRAM = "https://t.me/ayafester"
INSTAGRAM = "https://www.instagram.com/ayaoftheshire/"
EMAIL = "ayafester@gmail.com"

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
        done=["Обновили key visual: глубже, премиальнее, увереннее",
              "Собрали адаптивную дизайн-систему страниц — фичи, решения, цены, кейсы, — готовую к разработке",
              "Иллюстратор сделал систему иллюстраций, которая по шагам объясняет атрибуцию и incrementality-тесты"],
        result="Сайт собран как система: новые страницы делаются из готовых шаблонов — командой или AI-агентом.",
        tags=["многостраничный сайт", "тимлид", "дизайн-система"],
        en=dict(
            lead="A website for a marketing analytics SaaS platform that grows with the product.",
            facts=[("client", "Marketing analytics SaaS platform, UK"),
                   ("my part", "One page of the website, then leading the team"),
                   ("team", "Web designer and illustrator"),
                   ("scope", "10+ pages, responsive")],
            task="The product had grown, and the visual style hadn't kept up. The company needed a website that is easy to extend with new features and solutions.",
            role=["Designed one page of the website and handed the project over to a web designer",
                  "Then led the web designer and the illustrator: reviewed their work and the quality of the layouts"],
            done=["Updated the key visual: deeper, more premium, more confident",
                  "Built a responsive design system of pages — features, solutions, pricing, case studies — ready for development",
                  "The illustrator created an illustration system that explains attribution and incrementality tests step by step"],
            result="The website is built as a system: new pages are assembled from ready-made templates — by the team or by an AI agent.",
            tags=["multi-page website", "team lead", "design system"],
        ),
    ),
    dict(
        slug="fraxis", title="Fraxis",
        lead="Многостраничный сайт-каталог для производителя кабельных сборок.",
        cover="case-fraxis.jpg",
        facts=[("клиент", "Производство кабельных сборок на заказ"),
               ("что делала", "Структура, дизайн и сборка сайта-каталога"),
               ("формат", "B2B, многоуровневый каталог"),
               ("платформа", "Tilda + кастомный код")],
        task="У компании широкая линейка продуктов и услуг для разных отраслей, собственное производство и контрактная разработка. Нужен был сайт-витрина, который показывает всё и при этом остаётся понятным.",
        role=["Разработала многоуровневый сайт-каталог на Tilda",
              "Разложила продукцию и услуги в понятную структуру с удобной навигацией",
              "С помощью кода вышла за рамки типовых блоков платформы и собрала сложный B2B-сайт"],
        done_label="что сделала",
        done=["Сайт-витрина всей продукции и услуг компании",
              "Кастомный код вместо ограничений стандартных блоков Tilda",
              "Навигация, в которой не теряешься даже в большом каталоге"],
        result="По словам директора по маркетингу клиента, после запуска выросло количество заявок и средний чек.",
        tags=["многостраничный сайт", "tilda"],
        en=dict(
            lead="A multi-page catalog website for a cable assembly manufacturer.",
            facts=[("client", "Custom cable assembly manufacturer"),
                   ("my part", "Structure, design and build of the catalog website"),
                   ("format", "B2B, multi-level catalog"),
                   ("platform", "Tilda + custom code")],
            task="The company has a wide range of products and services for different industries, its own production and contract development. It needed a showcase website that presents everything and still stays clear.",
            role=["Built a multi-level catalog website on Tilda",
                  "Organised products and services into a clear structure with easy navigation",
                  "Used custom code to go beyond the platform's standard blocks and build a complex B2B website"],
            done=["A showcase of all the company's products and services",
                  "Custom code instead of the limits of standard Tilda blocks",
                  "Navigation that keeps you oriented even in a large catalog"],
            result="According to the client's marketing director, the number of leads and the average order value grew after launch.",
            tags=["multi-page website", "tilda"],
        ),
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
        en=dict(
            lead="A minimalist Webflow website for a Dubai renovation company.",
            facts=[("client", "Full-cycle renovation: villas, apartments, offices, Dubai"),
                   ("my part", "One page of the website, then leading a web designer"),
                   ("platform", "Webflow + CMS"),
                   ("based on", "The studio's updated logo and identity")],
            task="The company had updated its visual style and wanted to scale its marketing. It needed a simple website the client can manage on their own.",
            role=["Designed one page of the website and handed the project over to a web designer",
                  "Then oversaw his work until launch"],
            done=["A minimalist website in the new brand style",
                  "Webflow CMS with several collections — the client updates all the content themselves"],
            result=None,
            tags=["multi-page website", "team lead", "webflow"],
        ),
    ),
    dict(
        slug="vet-workshop", title="vet_workshop",
        lead="Новая айдентика и редизайн сайта крупнейшей ветеринарной онлайн-школы.",
        cover="case-vet.jpg",
        facts=[("клиент", "Онлайн-школа для ветеринаров: 7 000+ студентов, 17 направлений"),
               ("что делала", "Новая айдентика, редизайн главной, каталога и шаблонов курсов"),
               ("потом", "3 года вела веб-дизайнера на поддержке"),
               ("платформа", "Tilda")],
        task="Сделать продукт понятным для пользователей и при этом передать тематику школы.",
        role=["Сделала новую айдентику школы",
              "Переделала главную: структура и современный дружелюбный дизайн",
              "Масштабировала визуальную систему на каталоги курсов и шаблоны описаний",
              "Передала проект веб-дизайнеру и три года следила за его работой на поддержке"],
        done_label="что сделала",
        done=["Новая айдентика",
              "Новая главная страница",
              "Каталог курсов с фильтром — давняя задача клиента, которую раньше никто не мог решить",
              "Шаблоны страниц курсов"],
        result="По отзыву соосновательницы школы, задачи сдавались в срок или раньше, а каталог-фильтр собрали за один день.",
        tags=["айдентика", "многостраничный сайт", "тимлид", "tilda"],
        en=dict(
            lead="A new identity and website redesign for the largest online school for veterinarians.",
            facts=[("client", "Online school for veterinarians: 7,000+ students, 17 programs"),
                   ("my part", "New identity, redesign of the home page, catalog and course templates"),
                   ("after that", "Led a web designer on support for 3 years"),
                   ("platform", "Tilda")],
            task="Make the product clear for users while conveying what the school is about.",
            role=["Created a new identity for the school",
                  "Redesigned the home page: structure and a modern, friendly design",
                  "Scaled the visual system to course catalogs and description templates",
                  "Handed the project over to a web designer and oversaw his work on support for three years"],
            done=["New identity",
                  "New home page",
                  "Course catalog with a filter — a long-standing task nobody had been able to solve before",
                  "Course page templates"],
            result="According to the school's co-founder, tasks were delivered on time or early, and the catalog filter was built in one day.",
            tags=["identity", "multi-page website", "team lead", "tilda"],
        ),
    ),
    dict(
        slug="bravestone", title="Bravestone",
        lead="Сайт агентства недвижимости в Португалии.",
        cover="case-bravestone.jpg",
        facts=[("клиент", "Помогает покупать недвижимость в Португалии"),
               ("что делала", "Дизайн сайта"),
               ("платформа", "Webflow"),
               ("основа", "Готовая айдентика студии")],
        task="Передать на сайте премиальный и уверенный образ бренда для нового поколения инвесторов.",
        role=["Сделала сайт на основе готовой айдентики"],
        done_label="что сделала",
        done=["Сдержанный премиальный сайт в стиле бренда",
              "Сайт на Webflow"],
        result=None,
        tags=["многостраничный сайт", "webflow"],
        en=dict(
            lead="A website for a real estate agency in Portugal.",
            facts=[("client", "Helps people buy property in Portugal"),
                   ("my part", "Website design"),
                   ("platform", "Webflow"),
                   ("based on", "The studio's existing identity")],
            task="Convey a premium, confident brand image on the website for a new generation of investors.",
            role=["Designed the website based on the existing identity"],
            done=["A restrained, premium website in the brand style",
                  "Website on Webflow"],
            result=None,
            tags=["multi-page website", "webflow"],
        ),
    ),
    dict(
        slug="neon-insights", title="Neon Insights",
        lead="Айдентика с нуля и маркетинговый сайт консалтинга по данным и AI.",
        cover="case-neon.jpg",
        facts=[("клиент", "Консалтинг по анализу данных и AI, Нидерланды"),
               ("что делала", "Айдентика с нуля, дизайн сайта и сборка в Webflow"),
               ("платформа", "Webflow"),
               ("стиль", "Чистый, с неоновыми акцентами")],
        task="С нуля создать айдентику и сайт, которые помогут компании привлекать корпоративных партнёров и клиентов.",
        role=["Сделала айдентику с нуля",
              "Сделала дизайн маркетингового сайта",
              "Сама собрала его в Webflow"],
        done_label="что сделала",
        done=["Компактная визуальная система: чистый стиль с неоновыми элементами, который говорит о современных инструментах и простых решениях",
              "Маркетинговый сайт на Webflow",
              "Обложки для соцсетей в том же стиле"],
        result=None,
        tags=["айдентика", "сайт", "webflow"],
        en=dict(
            lead="An identity from scratch and a marketing website for a data and AI consultancy.",
            facts=[("client", "Data analytics and AI consultancy, Netherlands"),
                   ("my part", "Identity from scratch, website design and Webflow build"),
                   ("platform", "Webflow"),
                   ("style", "Clean, with neon accents")],
            task="Create an identity and a website from scratch that help the company attract corporate partners and clients.",
            role=["Created the identity from scratch",
                  "Designed the marketing website",
                  "Built it myself in Webflow"],
            done=["A compact visual system: a clean style with neon elements that speaks of modern tools and simple solutions",
                  "Marketing website on Webflow",
                  "Social media covers in the same style"],
            result=None,
            tags=["identity", "website", "webflow"],
        ),
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
        role=["Сделала дизайн сайта, который продолжает и развивает брендбук ДжумПро",
              "Придумала блочную систему, которая структурирует информацию",
              "Сделала яркие иллюстрации, которые передают смысл",
              "Кастомизировала «Потоки» — CMS Tilda, — чтобы команда сама публиковала кейсы и статьи"],
        done_label="что сделала",
        done=["Новый маркетинговый сайт на Tilda",
              "Блочная система и иллюстрации",
              "CMS для кейсов и статей"],
        result=None,
        tags=["редизайн", "tilda"],
        en=dict(
            title="JoomPro",
            lead="A new marketing website for a service that sources and delivers goods from China.",
            facts=[("client", "Logistics service by the Joom marketplace team"),
                   ("my part", "Website redesign"),
                   ("platform", "Tilda + Streams CMS"),
                   ("based on", "JoomPro brand book")],
            task="Develop the existing brand book and organise a lot of information so that it's easy to read.",
            role=["Designed a website that continues and develops the JoomPro brand book",
                  "Came up with a block system that structures the information",
                  "Made bright illustrations that convey the meaning",
                  "Customised Streams, Tilda's CMS, so the team can publish case studies and articles on their own"],
            done=["New marketing website on Tilda",
                  "Block system and illustrations",
                  "CMS for case studies and articles"],
            result=None,
            tags=["redesign", "tilda"],
        ),
    ),
]

GALLERY_DIR = {"segmentstream": "segmentstream", "fraxis": "fraxis", "brs": "brs",
               "vet-workshop": "vet", "bravestone": "bravestone",
               "neon-insights": "neon", "joompro": "joompro"}

# картинки галереи, которые повторяют обложку (обложка и так стоит наверху) — пропускаем
DUPLICATES = {"fraxis": ["g01.jpg"], "brs": ["g05.jpg"], "vet": ["g01.jpg"],
              "bravestone": ["g03.jpg"], "joompro": ["g01.jpg"]}

# Фото в футере: (файл, подпись RU, подпись EN). Добавляйте сюда новые страны.
PHOTOS_LIST = [(f"gallery/photo-{i:02d}.jpg", "Якутия", "Yakutia") for i in range(1, 11)]

# Интерфейсные строки
UI = {
    "ru": dict(
        prefix="", home="/", nav_label="Разделы", portfolio="портфолио", ai="ai-проекты", exp="опыт",
        name="Перелыгина Айаана", meta="Якутск<br>удалённо или релокация", lang_label="en", lang_title="English version",
        btn1=('href="/cv.pdf" download="Перелыгина Айаана — CV.pdf"', "скачать cv"),
        btn2=(f'href="{TELEGRAM}" target="_blank" rel="noopener"', "написать мне в telegram"),
        back="← на главную", task="задача", role="моя роль", done_we="что сделали", done_i="что сделала",
        result="результат", more="ещё кейсы", cover="обложка", screen="экран", email="почта", home_alt="На главную",
        case_word="кейс", author="Айаана Перелыгина", case_og="кейс Айааны Перелыгиной", locale="ru_RU",
    ),
    "en": dict(
        prefix="/en", home="/en/", nav_label="Sections", portfolio="portfolio", ai="ai projects", exp="experience",
        name="Ayaana Perelygina", meta="Yakutsk, Russia<br>remote or relocation", lang_label="ru", lang_title="Русская версия",
        btn1=(f'href="{LINKEDIN}" target="_blank" rel="noopener"', "linkedin"),
        btn2=(f'href="mailto:{EMAIL}"', "email me"),
        back="← back to home", task="task", role="my role", done_we="what we did", done_i="what I did",
        result="result", more="more case studies", cover="cover", screen="screen", email="email", home_alt="Home",
        case_word="case study", author="Ayaana Perelygina", case_og="case study by Ayaana Perelygina", locale="en_US",
    ),
}


def L(c, lang, key):
    """Поле кейса на нужном языке (EN берётся из c['en'], если есть)."""
    if lang == "en" and key in c["en"]:
        return c["en"][key]
    return c.get(key)


def gallery(slug):
    d = GALLERY_DIR[slug]
    files = sorted(f for f in os.listdir(os.path.join(ROOT, "assets/img/cases", d))
                   if f.endswith(".jpg") and f not in DUPLICATES.get(d, []))
    return [f"/assets/img/cases/{d}/{f}" for f in files]


def menu(lang, other_url, on_home=False):
    """Боковое меню. На главной аватар не ссылка, а пункты ведут на якоря этой же страницы."""
    u = UI[lang]
    p = "" if on_home else u["prefix"] + "/"
    pre = "" if not on_home else ("" if lang == "ru" else "/")
    avatar = f'<img class="menu__avatar" src="{pre}assets/img/avatar-menu.png" width="40" height="40" alt="">' if on_home else \
        f'<a href="{u["home"]}"><img class="menu__avatar" src="/assets/img/avatar-menu.png" width="40" height="40" alt="{u["home_alt"]}"></a>'
    ai_pill = f'        <a class="pill" href="{p}#ai">{u["ai"]}</a>\n' if SHOW_AI else ""
    btn1 = u["btn1"][0].replace('href="/cv.pdf"', 'href="cv.pdf"') if (on_home and lang == "ru") else u["btn1"][0]
    return f"""  <aside class="menu">
    <div class="menu__top">
      {avatar}
      <p class="menu__name">{u["name"]}<br><span>Lead Web Designer</span></p>
      <nav class="menu__nav" aria-label="{u["nav_label"]}">
        <a class="pill" href="{p}#portfolio">{u["portfolio"]}</a>
{ai_pill}        <a class="pill" href="{p}#experience">{u["exp"]}</a>
      </nav>
    </div>
    <div class="menu__bottom">
      <p class="menu__meta">{u["meta"]}</p>
      <a class="pill pill--lang" href="{other_url}" hreflang="{u["lang_label"]}" lang="{u["lang_label"]}" title="{u["lang_title"]}">{u["lang_label"]}</a>
      <a class="btn btn--outline" {btn1}>{u["btn1"][1]}</a>
      <a class="btn btn--dark" {u["btn2"][0]}>{u["btn2"][1]}</a>
    </div>
  </aside>"""


def photos_html(prefix, lang="ru"):
    lazy = ' loading="lazy"'
    k = 1 if lang == "ru" else 2
    imgs = "".join(f'<img src="{prefix}assets/img/{p[0]}" alt="{p[k]}" data-caption="{p[k]}"{lazy if i else ""}>'
                   for i, p in enumerate(PHOTOS_LIST))
    return (f'    <figure class="photo reel" data-interval="2000">\n      {imgs}\n'
            f'      <figcaption class="display">{PHOTOS_LIST[0][k]}</figcaption>\n    </figure>')


def links_html(lang):
    return f"""<ul class="links">
        <li><a href="{TELEGRAM}" target="_blank" rel="noopener">Telegram</a></li>
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
        <li><a href="mailto:{EMAIL}">{UI[lang]["email"]}</a></li>
        <li><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></li>
      </ul>"""


def footer(lang):
    return f"""    <section class="col footer">
      {links_html(lang)}
    </section>

{photos_html("/", lang)}"""


def ul(items):
    return "\n".join(f"          <li>{escape(i)}</li>" for i in items)


def case_url(slug, lang):
    return f"{SITE}{UI[lang]['prefix']}/cases/{slug}.html"


def person_ld():
    return {"@type": "Person", "name": "Ayaana Perelygina", "alternateName": "Айаана Перелыгина",
            "jobTitle": "Lead Web Designer", "url": SITE + "/en/"}


def page(c, others, lang):
    e = escape
    u = UI[lang]
    title = L(c, lang, "title")
    lead = L(c, lang, "lead")
    url = case_url(c["slug"], lang)
    other_lang = "ru" if lang == "en" else "en"
    facts = "\n".join(f'        <div><dt class="label">{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in L(c, lang, "facts"))
    shots = "\n".join(f'      <img src="{src}" alt="{e(title)} — {u["screen"]} {i}" loading="lazy">'
                      for i, src in enumerate(gallery(c["slug"]), 1))
    more = "\n".join(
        f'''        <a class="more__card" href="{u["prefix"]}/cases/{o["slug"]}.html">
          <img src="/assets/img/{o["cover"]}" alt="" loading="lazy">
          <span class="more__name">{e(L(o, lang, "title"))}</span>
        </a>''' for o in others)
    result = ""
    if L(c, lang, "result"):
        result = f"""
    <section class="col story">
      <div class="story__item">
        <p class="label">{u["result"]}</p>
        <p class="story__lead">{e(L(c, lang, "result"))}</p>
      </div>
    </section>
"""
    done_label = c.get("done_label", "что сделали")
    if lang == "en":
        done_label = u["done_i"] if done_label == "что сделала" else u["done_we"]
    ld = {"@context": "https://schema.org", "@type": "CreativeWork", "name": f"{title} — {u['case_word']}",
          "headline": lead, "description": L(c, lang, "task"), "inLanguage": lang, "url": url,
          "image": f"{SITE}/assets/img/{c['cover']}", "keywords": ", ".join(L(c, lang, "tags")),
          "author": person_ld(), "creator": person_ld()}
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)} — {u["case_word"]} · {u["author"]}, Lead Web Designer</title>
  <meta name="description" content="{e(lead)}">
  <meta name="author" content="{u["author"]}">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="ru" href="{case_url(c["slug"], "ru")}">
  <link rel="alternate" hreflang="en" href="{case_url(c["slug"], "en")}">
  <link rel="alternate" hreflang="x-default" href="{case_url(c["slug"], "en")}">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="{u["locale"]}">
  <meta property="og:site_name" content="{u["author"]} — Lead Web Designer">
  <meta property="og:title" content="{e(title)} — {u["case_og"]}">
  <meta property="og:description" content="{e(lead)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/img/{c["cover"]}">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
  <link rel="icon" href="/assets/img/avatar-menu.png">
  <link rel="preload" href="/assets/fonts/VelaSans-GX.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="preload" href="/assets/fonts/Sexsmith.otf" as="font" type="font/otf" crossorigin>
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
<!-- Сгенерировано tools/build_cases.py — правьте тексты там -->

{menu(lang, case_url(c["slug"], other_lang).replace(SITE, ""))}

  <main class="page">

    <section class="col case-hero">
      <a class="back" href="{u["prefix"]}/#portfolio">{u["back"]}</a>
      <h1 class="display case-hero__title">{e(title)}</h1>
      <p class="story__lead">{e(lead)}</p>
      <ul class="tags">{"".join(f"<li>{e(t)}</li>" for t in L(c, lang, "tags"))}</ul>
      <dl class="facts">
{facts}
      </dl>
    </section>

    <img class="case__img" src="/assets/img/{c["cover"]}" alt="{e(title)} — {u["cover"]}">

    <section class="col story">
      <div class="story__item">
        <p class="label">{u["task"]}</p>
        <p class="story__lead">{e(L(c, lang, "task"))}</p>
      </div>
      <div class="story__item">
        <p class="label">{u["role"]}</p>
        <ul class="story__list">
{ul(L(c, lang, "role"))}
        </ul>
      </div>
      <div class="story__item">
        <p class="label">{e(done_label)}</p>
        <ul class="story__list">
{ul(L(c, lang, "done"))}
        </ul>
      </div>
    </section>

    <div class="shots">
{shots}
    </div>
{result}
    <section class="more">
      <p class="label more__label">{u["more"]}</p>
      <div class="more__grid">
{more}
      </div>
    </section>

{footer(lang)}

  </main>

  <script src="/menu.js"></script>
  <script src="/reel.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- главная

REEL_FRAMES = 6  # обложка + 5 картинок из галереи
NO_REEL = {"bravestone", "neon-insights", "joompro"}  # маленькие карточки — одна картинка


def update_index_reels(s):
    """Пересобирает шоурилы на карточках главной: обложка + следующие картинки без повторов."""
    for c in CASES:
        pat = re.compile(r'<div class="case__img reel"><img src="assets/img/%s" alt="([^"]*)">.*?</div>|<img class="case__img" src="assets/img/%s" alt="([^"]*)" loading="lazy">' % (re.escape(c["cover"]), re.escape(c["cover"])))
        m = pat.search(s)
        if not m:
            print("  нет шоурила на главной для", c["slug"])
            continue
        alt = m.group(1) or m.group(2)
        if c["slug"] in NO_REEL:
            s = s[:m.start()] + f'<img class="case__img" src="assets/img/{c["cover"]}" alt="{alt}" loading="lazy">' + s[m.end():]
            continue
        frames = [f'<img src="assets/img/{c["cover"]}" alt="{alt}">']
        frames += [f'<img src="{src[1:]}" alt="" loading="lazy">' for src in gallery(c["slug"])[:REEL_FRAMES - 1]]
        s = s[:m.start()] + '<div class="case__img reel">' + "".join(frames) + "</div>" + s[m.end():]
    return s


def replace_menu_footer(s, lang, other_url, photo_prefix):
    s = re.sub(r'  <aside class="menu">.*?</aside>', lambda _: menu(lang, other_url, on_home=True), s, count=1, flags=re.S)
    s = re.sub(r'<ul class="links">.*?</ul>', lambda _: links_html(lang), s, count=1, flags=re.S)
    s = re.sub(r'    <figure class="photo[^"]*".*?</figure>', lambda _: photos_html(photo_prefix, lang), s, count=1, flags=re.S)
    return s


KNOWS = ["Web design", "Design systems", "Design team leadership", "Design review", "UX design",
         "Responsive design", "AI-assisted design and development", "Webflow", "Tilda", "Figma", "Lovable", "Claude Code"]


def person_full(lang):
    ru = lang == "ru"
    return {
        "@context": "https://schema.org", "@type": "ProfilePage",
        "url": SITE + ("/" if ru else "/en/"), "inLanguage": lang,
        "mainEntity": {
            "@type": "Person",
            "name": "Айаана Перелыгина" if ru else "Ayaana Perelygina",
            "alternateName": "Ayaana Perelygina" if ru else "Айаана Перелыгина",
            "jobTitle": "Lead Web Designer",
            "description": ("Lead Web Designer: 6 лет делаю сайты для B2B и SaaS, последние 2 года — лидом в студии. "
                            "Дизайн-системы, качество, процессы и AI в работе команды." if ru else
                            "Lead Web Designer with 6 years in websites for B2B and SaaS, the last 2 as a lead at a design studio. "
                            "Design systems, quality, processes and AI in team workflows."),
            "url": SITE + "/en/", "image": SITE + "/assets/img/avatar-hero.png", "email": "mailto:" + EMAIL,
            "address": {"@type": "PostalAddress", "addressLocality": "Якутск" if ru else "Yakutsk", "addressCountry": "RU"},
            "knowsLanguage": ["ru", "en"], "knowsAbout": KNOWS,
            "alumniOf": {"@type": "CollegeOrUniversity",
                         "name": "ПСТГУ" if ru else "St. Tikhon’s Orthodox University"},
            "sameAs": [LINKEDIN, TELEGRAM, INSTAGRAM],
        },
    }


def ld_script(lang):
    return f'  <script type="application/ld+json">{json.dumps(person_full(lang), ensure_ascii=False)}</script>\n'


def hreflang_links():
    return (f'  <link rel="alternate" hreflang="ru" href="{SITE}/">\n'
            f'  <link rel="alternate" hreflang="en" href="{SITE}/en/">\n'
            f'  <link rel="alternate" hreflang="x-default" href="{SITE}/en/">\n')


def build_index():
    p = os.path.join(ROOT, "index.html")
    s = open(p, encoding="utf-8").read()
    head, sep, body = s.partition("<body>")
    # шапка: hreflang и JSON-LD всегда свежие
    head = re.sub(r'  <link rel="alternate" hreflang[^\n]*\n', "", head)
    head = re.sub(r'  <script type="application/ld\+json">.*?</script>\n', "", head, flags=re.S)
    head = head.replace('  <meta property="og:type"', hreflang_links() + '  <meta property="og:type"', 1)
    head = head.replace('  <link rel="icon"', ld_script("ru") + '  <link rel="icon"', 1)
    s = head + sep + body.replace(" ", " ")  # снять старый типограф, ниже прогоним заново
    s = update_index_reels(s)
    s = re.sub(r'<section class="section" id="ai"( hidden)?>', '<section class="section" id="ai"%s>' % ("" if SHOW_AI else " hidden"), s)
    s = replace_menu_footer(s, "ru", "/en/", "")
    open(p, "w", encoding="utf-8").write(typo_html(s))
    print("index.html: шоурилы, меню, футер, типограф")
    return s


# Английская главная: (русский фрагмент, английский). Фрагменты ищутся в index.html без типографа.
INDEX_EN = [
    ('<html lang="ru">', '<html lang="en">'),
    ('<!-- Боковое меню (на мобильном — шапка) -->', '<!-- Side menu (header on mobile) -->'),
    ('<!-- Привет -->', '<!-- Hi -->'), ('<!-- Чем занимаюсь -->', '<!-- What I do -->'),
    ('<!-- Портфолио -->', '<!-- Portfolio -->'), ('<!-- AI-проекты -->', '<!-- AI projects -->'),
    ('<!-- Опыт -->', '<!-- Experience -->'), ('<!-- Обо мне -->', '<!-- About -->'), ('<!-- Фото -->', '<!-- Photos -->'),
    # hero
    ('alt="Айаана"', 'alt="Ayaana"'),
    ('<span class="muted">Привет, я Айаана — Lead Web Designer. </span>6 лет делаю сайты для B2B и SaaS, последние 2 года — лидом в студии: отвечаю за дизайн-системы, качество и процессы, встраиваю AI в работу команды.',
     '<span class="muted">Hi, I’m Ayaana — Lead Web Designer. </span>For 6 years I’ve been designing websites for B2B and SaaS, the last 2 as a lead at a design studio: I’m responsible for design systems, quality and processes, and I bring AI into the team’s workflow.'),
    # чем занимаюсь
    ('<span class="muted">Выстраиваю процессы.</span> Как проект проходит путь от брифа до релиза, кто за что отвечает, где хранятся правила и контекст.',
     '<span class="muted">Building processes.</span> How a project moves from brief to release, who owns what, where rules and context live.'),
    ('<span class="muted">Делаю сайты.</span> От концепции и дизайн-системы до сборки на Tilda, Webflow или с AI и передачи в разработку.',
     '<span class="muted">Designing websites.</span> From concept and design system to a build in Tilda, Webflow or with AI, and handoff to developers.'),
    ('<span class="muted">Отвечаю за качество.</span> Ревью макетов, дизайн-системы, единые стандарты для всех проектов.',
     '<span class="muted">Owning quality.</span> Design reviews, design systems, shared standards across all projects.'),
    ('<span class="muted">Внедряю AI в работу команды.</span> Правила, контекст и дизайн-токены, с которыми AI работает в стиле бренда.',
     '<span class="muted">Bringing AI into the team.</span> Rules, context and design tokens that keep AI output on-brand.'),
    ('<span class="muted">Веду людей.</span> Распределяю задачи, даю обратную связь, помогаю разобраться в проекте.',
     '<span class="muted">Leading people.</span> Assigning tasks, giving feedback, helping people get into a project.'),
    # портфолио
    ('<h2 class="display">Портфолио</h2>', '<h2 class="display">Portfolio</h2>'),
    ('href="cases/', 'href="/en/cases/'),
    ('alt="Сайт SaaS-платформы маркетинговой аналитики"', 'alt="Website for a marketing analytics SaaS platform"'),
    ('alt="Каталог B2B-производителя кабельных сборок"', 'alt="Catalog website for a B2B cable assembly manufacturer"'),
    ('alt="Сайт ремонтной компании из Дубая"', 'alt="Website for a Dubai renovation company"'),
    ('alt="Сайт онлайн-школы для ветеринаров"', 'alt="Website for an online school for veterinarians"'),
    ('alt="Сайт агентства недвижимости в Португалии"', 'alt="Website for a real estate agency in Portugal"'),
    ('alt="Сайт консалтинга по данным и AI"', 'alt="Website for a data and AI consultancy"'),
    ('alt="Сайт логистического сервиса"', 'alt="Website for a logistics service"'),
    ('alt="Сайт юридической фирмы"', 'alt="Website for a law firm"'),
    ('<li>многостраничный сайт</li>', '<li>multi-page website</li>'),
    ('<li>тимлид</li>', '<li>team lead</li>'),
    ('<li>дизайн-система</li>', '<li>design system</li>'),
    ('<li>сайт</li>', '<li>website</li>'),
    ('<li>редизайн</li>', '<li>redesign</li>'),
    ('<li>AI-разработка</li>', '<li>AI development</li>'),
    ('<li>инструмент</li>', '<li>tool</li>'),
    ('Сделала страницу для сайта SaaS-платформы аналитики и передала проект веб-дизайнеру. Дальше вела его и иллюстратора: команда собрала 10+ страниц и систему иллюстраций.',
     'Designed one page for a SaaS analytics platform’s website and handed the project over to a web designer. Then led him and an illustrator: the team built 10+ pages and an illustration system.'),
    ('Разложила большой каталог B2B-производителя в понятную структуру и собрала его на Tilda.',
     'Organised a B2B manufacturer’s large catalog into a clear structure and built it on Tilda.'),
    ('Сделала страницу сайта ремонтной компании из Дубая и передала проект веб-дизайнеру. Дальше следила за его работой.',
     'Designed one page for a Dubai renovation company’s website and handed the project over to a web designer. Then oversaw his work.'),
    ('Переделала главную, каталог и другие страницы онлайн-школы для ветеринаров. Потом передала проект веб-дизайнеру и три года следила за его работой на поддержке.',
     'Redesigned the home page, catalog and other pages of an online school for veterinarians. Then handed the project over to a web designer and oversaw his work on support for three years.'),
    ('Сделала сайт агентства недвижимости в Португалии на основе готовой айдентики.',
     'Designed a website for a real estate agency in Portugal based on an existing identity.'),
    ('Сделала дизайн сайта для консалтинга по данным и AI и сама собрала его в Webflow.',
     'Designed a website for a data and AI consultancy and built it myself in Webflow.'),
    ('Перестроила сайт логистического сервиса на блочную систему и добавила CMS, чтобы команда сама публиковала кейсы.',
     'Rebuilt a logistics service’s website on a block system and added a CMS so the team can publish case studies on their own.'),
    # AI
    ('<h2 class="display">Делаю так, чтобы AI работал консистентно</h2>', '<h2 class="display">I make AI work consistently</h2>'),
    ('aria-label="Сайт студии — изображение скоро"', 'aria-label="Studio website — image coming soon"'),
    ('aria-label="Генератор КП — изображение скоро"', 'aria-label="Proposal generator — image coming soon"'),
    ('aria-label="Изображение скоро"', 'aria-label="Image coming soon"'),
    ('Собрала дизайн-систему сайта студии и описала её для AI. Все страницы собираются по одним правилам.',
     'Built the design system of the studio’s website and documented it for AI. Every page follows the same rules.'),
    ('Сделала генератор коммерческих предложений. Менеджер собирает КП сам, без дизайнера.',
     'Built a commercial proposal generator. Managers put proposals together themselves, without a designer.'),
    ('Переделала дизайн сайта юридической фирмы и передала его в Lovable, чтобы клиент развивал сайт сам.',
     'Redesigned a law firm’s website and moved it to Lovable so the client can develop the site on their own.'),
    ('Убрала AI-слоп с сайта продукта и описала дизайн-систему в DESIGN.md, по которой клиент дальше работает с AI.',
     'Removed AI slop from a product website and described the design system in DESIGN.md, which the client now uses to work with AI.'),
    # опыт
    ('<h2 class="display">6 лет в вебе, 2 из них — лидом</h2>', '<h2 class="display">6 years in web design, 2 of them as a lead</h2>'),
    ('Международная дизайн-студия <a', 'International design studio <a'),
    ('<span class="muted">Lead Web Designer.</span> Отвечала за веб-направление: сайты и дизайн-системы для клиентов из Европы, ОАЭ и России. Встроила AI в процессы студии. Вела дизайнеров на проектах, презентовала концепции клиентам.',
     '<span class="muted">Lead Web Designer.</span> Led the web direction: websites and design systems for clients in Europe, the UAE and Russia. Brought AI into the studio’s processes. Led designers on projects, presented concepts to clients.'),
    ('Цифровая студия <u>27flows.</u> <span class="muted">Старший веб-дизайнер.</span> Делала сайты с нуля и редизайны: прототипы, адаптив, дизайн-системы, сборка на Tilda.',
     'Digital studio <u>27flows.</u> <span class="muted">Senior Web Designer.</span> Websites from scratch and redesigns: prototypes, responsive design, design systems, builds on Tilda.'),
    ('Маркетинговое агентство <a', 'Marketing agency <a'),
    ('<span class="muted">Веб-дизайнер и разработчик на Tilda.</span> Работала в команде над лендингами и многостраничными сайтами.',
     '<span class="muted">Web Designer and Tilda Developer.</span> Worked in a team on landing pages and multi-page websites.'),
    ('Фриланс. <span class="muted">Веб-дизайнер.</span> Сайты, визуал для соцсетей, афиши.',
     'Freelance. <span class="muted">Web Designer.</span> Websites, social media visuals, posters.'),
    ('<p class="label">образование</p>', '<p class="label">education</p>'),
    ('Skillbox — менеджер проектов, 6 месяцев, 2025', 'Skillbox — Project Management, 6 months, 2025'),
    ('Dzzzen Design — дизайн-мышление, 2 месяца, 2024', 'Dzzzen Design — Design Thinking, 2 months, 2024'),
    ('Moscow Digital Academy — веб-дизайн, 6 месяцев, 2022', 'Moscow Digital Academy — Web Design, 6 months, 2022'),
    ('ПСТГУ — бакалавр, прикладная математика и информатика, 2017 — 2021',
     'St. Tikhon’s Orthodox University, Moscow — BSc in Applied Mathematics and Computer Science, 2017 — 2021'),
    # обо мне
    ('Живу между Якутском и Вьетнамом. Люблю путешествовать, смотреть фильмы и сериалы, много гулять и делать что-нибудь руками. Сейчас сдаю на права.',
     'I live between Yakutsk and Vietnam. I love travelling, watching films and series, long walks and making things by hand. Currently taking my driving test.'),
]

# в EN-главной пути абсолютные, потому что она лежит в /en/
EN_PATHS = [('src="assets/', 'src="/assets/'), ('href="styles.css"', 'href="/styles.css"'),
            ('href="assets/', 'href="/assets/'), ('src="menu.js"', 'src="/menu.js"'), ('src="reel.js"', 'src="/reel.js"')]

EN_HEAD = f"""  <title>Ayaana Perelygina — Lead Web Designer</title>
  <meta name="description" content="Lead Web Designer with 6 years of experience designing websites for B2B and SaaS, the last 2 as a lead at a design studio. Design systems, quality, processes and AI in team workflows. Open to remote work or relocation.">
  <meta name="author" content="Ayaana Perelygina">
  <link rel="canonical" href="{SITE}/en/">
{hreflang_links()}  <meta property="og:type" content="profile">
  <meta property="og:locale" content="en_US">
  <meta property="og:site_name" content="Ayaana Perelygina — Lead Web Designer">
  <meta property="og:title" content="Ayaana Perelygina — Lead Web Designer">
  <meta property="og:description" content="Websites for B2B and SaaS, design systems and AI in team workflows. Portfolio and case studies.">
  <meta property="og:url" content="{SITE}/en/">
  <meta property="og:image" content="{SITE}/assets/img/og-en.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
"""


def build_en_index(plain_ru):
    s = plain_ru
    missing = []
    for ru, en in INDEX_EN:
        if ru not in s:
            missing.append(ru[:70])
        s = s.replace(ru, en)
    for a, b in EN_PATHS:
        s = s.replace(a, b)
    s = re.sub(r"  <title>.*?(?=  <link rel=\"icon\")", lambda _: EN_HEAD + ld_script("en"), s, count=1, flags=re.S)
    s = replace_menu_footer(s, "en", "/", "/")
    leftover = re.findall(r">[^<]*[А-Яа-яЁё][^<]*<", s.partition("<body>")[2])
    leftover += re.findall(r'(?:alt|aria-label|title)="[^"]*[А-Яа-яЁё][^"]*"', s.partition("<body>")[2])
    os.makedirs(os.path.join(ROOT, "en"), exist_ok=True)
    open(os.path.join(ROOT, "en", "index.html"), "w", encoding="utf-8").write(s)
    print("en/index.html")
    for m in missing:
        print("  ! не нашла фрагмент для перевода:", m)
    for t in leftover:
        if "Русская версия" not in t:
            print("  ! остался русский текст:", t[:90])


# ---------------------------------------------------------------- для поисковиков и AI

def write_sitemap():
    pairs = [(SITE + "/", SITE + "/en/")] + [(case_url(c["slug"], "ru"), case_url(c["slug"], "en")) for c in CASES]
    rows = []
    for ru, en in pairs:
        for loc in (ru, en):
            rows.append(f'  <url><loc>{loc}</loc>'
                        f'<xhtml:link rel="alternate" hreflang="ru" href="{ru}"/>'
                        f'<xhtml:link rel="alternate" hreflang="en" href="{en}"/></url>')
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
                + "\n".join(rows) + "\n</urlset>\n")
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "PerplexityBot",
            "Google-Extended", "Applebot-Extended"]
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\n# AI-ассистенты и AI-поиск — явно разрешены\n")
        for b in bots:
            f.write(f"User-agent: {b}\nAllow: /\n\n")
        f.write(f"Sitemap: {SITE}/sitemap.xml\n")
    print("sitemap.xml, robots.txt")


def write_llms():
    lines = [
        "# Ayaana Perelygina — Lead Web Designer",
        "",
        "> Ayaana Perelygina (Айаана Перелыгина) is a Lead Web Designer with 6 years of experience designing websites "
        "for B2B and SaaS companies, the last 2 years as the web lead at an international design studio. "
        "Open to Web Design Team Lead / Lead Web Designer roles, remote or with relocation. "
        "Based in Yakutsk, Russia (UTC+9). Languages: Russian (native), English (B2).",
        "",
        "## What she does",
        "",
        "- Builds design processes: how a project goes from brief to release, who owns what, where rules and context live",
        "- Owns design quality: design reviews, design systems, shared standards across projects",
        "- Leads web designers and illustrators: assigns tasks, reviews layouts, gives feedback",
        "- Brings AI into design team workflows: design systems documented for AI, DESIGN.md, design tokens, handoff to Lovable",
        "- Designs websites and builds them in Tilda and Webflow",
        "",
        "## Experience",
        "",
        "- 2024–2026 — busy studio (international design studio), Lead Web Designer: web direction, websites and design systems for clients in Europe, the UAE and Russia; led designers on projects; brought AI into the studio's processes; built a proposal generator that managers use without a designer",
        "- 2023–2024 — 27flows (digital studio), Senior Web Designer",
        "- 2022–2023 — Beauty Alliance (marketing agency), Web Designer and Tilda Developer",
        "- 2020–2022 — Freelance web designer",
        "",
        "## Case studies",
        "",
    ]
    for c in CASES:
        en = c["en"]
        lines.append(f"- [{en.get('title', c['title'])}]({case_url(c['slug'], 'en')}): {en['lead']} Her part: {en['facts'][1][1]}.")
    lines += [
        "",
        "## Skills and tools",
        "",
        "Figma, Webflow (CMS), Tilda (Zero Block), Lovable, Claude Code, Codex, HTML + CSS, Photoshop, Illustrator, Notion. "
        "Design systems, UI kits, prototyping, responsive design, UX (user flows, CJM, personas), developer handoff.",
        "",
        "## Education",
        "",
        "- Skillbox — Project Management, 2025",
        "- Dzzzen Design — Design Thinking, 2024",
        "- Moscow Digital Academy — Web Design, 2022",
        "- St. Tikhon's Orthodox University, Moscow — BSc in Applied Mathematics and Computer Science, 2017–2021",
        "",
        "## Contacts",
        "",
        f"- Website: {SITE}/en/ (Russian version: {SITE}/)",
        f"- Email: {EMAIL}",
        f"- LinkedIn: {LINKEDIN}",
        f"- Telegram: {TELEGRAM}",
        f"- CV (PDF, Russian): {SITE}/cv.pdf",
        "",
    ]
    with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("llms.txt")


def main():
    n = len(CASES)
    for lang, folder in (("ru", "cases"), ("en", "en/cases")):
        os.makedirs(os.path.join(ROOT, folder), exist_ok=True)
        for i, c in enumerate(CASES):
            others = [CASES[(i + k) % n] for k in (1, 2, 3)]
            html = page(c, others, lang)
            if lang == "ru":
                html = typo_html(html)
            with open(os.path.join(ROOT, folder, c["slug"] + ".html"), "w", encoding="utf-8") as f:
                f.write(html)
    print("cases/*.html и en/cases/*.html  (%d кейсов)" % n)
    plain = build_index()
    build_en_index(plain)
    write_sitemap()
    write_llms()


if __name__ == "__main__":
    main()
