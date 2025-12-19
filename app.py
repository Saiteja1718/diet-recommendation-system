"""
Hugging Face Spaces entry point for Diet Recommendation System.
This file launches the Streamlit app from the Streamlit_Frontend directory.
"""

import os
import sys
from pathlib import Path

# Add Streamlit_Frontend to Python path
frontend_path = Path(__file__).parent / "Streamlit_Frontend"
sys.path.insert(0, str(frontend_path))

# Change to Streamlit_Frontend directory
os.chdir(frontend_path)

# Import and run the Streamlit app
if __name__ == "__main__":
    import streamlit.web.cli as stcli
    import sys
    
    sys.argv = [
        "streamlit",
        "run",
        "Hello.py",
        "--server.port=7860",
        "--server.address=0.0.0.0",
        "--server.headless=true"
    ]
    
    sys.exit(stcli.main())
