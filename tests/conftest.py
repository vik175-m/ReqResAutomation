import pytest
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Define the fixture that provides the base URL
@pytest.fixture(scope="module")
def base_url():
    return "https://reqres.in/api"

