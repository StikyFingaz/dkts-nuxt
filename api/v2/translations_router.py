from fastapi import APIRouter
from fastapi_babel import _  # noqa - Not a portected memeber, Babel gettext.

router = APIRouter(
    prefix='/translations',
    tags=['translations'],
    dependencies=[],
    responses={}
)


# @router.get('/')
# async def fetch_strings():
#     common = {k: _(v) for k, v in common_strings.items()}
#     home = {k: _(v) for k, v in home_strings.items()}
#     events = {k: _(v) for k, v in events_strings.items()}
#     festival = {k: _(v) for k, v in festival_strings.items()}
#     about = {k: _(v) for k, v in about_strings.items()}
#     history = {k: _(v) for k, v in history_strings.items()}
#     stages = {k: _(v) for k, v in stages_strings.items()}
#
#     translated_strings = {
#         "common": common,
#         "home": home,
#         "events": events,
#         "festival": festival,
#         "about": about,
#         "history": history,
#         "stages": stages,
#     }
#
#     return translated_strings


@router.get('/')
async def fetch_common_strings():
    translated_strings = {k: _(v) for k, v in common_strings.items()}
    return translated_strings


@router.get('/home')
async def fetch_home_strings():
    translated_strings = {k: _(v) for k, v in home_strings.items()}
    return translated_strings


@router.get('/events')
async def fetch_event_strings():
    translated_strings = {k: _(v) for k, v in events_strings.items()}
    return translated_strings


@router.get('/festival')
async def fetch_festival_strings():
    translated_strings = {k: _(v) for k, v in festival_strings.items()}
    return translated_strings


@router.get('/about')
async def fetch_about_strings():
    translated_strings = {k: _(v) for k, v in about_strings.items()}
    return translated_strings


@router.get('/history')
async def fetch_history_strings():
    translated_strings = {k: _(v) for k, v in history_strings.items()}
    return translated_strings


@router.get('/stages')
async def fetch_stages_strings():
    translated_strings = {k: _(v) for k, v in stages_strings.items()}
    return translated_strings


# Navbar and footer
common_strings = {
    # Head
    'title': _('Welcome to DPT Shumen'),
    'description': _('Go to the theater! It\'s great! Here, you will be able to find information about upcoming '
                     'premieres and current performances.'),
    # Navbar
    'home': _('What\'s On'),
    'festival': _('Theater Festival'),
    'repertoire': _('Repertoire'),
    'search': _('Find actor, play...'),
    'tickets': _('Tickets'),
    # Navbar -> About Dropdown
    'about': _('About Us'),
    'collective': _('Collective'),
    'history': _('History'),
    'stages': _('Stages'),
    'theatre': _('About the Theatre'),
    'careers': _('Careers'),
    # Footer
    'address': _('bul. "Slavyanski" 72, 9700 Shumen Center, Shumen'),
    'online': _('Theatre Shumen Online'),
    'support': _('With the financial support of:'),
    'legal': _('Legal Information'),
    'dkts': _('DPT Shumen'),
    'privacy': _('Privacy Policy'),
    'gdpr': _('GDPR Policy'),
    'public': _('Public Information Policy'),
}

home_strings = {
    # Head
    'title': _('What\'s On'),
    'dkts': _('DPT Shumen'),
    'description': _('Go to the theater! It\'s great! Here, you will be able to find information about upcoming '
                     'premieres and current performances.'),
    # Events Table
    'upcoming': _('Upcoming Events'),
    'ticket': _('Ticket'),
    # Main Accent
    'more': _('Read More'),
}

