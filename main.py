from fastapi import FastAPI, Request
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
import os

app = FastAPI()

# On met des valeurs vides pour l’instant (on ajoutera App ID + password plus tard)
settings = BotFrameworkAdapterSettings("", "")
adapter = BotFrameworkAdapter(settings)

@app.post("/api/messages")
async def messages(req: Request):
    body = await req.json()
    activity = Activity().deserialize(body)

    async def logic(turn_context: TurnContext):
        # Réponse simple
        user_message = turn_context.activity.text.strip().lower()
        await turn_context.send_activity(f"Tu as dit : '{user_message}' 👋")

    await adapter.process_activity(activity, "", logic)
    return "ok"
