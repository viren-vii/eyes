import asyncio
from browser_use import Agent

from eyes.core.agent import controller, llm, system_prompt


async def main():
    agent = Agent(task=system_prompt, llm=llm, controller=controller)
    result = await agent.run()
    print(result)


asyncio.run(main())
