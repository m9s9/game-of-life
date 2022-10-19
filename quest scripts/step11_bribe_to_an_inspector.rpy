label bribe_to_an_inspector:
    scene start_location
    show insp at right
    "При слове \"деньги\" лицо инспектора озарилось жадной улыбкой."

label bribe_menu:
    menu:
        #TODO прикрутить рандом для генерации суммы?
        # TODO add check whether player has money >= bribe to show him bribe-taking choice in menu
        # If money < bribe probably we need to add choice leading to another fail ending (and we can add inspector reply)
        insp "- Что ж, за [bribe] cr я готов в виде исключения освободить тебя от подоходного налога"
        "Заплатить":
            $ inventory.remove(money, bribe)
            show insp at right with hpunch
            insp "- Вот и славно!"

            hide insp
            "Инспектор шустро засунул ваше подношение в карман."
            show insp at right
            insp "- Заходите почаще!"
            hide insp
            jump good_end1

        "Торговаться":
            hide insp
            show p at left
            p "- А может, сбросишь сотенку-другую, а?"
            #TODO картинка подмигивающего игрока
            hide p
            "Вы заискивающе подмигнули инспектору."
            $ bribe_roll = renpy.random.choice([1, 2])
            if bribe_roll ==1 and inventory.get_amount(money) > 0:
                jump successful_discount
            else:
                jump bribe_failed


label successful_discount:
    show insp at right
    insp "- Ладно, сотню скину"
    $ bribe -=100
    hide insp

    "Инспектор заметно поморщился."
    jump bribe_menu


label bribe_failed:
    #TODO картинка грозного инспектора с пистолетом
    show insp at right with hpunch
    insp "- Ты мне надоел!!!"
    "Ниспектор грозно зарычал, тыкая вам пистолетом в самое лицо."
    insp "- В общем, гони сюда всю свою рыбу и скажи спасибо, что я не оштрафовал тебя за попытку подкупа должностного лица!!!"
    "Вы поняли, что спорить бесполезно, и отдали инспектору весь свой улов."
    hide insp
    jump fiasco_scene
