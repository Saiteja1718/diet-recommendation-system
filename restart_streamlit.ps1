# Stop any running Streamlit processes
Get-Process | Where-Object {$_.ProcessName -eq "streamlit"} | Stop-Process -Force

# Wait a moment
Start-Sleep -Seconds 2

# Navigate to Streamlit_Frontend directory and start Streamlit
Set-Location -Path "Streamlit_Frontend"
python -m streamlit run Hello.py --server.port 8501
