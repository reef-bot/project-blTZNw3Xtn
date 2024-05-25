# bot.py

import discord
from discord.ext import commands

class ModerationBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        self.filtering = Filtering()
        self.tracking = Tracking()
        self.commands = Commands()
        self.permissions = Permissions()
        self.dashboard = Dashboard()
        self.logs = Logs()

        # Event to handle message filtering
        @commands.Cog.listener()
        async def on_message(self, message):
            if not message.author.bot:
                if await self.filtering.check_message(message):
                    await message.delete()
                    await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")

        # Command to warn a user
        @commands.command()
        async def warn(self, ctx, user: discord.Member):
            await self.tracking.warn_user(user)
            await ctx.send(f"{user.mention} has been warned for their behavior.")

        # Command to kick a user
        @commands.command()
        async def kick(self, ctx, user: discord.Member, *, reason="No reason provided."):
            await self.permissions.check_permission(ctx.author, "kick")
            await user.kick(reason=reason)
            await ctx.send(f"{user.mention} has been kicked from the server.")

        # Command to ban a user
        @commands.command()
        async def ban(self, ctx, user: discord.Member, *, reason="No reason provided."):
            await self.permissions.check_permission(ctx.author, "ban")
            await user.ban(reason=reason)
            await ctx.send(f"{user.mention} has been banned from the server.")

        # Command to view moderation logs
        @commands.command()
        async def logs(self, ctx):
            logs = await self.logs.get_logs()
            await ctx.send(logs)

# Create an instance of the bot
bot = ModerationBot(command_prefix="!")

# Add the Cogs to the bot
bot.add_cog(Filtering())
bot.add_cog(Tracking())
bot.add_cog(Commands())
bot.add_cog(Permissions())
bot.add_cog(Dashboard())
bot.add_cog(Logs())

# Run the bot
bot.run("YOUR_DISCORD_BOT_TOKEN")