events_strings = {
    # Head
    'title': _('Repertoire'),
    'dkts': _('DPT Shumen'),
    # Play
    # -> Poster Row
    'more': _('Read More'),
    'ticket': _('Ticket'),
    'trailer': _('Watch Trailer'),
    # -> Details Row
    # - Main Details
    'soon': _('Coming Soon'),
    'min': _('min'),
    'minutes': _('minutes'),
    'seats': _('Remaining Seats:'),
    # - Crew Details
    'author': _('Author'),
    'director': _('Director'),
    'scenographer': _('Scenographer'),
    'composer': _('Composer /music/'),
    'dramatization': _('Dramatization'),
    'artistic': _('Artistic director'),
    'translation': _('Translation'),
    # - Description Modal
    'close': _('Close'),
    # Plays
    # -> Play Filters
    'current': _('Current'),
    # Audience Dropdown
    'audience': _('Audience'),
    'adults': _('Adults'),
    'children': _('Children'),
    # Genre Dropdown
    'genre': _('Genre'),
    'drama': _('Drama'),
    'comedy': _('Comedy'),
    'other': _('Other'),
    'puppet': _('Puppet Show'),
    'childPlay': _('Children\'s Play'),
    # Reset Button
    'reset': _('Reset')
}

festival_strings = {
    # Head/common
    'title': _("Друмеви Театрални Празници"),
    'home': _('Начало'),
    'about': _('За Фестивала'),
    'achievements': _('Постижения'),
    'apply': _('Кандидатстване'),
    'more': _('Научете Повече'),
    'scroll': _('Продължи Надолу'),
    'mandatory': _('Това поле е задължително*'),
    'not_mandatory': _('Това поле HE е задължително'),
    'upload': _('Качване'),
    'submit': _('Изпращане'),
    # Home
    'details': _('гр. Шумен | 11-16 Май 2024'),
    'sponsors': _('С финансовата подкрепа на:'),
    # About
    'history': _('История'),
    # -> Short Story
    'which': _('който'),
    'highlight_1': _('насърчава'),
    'highlight_2': _('търси'),
    'highlight_3': _('създава'),
    # - Line 1
    'line_1': _('Празникът на българската драматургия от 1966 г.,'),
    # - Line 2
    'line_2': _('новото,'),
    # - Line_3
    'line_3': _('непознатото,'),
    # - Line 4
    'line_4': _('традиции на родните театрални сцени.'),
    'long_story': _('Историята на „Друмеви театрални празници“ е изключително богата, не само заради достолепната '
                    'възраст на фестивала, но и интересните и катарзисни моменти, през които преминава форумът. След '
                    'създаването на „Друмеви театрални игри“ (първото име на фестивала), той се провежда последователно'
                    ' и през 1967, 1970, 1972 и 1976 година, придобивайки характер на национален културен форум. '
                    'Изданието от 1976 година е последвано от дълга пауза, като фестивалът възобновява своята дейност '
                    'отново през 1993 година с ново име – Шуменска театрална среща „Нова българска драма“, с което се '
                    'слави и през последвалите две издания през 1994 и 1995 година. След изданието през 1995 година, '
                    'фестивалът отново е паузиран, но възобновява своята дейност само три години по-късно.\nПървите '
                    'четири издания на фестивала не са изцяло посветени на българската драматургия, повлияни от '
                    'политически причини – във фестивалната програма преобладават руски текстове. Въпреки силното '
                    'политическо напрежение през късните 70-те години, в афиша на „Друмеви театрални дни“ през 1976 '
                    'година присъстват само и единствено спектакли по български текстове. Така и до днес.\nПрез 1993 '
                    'година, при първото издание след дългото прекъсване на осъществяването на фестивала, възниква и '
                    'нов, изключително важен компонент за фестивалния живот – Авторски прочит. От тогава до днес, '
                    'във форума се включват множество автори, като в селектираните от различните селекционери през '
                    'годините влизат 184 текста.\nВ последните години „Друмеви театрални празници“ служи като стимул на'
                    ' младите, на търсещите български театрали, които намират смисъл в българската драматургия и '
                    'литература. Във фестивалния афиш ежегодно присъстват различни жанрове – моноспектакли, драми, '
                    'комедии, пърформанси, документални, експериментални спектакли. В последните издания могат да бъдат'
                    ' забелязани и заглавия от независимата сцена, което дава възможност на гостите на фестивала да се '
                    'докоснат до неконвенционалния български театър.\nПрез 2005 година в рамките на фестивала за първи '
                    'път са поканени международни продукции по български текстове – изключително  любопитно и нужно '
                    'явление, което доказва на българския театрал и зрител, че нашето творчество излиза извън граница и'
                    ' бива ценено и поставяно в друг контекст, в друга среда. През изминалите години от първото '
                    'международно издание на „Друмеви театрални празници“ са гостували продукции от Русия, Македония, '
                    'Турция, Германия, Румъния, Грузия и др.\nВ рамките на своята 58-годишна история и със своите 32 '
                    'изминали издания, Международен фестивал „Друмеви театрални празници“ е приютил и показал на '
                    'гостите на формата цели 378 спектакъла.'),
    # Achievements
    'inspiration': _('Вдъхновяваме българските творци от 58 години'),
    # -> Achievement Cards
    # - Issues Card
    'issues_num': _('32 издания'),
    'issues': _('Издания, които стимулират и насърчават българските театрали да намират смисъл в родната драматургия '
                'и литература.'),
    # - Shows Card
    'shows_num': _('378 спектакъла'),
    'shows': _('В рамките на своята дълголетна история, фестивалът е показал на своите гости цели 378 спектакъла на '
               'различните сцени в театъра и града.'),
    # - Plays Card
    'plays_num': _('184 пиеси'),
    'plays': _('От 1993 година, в „Авторски прочит“ са прочетени и селектирани 184 нови и непоставяни пиеси на '
               'български драматурзи.'),
    # Application
    'category': _('Кандидайтствай в направление'),
    # -> Application Cards
    # - Play Card
    'play': _('Преглед на спектакли'),
    'play_desc': _('*Спектаклите могат да бъдат продукция на държавни, общински или частни културни институти.'),
    # - Text Card
    'text': _('Авторски прочит'),
    'text_desc': _('*Текстът трябва да бъде непубликуван и непоставян, за да се впише в регламента на фестивала!'),
    # -> Options modal
    'or': _('или'),
    'options': _('Опции за кандидатстване'),
    'options_descr': _('Даваме ви две опции, чрез които да можете да кандидатствате за ваше улеснение. Моля изберете '
                       'един от двата варианта.'),
    'option_email': _('Чрез имейл:'),
    'option_email_descr': _('Изтеглете, попълнете и изпратете файла на theatreshumen@gmail.com.'),
    'option_online': _('Онлайн тук:'),
    'option_online_descr': _('Попълнете през уебсайта онлайн формуляра за кандидатстване.'),
    'download_btn': _('Изтегли Тук'),
    'online_btn': _('Продължи'),
    # -> Application Form
    # - #1 Slide
    '1_title': _('Преглед на Спектакли'),
    'organization': _('Име на театър или организация'),
    'play_title': _('Заглавие на спектакъла'),
    'play_message': _('Пълен запис на спектакъла (до 5гб)'),
    'author': _('Автор'),
    'director': _('Режисьор'),
    'scenographer': _('Сценограф'),
    'composer': _('Композитор'),
    'others': _('Други'),
    'actors': _('Участват'),
    # - #2 Slide
    '2_title': _('Данни за Спектакъла'),
    'annotation': _('Кратка анотация'),
    'pics': _('Снимков материал - до 5 снимки + плакат (общо 6 файла)'),
    'pics_message': _('Пуснете файловете тук или натиснете за качване'),
    'poster': _('Плакат'),
    'length': _('Времетраене'),
    'intermission': _('Антракт'),
    # - #3 Slide
    # Title is the same
    'contact': _('Лице за контакти, длъжност'),
    'address': _('Адрес'),
    'phone': _('Телефон'),
    'mail': _('E-mail'),
    'website': _('Web страница'),
    # - #4 Slide
    # Title is the same
    'specs': _('Технически и /или други специфични изисквания по построяване на декора, осветлението, музикалното '
               'оформление и други/описват се конкретно'),
    'chigi': _('Необходим брой чиги'),
    'space': _('Минимални размери на игралното пространство (Ш/В/Д)'),
    'build_time': _('Необходимо време за строеж на'),
    'decors': _('Декор'),
    'lights': _('Осветление'),
    'sound': _('Звук'),
    'demolition_time': _('Необходимо време за разваляне на декора'),
    'workers': _('Каква бройка хора и от кои технически служби на театъра домакин са ви необходими: горна '
                 'механизация, сценични работници, осветители, тон техници, мултимедиен техник, реквизитор, '
                 'гардеробиер и други.'),
    'workers_short': _('Каква бройка хора и от кои технически служби на театъра домакин са ви необходими?'),
    # - #5 Slide
    # Title is the same
    'contact_numbers': _(
        'Телефонен номер на директора; на отговорника на трупата за турнето и отговорник по технически въпроси;'
    ),
    'host_expenses': _('Данни за разходи, които се поемат от организатора на фестивала'),
    'crew': _('Списък на пътуващия екип със спектакъла (имена и длъжност), за изчисляване на командировъчни разходи.'),
    'crew_short': _('Списък на пътуващия екип'),
    'compensations': _('Хонорари на гост-актьори (поименно), доказани с прикачено копие на договор'),
    'copyrights': _('Задължения по закона за авторските и сродни права, доказани с прикачено копие на договор'),
    'travel_expenses': _('Общо пътни разходи за превоз на:'),
    'decor_transpo': _('Декор и технически служби'),
    'crew_transpo': _('Актьорски състав'),
    # Text Option
    'text_option_title': _('Авторски прочит'),
    'text_rules': _('Регламент'),
    't_rule_1': _('Пиесата трябва да е непубликувана и непоставяна;'),
    't_rule_2': _('Текстът трябва да е написан на български език;'),
    't_rule_3': _('Да не надвишава 60 страници.'),
    'name': _('Име'),
    't_description': _('За успешното реализиране на фестивала, очакваме Вашите предложения за текстове в направление '
                       '„Авторски прочит“ до '),
    't_date': _('31 март 2024 г. '),
    't_description_rest': _('на имейл адрес drumevipraznici@dktshumen.com или на място в Драматично-куклен театър '
                            '„Васил Друмев“, Шумен.'),
    # Footer
    'sponsors_text': _('Спонсори на МФ „Друмеви театрални празници“:'),
}

