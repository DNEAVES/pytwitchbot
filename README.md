# pytwitchbot
A Twitch chatbot made with Python. Chat commands from approved users can trigger keyboard shortcuts on the streamer's side.

A hollow python twitch bot.
I initially made it for a friend of mine so I could use twitch chat to trigger keyboard commands on his computer, so I can change his scenes when he forgets.
I have removed information specific to his Twitch stream and my own "bot account", so this is ready to be edited by any who would like to use a twitch bot in a similar fashion.

Requires the twitchio and keyboard modules, and optionally requires pysimplegui.
The latter is only if you want a small window when packaging the program for use outside of a terminal, so users know the program is running.

Since PySimpleGUI uses a GNU GPLv3 License, I'm going to assume this will also require a GNU GPLv3 License.
If you use this and remove PySimpleGUI, twitchio and keyboard only use an MIT License, so you would be able to use that upon removal.
