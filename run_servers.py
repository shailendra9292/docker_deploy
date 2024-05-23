# run_servers.py
import subprocess
import time

# Function to run a command
def run_command(command):
    return subprocess.Popen(command, shell=True)

# Run FastAPI server
fastapi_command = "uvicorn app:app --host 0.0.0.0 --port 8000"
fastapi_process = run_command(fastapi_command)
print("FastAPI server started...")

# Delay to ensure FastAPI server starts before Streamlit
time.sleep(5)

# Run Streamlit app
streamlit_command = "streamlit run template.py"
streamlit_process = run_command(streamlit_command)
print("Streamlit app started...")

# Wait for both processes to complete
# fastapi_process.wait()
# streamlit_process.wait()
