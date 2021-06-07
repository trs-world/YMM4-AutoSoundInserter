if not "%X_MIMIMIZED%"=="1" (
    set X_MIMIMIZED=1
    start /min cmd /c,"%~0" %*
    exit
)

CALL setPath.bat
cd../
python3 venv/Scripts/activate
python ymm.py %VOICE_PATH%