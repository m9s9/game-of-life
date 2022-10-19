##THIRD ADVICE AND BOMB
##THIRD ADVICE AND BOMB
##THIRD ADVICE AND BOBM
label the_bomb_and_third_advice:
    scene bog_go_away
    show fisherman at right
    "Пеленг быстро передал вам небольшой продолговатый цилиндр, завёрнутый в бумагу."
    show bomb at truecenter with dissolve
    "- Активировать, я надеюсь, умеешь?"
    hide fisherman

    show p at left
    "Вы кивнули."
    hide p

    show fisherman at right
    fisherman "- Отлично! Значит, активируешь и кидаешь в воду в любом конце пруда. Важно, чтобы шашка взорвалась прямо в воде.
    Тогда вся рыба, где бы она ни была, бросится в противоположный от места взрыва конец пруда."
    fisherman "Но если ты рассчитаешь неправильно, и взрыв произойдёт в воздухе, то его обязательно услышит рыбинспектор,
    и тебя прогонят отсюда взашей, отобрав весь улов. Так что сам решай, пользоваться шашкой или нет!"
    hide fisherman
    "И довольный пеленг ушёл прочь."
    $ inventory.add(bomb, 1)
    hide bomb
    jump step8
