from .. import Skill
import wolframalpha
import os
import asyncio

class SearchSkill(Skill):
    async def on_load(self):
        self.client = wolframalpha.Client(os.environ["ALPHA_KEY"])

    async def parse(self, message, question):
        res = await asyncio.get_event_loop().run_in_executor(None, self.client.query, message.clean_content)
        try:
            return "According to WolframAlpha:\n```"+next(res.results).text+"```"
        except:
            return "I asked Wolfram Alpha, but they returned no answers. Try rephrasing your question."
