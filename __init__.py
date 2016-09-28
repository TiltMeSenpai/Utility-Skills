from .. import Skill
import wolframalpha
import os

class SearchSkill(Skill):
    async def on_load(self):
        self.client = wolframalpha.Client(os.environ["ALPHA_KEY"])

    async def parse(self, message, question, phrase, conjunction=""):
        res = await asyncio.get_event_loop().run_in_executor(None, self.client.query, phrase)
        return "According to WolframAlpha:\n```"+next(res.results).text+"```"
