
import tkinter as tk
from tkinter import font
from adbfunctions import send_key_event, run_adb_command, disconnect_tv, connect_tv


def create_button(frame, text, row, col, rowspan=1, colspan=1, width=6, height=2, bg='black', fg='white', command=None, state='normal', sticky='nsew', font=None):
    button = tk.Button(frame, text=text, width=width, height=height, bg=bg, fg=fg, font=font, relief='flat',
                       state=state, command=command)
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=3, pady=3, sticky=sticky)

def create_ui(root):
    root.title("Remote Control")
    root.geometry("300x700")
    root.configure(bg='grey')

    button_font = font.Font(size=10, weight='bold')
    emoji_font = font.Font(size=20, weight='bold')

    frame = tk.Frame(root, bg='black')
    frame.pack(pady=10, padx=10, fill='both', expand=True)

    for i in range(15):
        frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(i, weight=1)

    buttons = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["*", "0", "#"]
    ]

    keycodes = [
        [8, 9, 10],
        [11, 12, 13],
        [14, 15, 16],
        [17, 7, 18]
    ]

    for row_index, row in enumerate(buttons):
        for col_index, label in enumerate(row):
            create_button(frame, label, row_index, col_index, bg='black',
                          command=lambda code=keycodes[row_index][col_index]: send_key_event(code))

    create_button(frame, "LANG.", 2, 3, colspan=1, bg='grey', command=lambda: send_key_event(213))
    create_button(frame, "SUB", 3, 3, colspan=1, bg='grey', command=lambda: send_key_event(175))

    create_button(frame, "➕", 3, 0, colspan=1, bg='black', command=lambda: send_key_event(24))
    create_button(frame, "V", 4, 0, colspan=1, bg='black', state='disabled')
    create_button(frame, "—", 5, 0, colspan=1, bg='black', command=lambda: send_key_event(25))
    create_button(frame, "⬆️", 3, 2, colspan=1, bg='black', command=lambda: send_key_event(166))
    create_button(frame, "P", 4, 2, colspan=1, bg='black', state='disabled')
    create_button(frame, "⬇️", 5, 2, colspan=1, bg='black', command=lambda: send_key_event(167))

# Place the Mute and Google Assistant Button
    create_button(frame, "🔇", 4, 1, bg='white', fg="red", command=lambda: send_key_event(164), font=emoji_font, width=1, height=1)
    create_button(frame, "🫧", 5, 1, bg='white', fg='blue', command=lambda: send_key_event(219), font=emoji_font, width=1, height=1)

# Add the Connect Button
    label = tk.Label(frame, text="TV IP Address:", bg='black', fg='white', font=button_font)
    label.grid(row=4, column=3, padx=3, pady=3, sticky='nse')
    entry = tk.Entry(frame, width=15)
    entry.grid(row=5, column=3, rowspan=4, padx=1, pady=1, sticky='n')
    connect_button = tk.Button(frame, text="Connect", bg='green', fg='white', font=button_font, command=lambda: connect_tv(entry.get()))
    connect_button.grid(row=6, column=3, padx=3, pady=3, sticky='nsew')

# Add the Channel Info and EPG buttons
    create_button(frame,"-   ℹ️", 6, 0, bg='white', fg="blue", command=lambda: send_key_event(227), font=emoji_font, width=1, height=1)
    create_button(frame,"📺", 6, 2, bg='white', fg='black', command=lambda: send_key_event(165), font=emoji_font, width=1, height=1)

# Add the Inputs Button
    inputs_button = tk.Button(frame, text="Inputs", bg='blue', fg='white', font=button_font, command=lambda: send_key_event(178))
    inputs_button.grid(row=9, column=3, padx=3, pady=3, sticky='nsew')

# Add the Power Button
    power_button = tk.Button(frame, text="⚡", bg='grey', fg='red', font=font.Font(size=14, weight='bold'), relief='raised', width=6, height=2, command=lambda: send_key_event(26))
    power_button.grid(row=0, column=3, padx=3, pady=3, sticky='nsew')

# Media Buttons
    create_button(frame, "Netflix", 11, 0, colspan=2, bg='red', fg='white', width=12, sticky='ew',
    command=lambda: run_adb_command("adb shell am start -n com.netflix.ninja/com.netflix.ninja.MainActivity"))
    create_button(frame, "YouTube", 11, 2, colspan=2, bg='white', fg='red', width=12, sticky='ew',
    command=lambda: run_adb_command("adb shell monkey -p com.google.android.youtube.tv -c android.intent.category.LAUNCHER 1"))
    create_button(frame, "Prime Video", 12, 0, colspan=2, bg='white', fg='black', width=12, sticky='ew',
    command=lambda: run_adb_command("adb shell am start -n com.amazon.amazonvideo.livingroom/com.amazon.ignition.IgnitionActivity"))
    create_button(frame, "Google Play", 12, 2, colspan=2, bg='white', fg='black', width=12, sticky='ew',
    command=lambda: run_adb_command("adb shell monkey -p com.android.vending -c android.intent.category.LAUNCHER 1"))

# Navigation Buttons
    create_button(frame, "⬆️", 6, 1, bg='black', command=lambda: send_key_event(19))
    create_button(frame, "◀️", 7, 0, bg='black', command=lambda: send_key_event(21))
    create_button(frame, "OK", 7, 1, bg='black', command=lambda: send_key_event(23))
    create_button(frame, "▶️", 7, 2, bg='black', command=lambda: send_key_event(22))
    create_button(frame, "⬆️", 8, 1, bg='black', command=lambda: send_key_event(20))

# Directional Buttons
    create_button(frame, "🔴", 9, 0, bg='grey', fg='red', command=lambda: send_key_event(130))
    create_button(frame, "🏠", 9, 1, bg='orange', colspan=2, sticky='ew', command=lambda: send_key_event(3), font=emoji_font, width=1, height=1)
    create_button(frame, "Back", 8, 0, bg='black', fg='white', command=lambda: send_key_event(4))
    create_button(frame, "Exit", 8, 2, bg='black', fg='white', command=lambda: send_key_event(178))
    create_button(frame, "MENU", 7, 3, bg='purple', command=lambda: send_key_event(82), font=button_font)
    create_button(frame, "TEXT", 8, 3, bg='black', command=lambda: send_key_event(233), font=button_font)


# Place colored buttons
    colors = ['red', 'green', 'yellow', 'blue']
    play_color_commands = [183, 184, 185, 186]
    for i, color in enumerate(colors):
        create_button(frame, "", 13, i, bg=color, width=5, command=lambda code=play_color_commands[i]: send_key_event(code))

# Place play control buttons
    play_controls = ['⏪', '⏹️▶️', '⏩', '⏺️']
    play_control_commands = [89, 85, 90, 86]
    for i, control in enumerate(play_controls):
        create_button(frame, control, 14, i, bg='black', command=lambda code=play_control_commands[i]: send_key_event(code))

# Kill connection with device
    root.protocol("WM_DELETE_WINDOW", lambda: [disconnect_tv(entry.get()), root.destroy()])

