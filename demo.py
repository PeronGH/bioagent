import asyncio
import uuid
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from dotenv import load_dotenv
from single_agent import root_agent

load_dotenv()

session_service = InMemorySessionService()

runner = Runner(agent=root_agent, app_name="BioAgent", session_service=session_service)


async def main():
    pmid = input("Enter a PMID: ").strip()
    query = f"Begin by fetching the full text for the provided PMID: {pmid}"
    user_id = "tester"
    session_id = str(uuid.uuid4())

    await session_service.create_session(
        app_name=runner.app_name, user_id=user_id, session_id=session_id
    )
    print(f"ℹ️ Session created with ID: {session_id}")

    async for event in runner.run_async(
        new_message=types.Content(role="user", parts=[types.Part(text=query)]),
        user_id=user_id,
        session_id=session_id,
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(f"🤖 {part.text.strip()}")
                if part.function_call:
                    if part.function_call.name == "submit_error":
                        print(f"🔴 {part.function_call.args}")
                        break
                    if part.function_call.name == "submit_success":
                        print(f"🟢 {part.function_call.args}")
                        break
                    print(f"🛠️ {part.function_call.name}")
        if event.is_final_response():
            break


if __name__ == "__main__":
    asyncio.run(main())
