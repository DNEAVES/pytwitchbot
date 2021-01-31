# pytwitchbot
A Twitch chatbot made with Python. Chat commands from approved users can trigger keyboard shortcuts on the streamer's side.

A hollow python twitch bot.
I made it for a friend of mine so I could use Twitch chat to trigger keyboard commands on his computer, so I can change his OBS scenes when he forgets.
I have removed information specific to his Twitch stream and my own "bot account", so this is ready to be edited by any who would like to use a twitch bot in a similar fashion.

Requires the [twitchio](https://github.com/TwitchIO/TwitchIO) and [keyboard](https://github.com/boppreh/keyboard) modules, and optionally requires [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI).
The latter is only if you want a small window when packaging the program for use outside of a terminal, so users know the program is running.
If you don't want to create a window via PySimpleGUI, just remove the import at the top and the "small window" section at the bottom of the python script.

Since PySimpleGUI uses a GNU GPLv3 License, I'm going to assume this will also require a GNU GPLv3 License. Otherwise twitchio and keyboard only require MIT.

Some probably-needed legal things for this: This project isn't affiliated with, nor endorsed by, Twitch.
