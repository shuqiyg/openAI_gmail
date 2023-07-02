import openai
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

function_descriptions = [
    {
        "name": "extract_info_from_email",
        "description": "categorise & extract key info from an email, such as use case, company name, contact details, etc.",
        "parameters": {
            "type": "object",
            "properties": {
                "senderName": {
                    "type": "string",
                    "description": "the name of the sender that sent the email"
                },
                "priority": {
                    "type": "string",
                    "description": "Try to give a priority score to this email based on how likely this email will leads to a good job opportunity, from 0 to 10; 10 most important"
                },
                "category": {
                    "type": "string",
                    "description": "Try to categorize this email into categories like those: 1. Advertisement; 2. Job; 3. Newsletter ; 4. Personal; 5. Junk; 6. Spam; 7. Others; 8, Work"
                },
                "summary": {
                    "type": "string",
                    "description": "Try to summarize the content of the email"
                },
                "response": {
                    "type": "string",
                    "description": "Does it sound like the sender require a response to this email"
                },
                "nextStep": {
                    "type": "string",
                    "description": "What is the suggested next step or action to move forward regarding this email?"
                }
            },
            "required": ["senderName", "priority", "category", "summary", "response", "nextStep"]
        }
    }
]


class Email(BaseModel):
    from_email: str
    content: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/sq")
def sq():
    return {"sqResponse": "what's up?"}

@app.post("/")
def analyse_email(email: Email):
    content = email.content
    query = f"Please extract key information from this email: {content}"

    messages = [{"role": "user", "content": query}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=function_descriptions,
        function_call="auto"
    )

    arguments = response.choices[0]["message"]["function_call"]["arguments"]
    senderName = eval(arguments).get("senderName")
    priority = eval(arguments).get("priority")
    category = eval(arguments).get("category")
    summary = eval(arguments).get("summary")
    response = eval(arguments).get("response")
    nextStep = eval(arguments).get("nextStep")

    return {
        "senderName": senderName,
        "priority": priority,
        "category": category,
        "summary": summary,
        "response": response,
        "nextStep": nextStep
    }

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
