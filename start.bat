@echo off
cd C://Users/orbar/Desktop/zoom_survey_alert
start "" python ./zoom_poll_detector.py
timeout /t 5 /nobreak
start "" "https://idc-il.zoom.us/j/5283915830"

timeout /t 5 /nobreak

rem Focus the browser window
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.AppActivate('Google Chrome')"

timeout /t 2 /nobreak

rem Press the left arrow key
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('{LEFT}')"
timeout /t 5 /nobreak

rem Press the enter key
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('{ENTER}')"
timeout /t 5 /nobreak

rem Press the enter key again (to join the meeting)
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('{ENTER}')"
timeout /t 5 /nobreak

rem Press the enter key one more time
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('{ENTER}')"


@REM rem Combine all key presses into one PowerShell command
@REM powershell -command "
@REM     $wshell = New-Object -ComObject wscript.shell;
@REM     $wshell.AppActivate('Google Chrome');
@REM     Start-Sleep -Seconds 1;
@REM     $wshell.SendKeys('{LEFT}');
@REM     Start-Sleep -Seconds 5;
@REM     $wshell.SendKeys('{ENTER}');
@REM     Start-Sleep -Seconds 5;
@REM     $wshell.SendKeys('{ENTER}');
@REM     Start-Sleep -Seconds 5;
@REM     $wshell.SendKeys('{ENTER}');
@REM "
