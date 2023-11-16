root=$(pwd)

# exit script when an error is detected
set -o errexit

# installation
python3 -m venv venv
ln -s venv/bin/activate .

. ./activate

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# post-installation message
echo "
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
pyOKX install.sh complete.

Run '. activate' to activate pyOKX's Python virtual environment and
'deactivate' to, well, deactivate it.

Refer to EXAMPLE.py on how to actually use the API endpoints.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"