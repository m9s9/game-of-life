label got_fish:
    # Сцена не меняется с шага 8_1
    "Есть! Это должно быть рыба!"
    $ turn_timer += 1
    if lure_type_selected == 'leech':
        #no_disturbance_to_fish
        $ fish_count_roll = renpy.random.choice([1, 1, 1, 1, 2, 2])
    else:
        $ turn_timer += 1
        $ fish_count_roll = renpy.random.choice([2, 2, 2, 3, 3, 3])

    show p_cheer at truecenter with moveintop
    "Вы поймали рыбу весом в [fish_count_roll] кг!"
    $ inventory.add(fish, fish_count_roll)
    hide p_cheer

    jump fishing_in_progress_screen
