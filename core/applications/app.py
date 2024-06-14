from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    verbose_name = 'NeoTelecom'
    menu_show_home = False
    form_inlines_hide_original = True

    menu = [
        ParentItem('Маркетинг', children=[
            ChildItem(model='banners.banner'),
            ChildItem(model='promotions.promotion'),
            ChildItem(model='news.news'),
            ChildItem(model='core.vacancy'),
        ], icon='fa fa-th'),
        ParentItem('Обратная связь', children=[
            ChildItem(model='core.joinus', label='Заявки на подключение'),
            ChildItem(model='core.callme', label='Заявки на звонок'),
        ]),
        ParentItem('Тарифы', app='tariffs'),
        ParentItem('Ядро', children=[
            ChildItem(model='core.city', permissions='is_superuser'),
            ChildItem(model='channels.channel'),
            ChildItem(model='maps.map'),
            ChildItem(model='handbook.handbook'),
            ChildItem(model='core.neotvfiles'),
        ]),
        ParentItem('Управление пользователями', children=[
            ChildItem('Пользователи', 'auth.user'),
            ChildItem('Группы пользователей', 'auth.group'),
        ], permissions='is_superuser'),
    ]
