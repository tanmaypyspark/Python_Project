@echo off
set TFLITE_DISABLE_XNNPACK=1
"%~dp0clean_env\Scripts\python.exe" -B "%~dp0wrapperWebScrap.py"
pause