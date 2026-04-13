from pydantic_ai import Agent
from dotenv import load_dotenv
from constants import MODEL_SMALL, MODEL_MEDIUM, MODEL_LARGE
from data_models import ChatRequest, ChatResponse

# overrides eventual caching of environment variables so that we always use env variable from .env
load_dotenv(override=True)

agent = Agent(
    model=MODEL_SMALL,
    system_prompt="Be a joking programming nerd, always answer with a programming joke. Also add in some emojis to make it funnier.",
    retries=1,
)


async def chat(request: ChatRequest):
    result = await agent.run(request.question, message_history=request.message_history)

    return ChatResponse(response=result.output, message_history=result.all_messages())
