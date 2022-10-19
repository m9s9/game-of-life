
label step4:
    scene bait
    menu:
        "Вы осмотрелись. Прямо перед вами огромная грязная лужа. За вашей спиной лежит старое поваленное дерево."
        "Попробовать ловить наживку в грязной луже":
            jump lure_luzha_scene

        "Попробовать ловить наживку рядом с поваленным деревом":
            jump lure_three_scene




label lure_luzha_scene:
    scene bait_lu
    $ lure_roll = renpy.random.choice([0, 1, 1, 2, 2, 2])
    if lure_roll == 0:
        scene bait_dirt
        "Вы сунули руку по локоть в вонючую жижу... Оп! Что-то есть!
        \nВы сжали кулак и вытащили добычу на свет божий.
        \nНо на ладони оказалась только кучка грязи и травинок.
        \nКопаемся дальше..."
    elif lure_roll == 1:
        show leech at truecenter with zoomin
        $ inventory.add(leech, 1)
        "Вы сунули руку по локоть в вонючую жижу...
        \nОп! Есть! Вы сжали кулак и вытащили добычу на свет божий.
        \nПИЯВКА.
        \nХорошая наживка! Копаемся дальше..."
        hide leech
    else:
        show leech at truecenter with zoomin
        $ inventory.add(leech, 2)
        "Вы сунули руку по локоть в вонючую жижу... Оп! Есть!
        \nВы сжали кулак и вытащили добычу на свет божий.
        \nПИЯВКА."
        hide leech
        show leech2 at truecenter
        "\nДа не одна, а две штуки!
        \nПовезло!
        \nКопаемся дальше..."
        hide leech2
    jump lure_amount_check


label lure_three_scene:
    scene bait_der
    $ lure_roll = renpy.random.choice([0, 1, 1, 2, 2])
    if lure_roll == 0:
        scene bait_dirt
        "Вы обшариваете ветки и мох вокруг поваленного дерева...
        \nОп! Есть! Вы сжали кулак и вытащили кого-то на свет божий.
        \nПытаясь рассмотреть добычу вы раскрыли кулак.
        \nНо на ладони только кучка грязи и травинок. Копаемся дальше..."
    elif lure_roll == 1:
        show cockroach at truecenter with moveintop
        $ inventory.add(cockroach, 1)
        "Вы обшариваете ветки и мох вокруг поваленного дерева...
        \nОп! Есть! Вы сжали кулак и вытащили кого-то на свет божий.
        \nТАРАКАН.
        \nПрекрасная наживка! Копаемся дальше..."
        hide cockroach
    else:
        scene bait_der2
        $ inventory.add(cockroach, 2)
        "Вы обшариваете ветки и мох вокруг поваленного дерева...
        \nОп! Есть! Вы сжали кулак и вытащили кого-то на свет божий.
        ТАРАКАН. Жирненький!"
        scene bait_der5
        "И ВТОРОЙ!!
        \nОтвлёкшись на добычу, вы не сразу заметили что рядом с первым был и второй!
        \nДва таракана резко бросились врассыпную, но вы шустро их изловили."
        "\nПовезло!
        \nКопаемся дальше..."

    jump lure_amount_check



label lure_amount_check:
    # Check whether player has caught all available bait
    if inventory.get_amount(leech) + inventory.get_amount(cockroach) >= 10:
        jump step5
    else:
        jump step4
