# FastAPI Spam Detector Microservice

## What This Project Does

This project is a REST API microservice built with FastAPI that detects whether an email or text message is spam or not. It uses a pre-trained machine learning model and NLP preprocessing with NLTK to classify input texts. The service exposes an endpoint to accept text and returns a spam prediction.

**Input:** Email or text message (string)

**Output:** Spam or Not Spam (classification result)

---

## How to Run

### 1. Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/sanjib7777/fastapi-spam-detector.git
   cd fastapi-spam-detector
   
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv myenv
   myenv/bin/activate  # On Windows 

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the API Server
   ```bash
   uvicorn main:app --reload
5. Test the API:  Open http://127.0.0.1:8000/docs in your browser to access the Swagger UI and try the /api/v1/predict endpoint.


### 2.Run Using Docker

1. Build the Docker image:

   ```bash
   docker build -t fastapi-spam-detector .

   
2. Run the container:

   ```bash
   docker run -d -p 8000:8000 fastapi-spam-detector
3. Access the API at:
  ```bash
  http://localhost:8000/docs
```
Or
```bash
docker pull sanjib7777/fastapi-spam-detector:latest
docker run -p 8000:8000 sanjib7777/fastapi-spam-detector:latest
```
## How to Test
1. Run automated tests with:
```bash
pytest
```
  OR

2. To run it specifically:
```bash
pytest test/test_predict.py
```
## Configuration and Setup Notes

- **Environment Variables:**  
  The app uses environment variables to configure paths and settings. You can manage these using a `.env` file or directly set them in your environment.

- **NLTK Data:**  
  The app relies on NLTK resources such as `punkt` and `stopwords`. These are downloaded automatically during the CI workflow. If running locally for the first time, you may need to manually download them by running:  
  ```bash
  python -m nltk.downloader punkt stopwords
  ```



  
