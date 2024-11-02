from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model2 import Summ_Model

model = Summ_Model("./model2")

app = FastAPI()

# это для общения вьюшки и фастапи
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def process_short(user_message) -> str:
    return model.predict(user_message, 0)

def process_long(user_message) -> str:
    return model.predict(user_message, 1)

@app.post("/api/chat")
async def chat(message: dict):
    user_message = message.get("text", "")
    compression_level = message.get("compression", "normal")
    if compression_level == "high":
        ai_response = process_short(user_message)
    else:
        ai_response = process_long(user_message)  # передаем user_message в process_long

    return {"response": ai_response}