about_strings = {
    # Head
    'title': _('Collective'),
    'dkts': _('DPT Shumen'),
    # Actor
    # -> Actor ID
    'more': _('Read More'),
    # -> Actor Plays
    'watch': _('You can watch'),
    'watchIn': _('in'),
    # -> Description Modal
    'close': _('Close'),
    # Actors
    'meet': _('Meet')
}

history_strings = {
    # Head
    'title': _('History'),
    'dkts': _('DPT Shumen'),
    # Title & pics
    'text_title': _('History of the Shumen Theater'),
    'pic1': _('Stefan Izvorski'),
    'pic2': _('Teachers and students on the Shumen theater stage. In the first row, from right to left, are Tsarevna '
              'Miladinova, Dobri Voinikov, the priest Todor Baychev - the prompter for the Shumen performances, '
              'and the co-director Todor Dzhabarov.'),
    'pic3': _('Kavrakov\'s cafe, where the play "Mihal Mishkoed" was performed in 1856, artist St. Petrov'),
    'pic4': _('Community Center "Archangel Michael"'),
    'pic5': _('The first theater curtain from 1898 in the "Archangel Michael" Community Center'),
    'pic6': _('Vasil Drumev'),
    'pic7': _('Dobri Voinikov'),
    'pic8': _('Sava Dobroplodni'),
    'pic9': _('Veliko Dukemendjiev'),
    'pic10': _('Shumen - ul. "Slavianska" - "Odeon" Theater'),
    'pic11': _('National Theatre "Vasil Drumev"'),
    'pic12': _('Drama Puppet Theater "Vasil Drumev"'),
    # History
    'p1': _('The Drama-Puppet Theatre "Vasil Drumev" is the inheritor of theatrical traditions in Shumen dating back '
            'to the era of the Bulgarian Revival. The first documented record of a theatrical event from the distant '
            'past is associated with Shumen. In 1813, the Armenian priest and cultural figure Minas Puzhshkyan, '
            'passing through our town, witnessed a locally organized "theater" event. He described the spectacle as a '
            '"play." This event was connected with the civic celebration of the Day of Saints Cyril and Methodius. '
            'This documents Shumen\'s initial contribution to Bulgarian theater knowledge.'),
    'p2': _('In a publication of the magazine "Lyuboslovie" from 1846, a theatrical celebration at the end of the '
            'school year is described, which took place at the Shumen Mutual Teaching School on August 11, 1846, '
            'under the guidance of teacher Stefan Izvorski. This date is considered the birth of the school theater. '
            'Its students were Vasil Drumev and Dobri Voynikov, and its deputy was Sava Dobroplodni. Voynikov studied '
            'and developed his own way of presenting student performances. This is the origin of the school theater, '
            'which featured characteristic dramatic dialogues of that era.'),
    'p3': _('The Shumen society was not satisfied with child-student plots, thus it took great interest in the '
            'cultural life of the Hungarian emigration. Among them were prominent dramatic, operatic artists, '
            'and musicians. The city\'s residents became witnesses to diverse cultural events – theatrical and '
            'operatic performances, orchestral renditions of European music. On March 13, 1850, the play "The '
            'Fugitive" by Sigligeti was staged on a specially decorated stage in the garrison barracks. This first '
            'theatrical performance caused extraordinary excitement in the city. It was then that Mihai Shafran '
            'created a permanent orchestra of immigrants, and the following year saw the establishment of the first '
            'Bulgarian orchestra. In September 1850, the Polish emigration staged the first opera production in the '
            'city, which was a great success.'),
    'p4': _('During the Crimean War (1853-1856), the people of Shumen gradually embraced new cultural entertainments '
            'brought from Europe by the English and French forces stationed in the city.'),
    'p5': _('With the growing cultural needs of Shumen society, the idea of establishing a public community center ('
            'chitalishte) was born. It was founded in 1856 in Shumen by the initiative of Sava Dobroplodni and was '
            'one of the first community centers in the country. It was initially located in the Kavrakov Cafe, '
            'and later in Tash Maaza – a building constructed by Hungarian emigrants, owned by Anastas Haji Stoyanov. '
            'At the insistence of Dobri Voynikov, chorbadji Anastas provided two rooms for the needs of the community '
            'center.'),
    'p6': _('In the same year, on August 15, Sava Dobroplodni staged the Bulgarianized comedy "Mihal Mishkoed." This '
            'performance is considered the beginning of contemporary Bulgarian theater. His assistant in directing '
            'was Czech emigrant Josef Meisner, and the actors were his students – Vasil Drumev, Vasil Stoyanov, '
            'and others. The success of the first Bulgarian performance confirmed in the artists and the Shumen '
            'community the belief that theatrical art is not foreign and inaccessible to Bulgarians. The theatrical '
            'enterprise in Shumen continued its development, being closely connected with the "Archangel Michael" '
            'community center (now the "Dobri Voynikov" community center) until the end of the 19th century.'),
    'p7': _('In the 1860s, Dobri Voynikov began his theatrical and dramaturgical activities. After school stage '
            'dialogues, he transitioned to larger-scale theatrical performances. On June 29, 1862, the comedy "The '
            'Doctor in Spite of Himself" by Molière was presented.'),
    'p8': _('Later, in the 70s, theatrical activity continued to develop within the community center, which became a '
            'hub of cultural and intellectual life in the city. A modern theater hall with a rich wardrobe and props '
            'was established, which was advanced for its time.'),
    'p9': _('During this period, plays such as "The Suffering Genevieve," "Nevyanka," "Lost Stanca," Voinikov\'s '
            '"Misunderstood Civilization" on November 21, 1871, "Raina Knyaginya" in February 1872, and also "Ivanko, '
            'the Killer of Asen I" by Vasil Drumev in 1874 were performed on the community center stage, among many '
            'others.'),
    'p10': _('Almost all of the actors were members of the community center. In Voinikov\'s historical plays, '
             'members of the Revolutionary Committee, led by chairman Panayot Volov, also participated. His '
             'involvement in "Misunderstood Civilization", which led to the event known as the "French Wedding,'
             '" is significant. This event defined Shumen\'s contribution to the Renaissance theater, lifting our '
             'national self-esteem. The Revolutionary Committee recognized the moral impact that theatrical '
             'performances had on the youth of Shumen, encouraging its members to participate in the theater. This '
             'prompted the Turkish authorities to halt the theatrical activity of the community center in 1875.'),
    'p11': _('In 1876, Dobri Voinikov returned to his hometown and, alongside his teaching work, once again engaged '
             'in community center activities. With the help of chairman Haralan Angelov, along with theater '
             'enthusiasts Todor Chengeliev and Todor Dzhabarov, he succeeded in forming a new association within the '
             'community center named "Shumen Theater Stage," where he became a director and producer. On the eve of '
             'the Liberation War, theatrical performances were again halted until the city was occupied by Russian '
             'forces.'),
    'p12': _('In the first two decades following the Liberation, theatrical activity in Shumen was organized jointly '
             'by the "Archangel Michael" community center and the teacher\'s society "Foundation." Thus, '
             'the new theater life after the Liberation began with Voinikov\'s play "Princess Raina," in honor of the '
             'long-awaited freedom.'),
    'p13': _('In 1882, the community of Russian officers in the city joined the community center theater. Prince '
             'Gedroitz prepared several Russian plays, including comedies by Gogol, "Marriage" and "Inspector '
             'General." The following year, the community center theater commission included Racho M. Rachev, '
             'Georgi Balkanski, and Encho Atanasov, who invigorated theatrical activity with the help of the '
             '"Foundation" teacher\'s society and the "Patriotism" women\'s society. Thus, in the mid-80s, '
             'the presentation of theatrical productions entirely shifted to the "Foundation" society. The wide '
             'corridor of the pedagogical school was often used as a theater salon.'),
    'p14': _('In 1898, extensive opportunities for theater emerged in Shumen when the new community center building '
             'was completed, featuring a modern hall and a wide stage for its time. Then, the "Foundation" society '
             'staged a new production of "Ivanko, the Killer of Asen I," which was one of its last theatrical '
             'performances.'),
    'p15': _('After 1900, the Renaissance theme gave way to contemporary artistic drama, mainly of Western European '
             'origin. The city\'s theatrical activity depended on the initiatives of some schools and incidentally '
             'formed amateur troupes. Attempts were made to establish a permanent professional theater. Many of these '
             'attempts were unsuccessful, until in 1910, Sava Stoyanov formed the "Bulgarian Free Theater" with '
             'several artists and enthusiasts. They debuted with the play "Happiness in Hell," which was highly '
             'successful. Due to lack of funding, the theater ceased its operations in 1912.'),
    'p16': _('After the First World War, the "Shumen City Theater" was founded by actors Vladimir Sheytanov and Al. '
             'Robertovich. In 1920, artists from the "Shumen People\'s Theater" joined it. The period from 1919 to '
             '1920 is one of the most dazzling for theater in Shumen. The "Shumen City Theater" existed until 1927, '
             'and during its eight years of existence, it staged 35 productions from contemporary European drama.'),
    'p17': _('In 1927, the professional artists in Shumen established the "Dramatic Studio," which was later renamed '
             'the "Shumen Municipal Theater," replacing the Shumen City Theater. The following year, the two theaters '
             'merged under the name "Shumen Municipal City Theater," which existed until 1934 with municipal support. '
             'On its stage, 16 Bulgarian plays were performed. After its closure, the first "Regional Theater" in the '
             'country was established, directed by Veliko Dyukmedzhiev, and it existed until 1937.'),
    'p18': _('A stable, professional municipal theater was established by the decision of the Shumen Municipality in '
             'the spring of 1944, with director Stefan Gudularov. Due to events in the same year, its activities '
             'began after September 9. The issue of a theater building was a challenge for the Shumen administration. '
             'The composition of the new municipal theater either performed on the community center stage or at the '
             '"Odeon" cinema. Neither of these venues was suitable for theatrical performances; the conditions were '
             'extremely poor – there were no dressing rooms, the premises were unhygienic, and the stage was '
             'unsuitable, which created numerous difficulties for a proper play production. The poor conditions began '
             'to affect the theater\'s work, and some of the artists moved to other ensembles.'),
    'p19': _('In the years after 1944, despite facing many challenges, the theater presented up to ten premieres per '
             'season. A committee for the construction of a theater building was formed, which managed to raise some '
             'funds, but they were extremely insufficient. The construction of such a building began, but even before '
             'the foundations were completed, it was halted.'),
    'p20': _('On January 1, 1949, the theater was nationalized. Its director was Ivan Georgiev. The first '
             'manifestation of the State People\'s Theater – Shumen was the restored production of Molière\'s '
             '"Tartuffe" directed by Dimitar Stratev.'),
    'p21': _('On October 13, 1957, after almost a decade of construction, the new multifunctional theater building '
             'with a revolving stage was opened. The theater\'s director was Doychin Doychinov. The grand opening of '
             'the new building took place with the play "Ivailo," prepared by director Boris Spirov.'),
    'p22': _('In 1966, the first edition of the "Drumevi Theater Holidays" festival was realized. The main organizer '
             'and host was the Drama Theater – Shumen. At that time, the theater was directed by actor Ivan Yanchev.'),
    'p23': _('On the occasion of celebrating the 1300th anniversary of the Bulgarian state, various festivities and '
             'the opening of new cultural institutions were organized in our city. On this occasion, and upon the '
             'proposal of the District Council for Art and Culture – Shumen, the beginning of the "Creators of the '
             'Bulgarian State" Complex was marked, starting from the theater building. The project for the main '
             'reconstruction and modernization of the theater was entrusted to architects Mikhail Sokolovski, '
             'Boris Kamilarov, and Tzanko Hadzhistoychev. The new building of the "Vasil Drumev" Drama Theater was '
             'opened on November 28, 1981. The first play performed on the main theater stage was the play '
             '"Daughter-in-Law."'),
    'p24': _('Starting from January 1, 2000, the Drama Theater – Shumen, and the Puppet Theater "Patilanchо,'
             '" were merged into the "Vasil Drumev" Drama and Puppet Theater – Shumen.'),
}

stages_strings = {
    # Buttons
    'floor': _('Floor Plan'),
    'seating': _('Seating Plan'),
    # Main Stage
    'main_title': _('Main Stage'),
    'main': _('The main stage in the theater has 485 seats distributed on the ground floor and balcony. It often hosts '
              'large and massive productions, both from our theater and guest performances.\n'
              'On the main stage, we have an orchestra pit, which is raised manually.'),
    # Small Stage
    'small_title': _('Chamber Stage'),
    'small': _('The Chamber Stage "Rada Spasova" has 60 seats. On it, we perform productions with an intimate '
               'character that require a more intimate space.\n'
               'Rada Spasova was a long-time director and actress at the "Vasil Drumev" Theater.'),
    # Children's Stage
    'children_title': _('Patilancho Stage'),
    'children': _('Since 2000, the Puppet and Drama Theater unite under one roof, giving rise to the "Patilantcho" '
                  'Hall. The stage has 60 seats and hosts all of our puppet performances.\n'
                  'The hall and the path to it are entirely painted in magical worlds.')
}
