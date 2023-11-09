@echo off

set root=%cd%

:: installation

python -m venv venv
:: Windows doesn't allow the creation of symlinks without special priviledges, so hardlinks are created instead.
mklink /h activate.bat venv\Scripts\activate.bat

call activate.bat

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

:: post-installation message

echo @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
echo.
echo pyOKX install complete.
echo.
echo Run 'activate' to activate pyOKX 's Python virtual environment and
echo 'deactivate' to, well, deactivate it.
echo.
echo Refer to EXAMPLE.py on how to actually use the API endpoints.
echo.
echo @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

pause

deactivate