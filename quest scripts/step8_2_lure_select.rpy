label lure_type_choice:
    #Сцена не меняется с шага 8_1
    show lure_select
    menu:
        "Нацепить пиявку" if inventory.get_amount(leech) >= 1:
            hide lure_select
            $ inventory.remove(leech, 1)
            $ lure_type_selected = 'leech'
            jump distance_select

        "Нацепить таракана" if inventory.get_amount(cockroach) >= 1:
            hide lure_select
            $ inventory.remove(cockroach, 1)
            $ lure_type_selected = 'cockroach'
            jump distance_select

        "Использовать шашку" if inventory.get_amount(bomb) >= 1:
            hide lure_select
            jump bomb_use_scene

        "Пойти в другой конец пруда" if inventory.get_amount(cockroach) >= 1 or inventory.get_amount(leech) >= 1:
            hide lure_select
            jump step8

        "Возвращаться к кораблю":
            hide lure_select
            $ turn_timer +=1
            jump to_the_ship
