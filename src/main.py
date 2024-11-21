import os

# Start FastAPI server
# os.system("uvicorn server:app --reload --port 8000")
# os.system("uvicorn server:app --reload --port 8000 --workers 4")

# Start Streamlit app
# os.system("streamlit run app.py")
print('reaching streamlit')
# os.system("streamlit run app.py --server.port 8505")
# lines below help us run multiple clients at the same time
import subprocess
command_0 = ["uvicorn", "src.server:app", "--reload", "--port", "8000"]
# Command to run the first Streamlit instance on port 8501
command_1 = ["streamlit", "run", "src/app.py", "--server.port", "8501"]
# Command to run the second Streamlit instance on port 8502
command_2 = ["streamlit", "run", "src/app.py", "--server.port", "8502"]
# Start both Streamlit instances as separate processes
process_0 = subprocess.Popen(command_0)
process_1 = subprocess.Popen(command_1)
process_2 = subprocess.Popen(command_2)
# Optional: Wait for both processes to complete (will keep main.py running)
process_0.wait()
process_1.wait()
process_2.wait()
