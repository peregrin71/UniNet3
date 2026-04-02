@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."
pushd "%PROJECT_ROOT%"

call "%SCRIPT_DIR%preprocess_real_data.bat" --enable-datasets --disable-other-datasets --dataset-id cmb_planck_compressed_pr3 --dataset-id rsd_desi_dr1_fsigma8 --dataset-id wl_kids1000_s8
if errorlevel 1 (
  popd
  exit /b 1
)

call "%SCRIPT_DIR%run_pipeline.bat" %*
set "EXIT_CODE=%ERRORLEVEL%"

popd
exit /b %EXIT_CODE%
