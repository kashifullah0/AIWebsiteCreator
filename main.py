import os
import asyncio
from dotenv import load_dotenv
import streamlit as st
from agents import Runner, Agent, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
st.title("AI Web Designer Create website by one line of Prompt")

load_dotenv()
api = os.getenv("GOOGLE_API_KEY")

external_client = AsyncOpenAI(
    api_key=api,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name="Frontend Expert",
    instructions="You are a frontend expert. You will give me only one file of code where HTML, CSS, and JS are included. No explanation, only code. direct start coding, do not any comment or text"
)

prompt = st.text_area("Prompt:")

if st.button("Run"):
    if prompt:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        result = Runner.run_sync(
            agent,
            input=prompt,
            run_config=config
        )

        with open("preview.html", "w") as f:
            f.write(result.final_output)

        st.success("Code Generated!")

if st.button("Show Preview"):
    import webbrowser
    webbrowser.open("preview.html")
