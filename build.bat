@echo off
@RD /S /Q "C:\Users\outro\Documents\valorant-ingame-twitch-chat\dist"
@RD /S /Q "C:\Users\outro\Documents\valorant-ingame-twitch-chat\build"
python -m build
python -m twine upload dist/*
pause