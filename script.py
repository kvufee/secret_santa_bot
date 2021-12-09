def who_is_your_goal(user):
    all_members = {
        '@sexozavr': 'Даня Дивеев',
        '@segtree': 'Никита Поздняков',
        '@FlashRS0': 'Рома Лаврентьев',
        '@wibbleydock': 'Лёха Попов',
        '@homyatsosek': 'Соня Матвеенко',
        '@onefore_in_tg': 'Ярик Мудров',
        '@XXXkiller228': 'Федя Ланской',
        '@mlfhuntr': 'Даня Лапин',
        '@afastress': 'Марина Лебкова',
        '@KrivolapovaA': 'Анастасия Анатольевна',
        '@datagrabber_bot': 'Миша Задорский',
        '@I_name_I': 'Глебка Заграничнов',
        '@frspacee': 'Оля Фёдорова',
        '@g10wer': 'Сеня Рябов',
        '@o1eg1live': 'Ульяна Фролова'
    }

    dataset_sh = {
        '@wibbleydock': '@sexozavr',
        '@sexozavr': '@segtree',
        '@datagrabber_bot': '@FlashRS0',
        '@o1eg1live': '@wibbleydock',
        '@homyatsosek': '@homyatsosek',
        '@onefore_in_tg': '@onefore_in_tg',
        '@segtree': '@XXXkiller228',
        '@afastress': '@mlfhuntr',
        '@KrivolapovaA': '@afastress',
        '@XXXkiller228': '@KrivolapovaA',
        '@g10wer': '@datagrabber_bot',
        '@frspacee': '@I_name_I',
        '@I_name_I': '@frspacee',
        '@mlfhuntr': '@g10wer',
        '@FlashRS0': '@o1eg1live'
    }

    return f'Ты даришь подарок: {all_members[dataset_sh[f"@{user}"]]}'


if __name__ == '__main__':
    pass
