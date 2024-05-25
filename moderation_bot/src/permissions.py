# permissions.py

# Importing necessary modules
import discord

# Class for handling permissions
class Permissions:
    def __init__(self, client):
        self.client = client

    # Function to check if a user has admin permissions
    async def check_admin_permissions(self, user):
        if user.guild_permissions.administrator:
            return True
        else:
            return False

    # Function to assign a role to a user
    async def assign_role(self, user, role_name):
        guild = user.guild
        role = discord.utils.get(guild.roles, name=role_name)
        if role:
            await user.add_roles(role)
            return f"Role {role_name} assigned successfully to {user.display_name}."
        else:
            return f"Role {role_name} not found."

    # Function to remove a role from a user
    async def remove_role(self, user, role_name):
        guild = user.guild
        role = discord.utils.get(guild.roles, name=role_name)
        if role:
            await user.remove_roles(role)
            return f"Role {role_name} removed successfully from {user.display_name}."
        else:
            return f"Role {role_name} not found."

    # Function to kick a user from the server
    async def kick_user(self, user):
        await user.kick()
        return f"{user.display_name} has been kicked from the server."

    # Function to ban a user from the server
    async def ban_user(self, user):
        await user.ban()
        return f"{user.display_name} has been banned from the server."