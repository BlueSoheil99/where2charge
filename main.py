import os

# Start FastAPI server
os.system("uvicorn server:app --reload --port 8000")
# os.system("uvicorn server:app --reload --port 8000 --workers 4")

# Start Streamlit app
# os.system("streamlit run app.py")
# os.system("streamlit run app.py --server.port 8502")
# lines below help us run multiple clients at the same time
import subprocess
# Command to run the first Streamlit instance on port 8501
command_1 = ["streamlit", "run", "app.py", "--server.port", "8501"]
# Command to run the second Streamlit instance on port 8502
command_2 = ["streamlit", "run", "app.py", "--server.port", "8502"]
# Start both Streamlit instances as separate processes
process_1 = subprocess.Popen(command_1)
process_2 = subprocess.Popen(command_2)
# Optional: Wait for both processes to complete (will keep main.py running)
process_1.wait()
process_2.wait()
