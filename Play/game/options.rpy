define config.name = "凉宫春日的心愿"
define config.version = "1.0"
define config.window_title = "凉宫春日的心愿"
define config.has_sound = False
define config.has_music = False
define config.has_voice = False
define config.save_directory = "SOS_Project"
define build.name = "SOS_Project"
define build.version = "1.0"

init -1 python:
    config.screen_width = 1280
    config.screen_height = 800
    config.has_autosave = False
    config.autosave_on_quit = False
    config.autosave_on_choice = False
    config.rollback_enabled = False
    config.check_conflicting_properties = True
    config.quit_action = Quit(confirm=False)
    for keymap_name in (
            "game_menu", "help", "hide_windows", "self_voicing", "clipboard_voicing",
            "toggle_skip", "skip", "fast_skip", "toggle_afm", "focus_up", "focus_down",
            "focus_left", "focus_right"):
        if keymap_name in config.keymap:
            config.keymap[keymap_name] = []
    config.keymap["screenshot"] = ["alt_K_s"]
