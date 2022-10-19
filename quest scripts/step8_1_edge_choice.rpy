
label step8:
    scene start_location
    menu:
        "Пруд Грезус, в котором водятся мертинии, покрыт тиной и плесенью.
        Неудивительно, думаете вы.
        \nВ какой же конец пруда направиться?"
        "В западный - кажется, он лучше других подходит для нереста" if inventory.get_amount(cockroach) >= 1 or inventory.get_amount(leech) >= 1:
            $ turn_timer +=1
            jump west_edge

        "В восточный - там, скорее всего, у рыбы больше корма" if inventory.get_amount(cockroach) >= 1 or inventory.get_amount(leech) >= 1:
            $ turn_timer +=1
            jump east_edge

        "В южный - должно быть, рыба ушла туда, где ей теплее" if inventory.get_amount(cockroach) >= 1 or inventory.get_amount(leech) >= 1:
            $ turn_timer +=1
            jump south_edge

        "В северный - наверное, рыба лучше всего чувствует себя там" if inventory.get_amount(cockroach) >= 1 or inventory.get_amount(leech) >= 1:
            $ turn_timer +=1
            jump north_edge

        "Возвращаться к кораблю":
            jump to_the_ship


label west_edge:
    scene west_edge
    "Вы находитесь на западном берегу пруда. Берег здесь крутой и обрывистый. Вы нашли себе удобное местечко и присели на землю. Что делать дальше?"
    $ edge_selected = 'Вы находитесь на западном берегу пруда. Берег здесь крутой и обрывистый. Вы нашли себе удобное местечко и присели на землю. Что делать дальше?'
    $ player_position = 1
    jump lure_type_choice
label north_edge:
    scene north_edge
    "Вы находитесь на северном берегу пруда. Берег здесь слегка заболочен. Вы нашли более или менее сухое местечко и присели на землю. Что делать дальше?"
    $ edge_selected = 'Вы находитесь на северном берегу пруда. Берег здесь слегка заболочен. Вы нашли более или менее сухое местечко и присели на землю. Что делать дальше?'
    $ player_position = 4
    jump lure_type_choice
label east_edge:
    scene east_edge
    "Вы находитесь на восточном берегу пруда. Берег здесь весьма заболочен, а сам пруд зарос камышом. Вы решили не садиться на землю вообще. Что делать дальше?"
    $ edge_selected = 'Вы находитесь на восточном берегу пруда. Берег здесь весьма заболочен, а сам пруд зарос камышом. Вы решили не садиться на землю вообще. Что делать дальше?'
    $ player_position = 7
    jump lure_type_choice
label south_edge:
    scene south_edge
    "Вы находитесь на южном берегу пруда. Берег здесь пологий, поросший мягкой травкой. Вы сели прямо на траву. Что делать дальше?"
    $ edge_selected = 'Вы находитесь на южном берегу пруда. Берег здесь пологий, поросший мягкой травкой. Вы сели прямо на траву. Что делать дальше?'
    $ player_position = 10
    jump lure_type_choice
