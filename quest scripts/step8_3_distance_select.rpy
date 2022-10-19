
label distance_select:
    # Сцена не меняется с шага 8_1
    # TODO move $ fishing_bobber_position = player_position from all choices before menu
    menu:
        "Забросить ближе к берегу":
            $ fishing_bobber_position = player_position
            $ fishing_bobber_position += 0
            "Вы забросили удочку и стали ждать"
            jump loot_selection_tree

        "Забросить подальше от берега":
            $ fishing_bobber_position = player_position
            $ fishing_bobber_position += 1
            "Вы забросили удочку и стали ждать"
            jump loot_selection_tree

        "Забросить как можно дальше":
            $ fishing_bobber_position = player_position
            $ fishing_bobber_position += 2
            "Вы забросили удочку и стали ждать"
            jump loot_selection_tree


label loot_selection_tree:
    # Player throw his rod to the shoal location
    if fishing_bobber_position in fish_shool_position[turn_timer % 12]:
        jump got_fish

    # Player didn't find boot yet, so here is his chance
    elif not boot_was_caught:
        $ boot_roll = renpy.random.random()
        # Player found the boot!
        if boot_roll > 0.8:
            jump i_catch_boot

    # Player didn't catch anything (no fish, no boot)
    jump no_fish
