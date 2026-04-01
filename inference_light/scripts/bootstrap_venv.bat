@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."
pushd "%PROJECT_ROOT%"

if not exist ".venv\Scripts\python.exe" (
  py -3 -m venv .venv
  if errorlevel 1 (
    python -m venv .venv
    if errorlevel 1 (
      echo Failed to create virtual environment.
      popd
      exit /b 1
    )
  )
)

".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 (
  echo Failed to upgrade pip.
  popd
  exit /b 1
)

".venv\Scripts\python.exe" -m pip install -r requirements-windows.lock
if errorlevel 1 (
  echo Failed to install dependencies.
  popd
  exit /b 1
)

echo Virtual environment ready at %PROJECT_ROOT%\.venv
popd
exit /b 0

