# ReqRes API Automation Project

This project is an API automation framework designed to test the APIs of [ReqRes](https://reqres.in) using Python and PyTest. The framework covers various test scenarios including authentication basic and oAuth, API failure Scenarios, and general API testing along with CRUD operation.

## Getting Started

### Prerequisites

- Python latest installed
- A virtual environment (recommended)
- Install required dependencies listed in `requirements.txt`

  pip install -r requirements.txt

  

**To execute all tests, use the following command:**

  pytest
  

## Test Scenarios Covered   


   ### Authentication Testing
   - OAuth token tests (valid, expired, missing)
   - Simulated Basic Auth tests 
  ### API Failure Scenarios:
   - 500 Internal Server Error simulation         
   - Network timeout          
   - 404 Not Found errors  
  ### General API Testing:
   - User functionalities using the ReqRes API        
   - CRUD Operation
    

### License
This project is open-source and available under the MIT License.

