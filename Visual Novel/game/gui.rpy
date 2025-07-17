init offset = -2

init python:
    gui.init(1920, 1080)

define config.check_conflicting_properties = True

################################################################################
## COLORS — Warm & Soft
################################################################################

define gui.accent_color = "#d6a97a"           # Warm tan
define gui.idle_color = "#755c48"             # Soft brown
define gui.idle_small_color = "#a78977"
define gui.hover_color = "#e8c9b0"            # Light cream highlight
define gui.selected_color = "#ffffff"
define gui.insensitive_color = "#755c4877"

define gui.muted_color = "#ede2d1"
define gui.hover_muted_color = "#d6a97a"

define gui.text_color = "#ffd0b4"
define gui.interface_text_color = "#3b2f28"

################################################################################
## FONTS — Friendly & Readable
################################################################################

define gui.text_font = "gui/fonts/SFCompactRounded.ttf"
define gui.name_text_font = "gui/fonts/Arial Rounded Bold.ttf"
define gui.interface_text_font = "gui/fonts/SFNSRounded.ttf"

define gui.text_size = 33
define gui.name_text_size = 45
define gui.interface_text_size = 30
define gui.label_text_size = 36
define gui.notify_text_size = 24
define gui.title_text_size = 75

################################################################################
## BACKGROUNDS
################################################################################

define gui.main_menu_background = "gui/main_menu.jpg"
define gui.game_menu_background = "gui/game_menu.jpg"

################################################################################
## TEXTBOX
################################################################################

define gui.textbox_height = 260
define gui.textbox_yalign = 0.94

define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(10, 10, 10, 10)
define gui.namebox_tile = False

define gui.dialogue_xpos = 420
define gui.dialogue_ypos = 75
define gui.dialogue_width = 1080
define gui.dialogue_text_xalign = 0.0

################################################################################
## BUTTONS — Soft & Simple
################################################################################

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(20, 12, 20, 12)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.accent_color
define gui.button_text_insensitive_color = gui.insensitive_color

define gui.button_text_xalign = 0.5

define gui.radio_button_borders = Borders(20, 10, 20, 10)
define gui.check_button_borders = Borders(20, 10, 20, 10)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(15, 10, 15, 10)

define gui.quick_button_borders = Borders(15, 10, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

################################################################################
## CHOICE BUTTONS — For Menus
################################################################################

define gui.choice_button_width = 1185
define gui.choice_button_borders = Borders(30, 12, 30, 12)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#755c48"
define gui.choice_button_text_hover_color = "#3b2f28"
define gui.choice_button_text_insensitive_color = "#755c4877"

################################################################################
## SAVE / LOAD SLOTS
################################################################################

define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(20, 20, 20, 20)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 384
define config.thumbnail_height = 216

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

################################################################################
## POSITIONING & SPACING
################################################################################

define gui.navigation_xpos = 60
define gui.skip_ypos = 20
define gui.notify_ypos = 70
define gui.choice_spacing = 36
define gui.navigation_spacing = 12
define gui.pref_spacing = 20
define gui.pref_button_spacing = 10
define gui.page_spacing = 10
define gui.slot_spacing = 20
define gui.main_menu_text_xalign = 1.0

################################################################################
## FRAMES
################################################################################

define gui.frame_borders = Borders(12, 12, 12, 12)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 12, 75, 12)
define gui.notify_frame_borders = Borders(24, 12, 60, 12)
define gui.frame_tile = False

################################################################################
## BARS & SLIDERS
################################################################################

define gui.bar_size = 32
define gui.scrollbar_size = 16
define gui.slider_size = 32

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

define gui.unscrollable = "hide"

################################################################################
## HISTORY SCREEN
################################################################################

define config.history_length = 200
define gui.history_height = 210
define gui.history_spacing = 6

define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0

################################################################################
## NVL MODE
################################################################################

define gui.nvl_borders = Borders(0, 15, 0, 30)
define gui.nvl_list_length = 6
define gui.nvl_height = 173
define gui.nvl_spacing = 15

define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

################################################################################
## LOCALIZATION
################################################################################

define gui.language = "unicode"

################################################################################
## MOBILE VARIANTS
################################################################################

init python:
    @gui.variant
    def touch():
        gui.quick_button_borders = Borders(60, 21, 60, 0)

    @gui.variant
    def small():
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        gui.slider_size = 54
        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035
        gui.quick_button_text_size = 30

        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        gui.nvl_height = 255
        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488
        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8
        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30
        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30