# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THEdeledele
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess
import os

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
from libqtile import qtile

cursor_warp = True

home_path="/home/max"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

redshift_states = [7000, 6000, 5000, 4000, 3000]
def cycle_redshift(qtile):
    qtile.cmd_spawn("redshift -x")
    qtile.cmd_spawn(f"redshift -O {redshift_states[0]}")
    last = redshift_states.pop(0)
    redshift_states.append(last)



mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),


    Key([mod], "a", lazy.spawn("rofi -show window -font 'hack 15'"), desc="Reset all window sizes"),
    Key([mod], "s", lazy.spawn("rofi -show run -font 'hack 15'"), desc="Reset all window sizes"),
    Key([mod], "d", lazy.spawn("rofi -show drun -font 'hack 15'"), desc="Reset all window sizes"),
    Key([mod], "7", lazy.spawn("nautilus --new-window"), desc="Reset all window sizes"),
    Key([mod], "8", lazy.spawn("chromium --new-window"), desc="Reset all window sizes"),
    Key([mod], "0", lazy.spawn("alacritty"), desc="Reset all window sizes"),
        
    Key([mod], "o", lazy.next_screen(), desc="Next Monitor"),


    Key([], "XF86AudioMute", lazy.spawn("amixer  set Master 1+ toggle")),
     Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set 'Master' 10%-")),
     Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set 'Master' 10%+")),
    #Key([], "XF86AudioLowerVolume", lazy.spawn(f"bash {home_path}/scripts/sound.sh down")),
    #Key([], "XF86AudioRaiseVolume", lazy.spawn(f"bash {home_path}/scripts/sound.sh up")),
    Key([], "XF86AudioMicMute", lazy.spawn("amixer set Capture toggle")),
       Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 10%+")),
    #Key([], "XF86MonBrightnessDown", lazy.spawn(f"bash {home_path}/scripts/brightness.sh down")),
    #Key([], "XF86MonBrightnessUp", lazy.spawn(f"bash {home_path}/scripts/brightness.sh up")),

    #
    # Key([], "F1", lazy.spawn("amixer  set Master 1+ toggle")),
    # Key([], "F2", lazy.spawn(" amixer set 'Master' 10%-")),
    # Key([], "F3", lazy.spawn(" amixer set 'Master' 10%+")),
    # Key([], "F4", lazy.spawn("amixer set Capture toggle")),
    # Key([], "F5", lazy.spawn("brightnessctl set 10%-")),
    # Key([], "F6", lazy.spawn("brightnessctl set 10%+")),
    
    Key([mod, "shift"], "m", lazy.spawn("bash monitor.sh"), desc="Reset all window sizes"),
    Key([mod, "shift"], "b", lazy.spawn("bash fastpdf.sh"), desc="Reset all window sizes"),
    Key([mod, "shift"], "n", lazy.function(cycle_redshift) , desc="cycle trough redshift"),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    Key(
        [mod],
        "Tab",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "a", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "d", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

#groups = [Group(i) for i in "1234"]

groups = [
    # Screen affinity here is used to make
    # sure the groups startup on the right screens
    Group(name="1", screen_affinity=0),
    Group(name="2", screen_affinity=0),
    #Group(name="3", screen_affinity=0),
    Group(name="q", screen_affinity=1),
    Group(name="w", screen_affinity=1),
    #Group(name="e", screen_affinity=1),
]
def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in '12':
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()

    return _inner

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.function(go_to_group(i.name))),
            # mod1 + letter of group = switch to group
            # Key(
            #     [mod],
            #     i.name,
            #     lazy.group[i.name].toscreen(),
            #     desc="Switch to group {}".format(i.name),
            # ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            # Key(
            #     [mod, "shift"],
            #     i.name,
            #     lazy.window.togroup(i.name, switch_group=True),
            #     desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#E14545", "#E14545"], border_width=4,
                   margin = 16),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Jetbrains Mono",
    fontsize=18,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                #widget.WindowName(),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Clock(format="%d-%m-%Y %a %I:%M %p"),
                widget.Sep(foreground='FFFFFF', linewidth=2, padding=10),
                widget.Battery(foreground="#FFFC00", charge_char='C', discharge_char='D', full_char='F', low_foreground="#FF0000", low_percentage=0.1),
                widget.Sep(foreground='FFFFFF', linewidth=2, padding=10),
                #widget.Bluetooth(),
                #widget.Wlan(),
                widget.Net(),
                widget.NetGraph(type='line', graph_color='ffff00', border_color='000000', frequency=0.1),
                widget.Systray(),
                widget.Sep(foreground='FFFFFF', linewidth=2, padding=10),
                widget.CPU(),
                widget.CPUGraph(type='line', graph_color='ffff00', border_color='000000', frequency=0.1),
                widget.Sep(foreground='FFFFFF', linewidth=2, padding=10),
                widget.Volume(fmt='Vol: {}'),
                widget.Sep(foreground='FFFFFF', linewidth=2, padding=10),
                widget.Memory(),
                widget.MemoryGraph(type='line', graph_color='ffff00', border_color='000000', frequency=1),
                widget.Sep(foreground='FFFFFF', linewidth=2, padding=10),
                widget.CryptoTicker(crypto="ETH"),
                widget.Sep(foreground='FFFFFF', linewidth=2, padding=10),
                #widget.Notify()

                # widget.QuickExit(),
            ],
            24,
            backgrond="#020000"
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
# mouse = [def go_to_group(name: str) -> Callable:
#     def _inner(qtile: Qtile) -> None:
#         if len(qtile.screens) == 1:
#             qtile.groups_map[name].toscreen()
#             return
#
#         if name in '123':
#             qtile.focus_screen(0)
#             qtile.groups_map[name].toscreen()
#         else:
#             qtile.focus_screen(1)
#             qtile.groups_map[name].toscreen()
#
#     return _inner
#     Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
#     Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
#     Click([mod], "Button2", lazy.window.bring_to_front()),
# ]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
