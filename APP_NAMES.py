from abc import ABC


class APP_NAMES(ABC):
    # MY APPS NAMES:
    # Если сразу давать русский перевод, то при появлении новых приложений не протеряется и не забудется
    HOME = 'home'

    SIGN = 'sign'
    REG_USER = 'reguser'
    LOGIN_USER = 'loginuser'
    LOGOUT_USER = 'logoutuser'
    PROFILE_UP = 'profileup'

    USER_PROFILE = 'userprofile'
    PORTFOLIO = 'portfolio'
    BLOG = 'blog'
    ARTICLES = 'articles'
    ARTICLE = 'article'
    USER_MESSAGES = 'usermessages'

    STANDARDS = 'standards'
    ISSUES = 'issues'
    EVENTS = 'events'
    CONTESTS = 'contests'

    ARTISTS = 'artists'


    PARTNERS = 'partners'

class VERBOSE_APP_NAMES(APP_NAMES):
    # MY APPS NAMES:
    # Если сразу давать русский перевод, то при появлении новых приложений не протеряется и не забудется
    HOME = u'Главная'

    SIGN = u'Вход'
    REG_USER = u'Регистрация'
    LOGIN_USER = u'Войти'
    LOGOUT_USER = u'Выйти'
    PROFILE_UP = u'Редактировать профиль'
    USER_PROFILE = u'Профиль'
    PORTFOLIO = u'Портфолио'
    BLOG = u'Блог'
    ARTICLES = u'Статьи'
    ARTICLE = u'Статья'
    USER_MESSAGES = u'Сообщения'

    STANDARDS = u'Нормативы'
    ISSUES = u'Обсуждения'
    EVENTS = u'События'
    CONTESTS = u'Конкурсы'

    ARTISTS = u'Проектанты'
    PARTNERS = u'Партнеры'


print(VERBOSE_APP_NAMES.PARTNERS)