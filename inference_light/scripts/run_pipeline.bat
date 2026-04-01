@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."
pushd "%PROJECT_ROOT%"

if not exist ".venv\Scripts\python.exe" (
  echo Missing .venv. Run scripts\bootstrap_venv.bat first.
  popd
  exit /b 1
)

set "PYTHONPATH=%PROJECT_ROOT%\src"
".venv\Scripts\python.exe" -m uninet_inference.cli --root "%PROJECT_ROOT%" %*
set "EXIT_CODE=%ERRORLEVEL%"

popd
exit /b %EXIT_CODE%

