Write-Host "Creating python virtual environment" -ForegroundColor red -BackgroundColor white
python -m venv .\venv

Write-Host "Activating python virtual environment" -ForegroundColor red -BackgroundColor white
.\

Write-Host 'Installing all requirements for the app' -ForegroundColor red -BackgroundColor white
pip install -r .\SQLLAAMA\requirements.txt

Write-Host 'Running app' -ForegroundColor red -BackgroundColor white
gradio .\SQLLAAMA\app.py