# 2024 GKO - Machine Learning Hackathon

## 🎯 Task Description 
Welcome to the **2024 GKO Machine Learning Hackathon**! In this event, your team will create a solution to
generate an OpenAPI 3.0 yaml schema from API traffic. Your solution should output the [Swagger Petstore](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)
schema based on a set of API hits / traffic of your design.

This task can be tackled in many different ways. One approach is to use ML to infer parameters in API traffic hits. 
The data that could prove to be useful for this task can be accessed [HERE](https://drive.google.com/file/d/1feKpIiJY-_IbeDYUvtrpRPcHHsrgc9t2) or via the command
```bash
curl -s -L "https://drive.google.com/uc?confirm=t&export=download&id=1feKpIiJY-_IbeDYUvtrpRPcHHsrgc9t2" -o "./endpoints_inference.csv"
```
You can use [pandas](https://pandas.pydata.org/docs/user_guide/10min.html) to load and manipulate the data.

## 🚀 Getting started 
For this project, you are given access to GPT 3.5 api. Feel free to use it for this project while keeping in mind its 
[pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/) 
(say you get 1M api hits in your schema generation service. How much would it cost?)

Furthermore, a basic reverse proxy app has been prepared for you. Use at will.

### 🐍 Setup Python
First, you need to install Python (recommended Python >= 3.8) and create a virtual environment. Once this is done run

```bash
pip install -r requirements.txt
```
to install the project requirements. Feel free to update those as necessary.

### 🌳 Download .env
Download file [HERE](https://drive.google.com/file/d/1zDrxOh4p-lQtjpDITZmMfFJcbrwedohh/view).
Note that the file must be named ".env" and placed in the repository root for the code to work.

### 🏃‍♀️ Run
To run the chatgpt model:
```bash
python run_chatgpt.py --config "chatgpt_001.json" --message "how big is the earth?"
```
Model response:
```text
The Earth has a diameter of approximately 12,742 kilometers (7,918 miles)...
```

To run the reverse proxy `app.py`

```bash
python app.py
```
This runs the app at http://127.0.0.1:5000 by default and redirects to the `PROXY__API_HOST` defined in ".env" file.

## ✅ Results
The result should be an OpenAPI 3.0 yaml schema of [Swagger Petstore](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml) with as much information as possible 😊

## 💥 Have Fun!
The primary goal for the hackathon is to learn and have fun. Don't hesitate to reach out if you have any questions or 
need assistance.

Good luck!
