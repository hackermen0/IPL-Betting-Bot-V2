from discord.ui import Button
from discord import ButtonStyle


class donationButton(Button):

    def __init__(self):

        self.value = True


        super().__init__(style= ButtonStyle.link, label = "Donate", disabled = False, url = "https://ipl-betting-bot-website.vercel.app/#donate", row = 2)

