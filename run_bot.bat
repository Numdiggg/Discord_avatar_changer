@echo off
title Discord Bot Avatar Changer

echo Installing discord.py...
pip install discord.py==1.7.3
pip install colorama

if %errorlevel% neq 0 (
    echo ^[[91mFailed to install discord.py. Exiting.^[[0m
    exit /b %errorlevel%
)

echo ^[[92mdiscord.py installed successfully.^[[0m
echo.

python Avtar_changer.py

echo.
echo Press any key to exit...
pause >nul
