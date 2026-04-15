@echo off
setlocal enabledelayedexpansion

set FOLDER=C:\Users\Vanya\Downloads\Telegram Desktop

for /f "delims=" %%f in ('dir "%FOLDER%\label*.zpl" /b /o:-d') do (
    set FILE=%%f
    goto found
)

:found
if defined FILE if exist "%FOLDER%\!FILE!" (
    copy /b "%FOLDER%\!FILE!" "\\localhost\Gainscha_GS-2408D"
) else (
    echo File not found
)