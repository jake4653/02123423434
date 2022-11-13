import discord, time
import cloudscraper, requests
import random, threading
import asyncio
from discord import app_commands
from discord.ext import commands
from random import randint as tokenSearch
import bloxflip


bot = commands.Bot(command_prefix='.', intents= discord.Intents.all())


@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Streaming(name = "Semi gets u woman!", url = "https://www.twitch.tv/ttoppl"))
    print("Bot is up and ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} Command(s)")
    except Exception as e:
        print(e)
        
@bot.tree.command(name="free-mines")
@app_commands.checks.cooldown(1, 30, key = lambda i: (i.guild_id))
@app_commands.describe(serverhash = "enter your serverhash", mines = "enter your amount of mines")
async def mines(interaction: discord.Interaction, serverhash: str, mines: str):
    serverhash = str(serverhash)
    serverhash_length = len(serverhash)
    if serverhash_length < 64:
        await interaction.response.send_message(":x: Enter a real server hash monkey :x:")
    elif serverhash_length == 64:
      try:
        rfile = open("dataID.txt", "r")
      except:
        e = open("dataID.txt", "w")
        e.write("data")
        e.close()
        rfile = open("dataID.txt", "r")

      rid = rfile.read(64)
      if rid != serverhash:
        wfile = open("dataID.txt", "w")
        wfile.write(serverhash)
        wfile.close()
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:'
        a = tokenSearch(1, 8)
        b = tokenSearch(9, 13)
        c = tokenSearch(14, 17)
        d = tokenSearch(18, 25)
        if a == 1:
          mine1 = ":white_check_mark:"
        elif a == 2:
          mine2 = ":white_check_mark:"
        elif a == 3:
          mine3 = ":white_check_mark:"
        elif a == 4:
          mine4 = ":white_check_mark:"
        elif a == 5:
           mine5 = ":white_check_mark:"
        elif a == 6:
          mine6 = ":white_check_mark:"
        elif a == 7:
          mine7 = ":white_check_mark:"
        elif a == 8:
          mine8 = ":white_check_mark:"
        if b == 9:
          mine9 = ":white_check_mark:"
        elif b == 10:
          mine10 = ":white_check_mark:"
        elif b == 11:
          mine11 = ":white_check_mark:"
        elif b == 12:
          mine12 = ":white_check_mark:"
        elif b == 13:
          mine13 = ":white_check_mark:"
        if c == 14:
          mine14 = ":white_check_mark:"
        elif c == 15:
          mine15 = ":white_check_mark:"
        elif c == 16:
          mine16 = ":white_check_mark:"
        elif c == 17:
          mine17 = ":white_check_mark:"
        if d == 18:
          mine18 = ":white_check_mark:"
        elif d == 19:
          mine19 = ":white_check_mark:"
        elif d == 20:
          mine20 = ":white_check_mark:"
        elif d == 21:
          mine21 = ":white_check_mark:"
        elif d == 22:
          mine22 = ":white_check_mark:"
        elif d == 23:
          mine23 = ":white_check_mark:"
        elif d == 24:
          mine24 = ":white_check_mark:"
        elif d == 25:
          mine25 = ":white_check_mark:"
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        result = f"""
        Mines
        {row1}
        {row2}
        {row3}
        {row4}
        {row5}
        """
        gamedata = f"""
        Info
        ───────────────
        Mines: {mines}
        ───────────────
        :white_check_mark: is a predicted safe spot
        ───────────────
        :bomb: is where a bomb could be
        """
        dfile = open("dataRes.txt", "w")
        dfile.write(result)
        dfile.close()
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="")
        em.add_field(name="Free mines Semi predictor", value=result)
        em.add_field(name="Game Data", value=gamedata)
        await interaction.response.send_message(embed=em)
      elif serverhash == rid:
        dafile = open("dataRes.txt", "r")
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="")
        em.add_field(name="Why u using the same hash again???", value=dafile.read())
        await interaction.response.send_message(embed=em)
        dafile.close()
      rfile.close()


@bot.tree.command(name="premium-mines")
@discord.app_commands.checks.has_role("Buyer")
@app_commands.describe(serverhash = "enter your serverhash", mines = "enter your amount of mines")
async def mines(interaction: discord.Interaction, serverhash: str, mines: str):
    serverhash = str(serverhash)
    serverhash_length = len(serverhash)
    if serverhash_length < 64:
        await interaction.response.send_message(":x: Enter a real server hash monkey :x:")
    elif serverhash_length == 64:
      try:
        rfile = open("dataID.txt", "r")
      except:
        e = open("dataID.txt", "w")
        e.write("data")
        e.close()
        rfile = open("dataID.txt", "r")

      rid = rfile.read(64)
      if rid != serverhash:
        wfile = open("dataID.txt", "w")
        wfile.write(serverhash)
        wfile.close()
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:'
        a = tokenSearch(1, 8)
        b = tokenSearch(9, 13)
        c = tokenSearch(14, 17)
        d = tokenSearch(18, 25)
        e = tokenSearch(22, 25)
        
        a1 = tokenSearch(26, 33)
        b1 = tokenSearch(34, 38)
        c1 = tokenSearch(39, 42)

        a2 = tokenSearch(1, 12)
        b2 = tokenSearch(13, 25)
        
 

        # normal mines

        if a == 1:
          mine1 = ":white_check_mark:"
        elif a == 2:
          mine2 = ":white_check_mark:"
        elif a == 3:
          mine3 = ":white_check_mark:"
        elif a == 4:
          mine4 = ":white_check_mark:"
        elif a == 5:
           mine5 = ":white_check_mark:"
        elif a == 6:
          mine6 = ":white_check_mark:"
        elif a == 7:
          mine7 = ":white_check_mark:"
        elif a == 8:
          mine8 = ":white_check_mark:"
        if b == 9:
          mine9 = ":white_check_mark:"
        elif b == 10:
          mine10 = ":white_check_mark:"
        elif b == 11:
          mine11 = ":white_check_mark:"
        elif b == 12:
          mine12 = ":white_check_mark:"
        elif b == 13:
          mine13 = ":white_check_mark:"
        if c == 14:
          mine14 = ":white_check_mark:"
        elif c == 15:
          mine15 = ":white_check_mark:"
        elif c == 16:
          mine16 = ":white_check_mark:"
        elif c == 17:
          mine17 = ":white_check_mark:"
        if d == 18:
          mine18 = ":white_check_mark:"
        elif d == 19:
          mine19 = ":white_check_mark:"
        elif d == 20:
          mine20 = ":white_check_mark:"
        elif d == 21:
          mine21 = ":white_check_mark:"
        if e == 22:
          mine22 = ":white_check_mark:"
        elif e == 23:
          mine23 = ":white_check_mark:"
        elif e == 24:
          mine24 = ":white_check_mark:"
        elif e == 25:
          mine25 = ":white_check_mark:"


                # 50% mines

        if a2 == 1:
          mine1 = ":mag_right:"
        elif a2 == 2:
          mine2 = ":mag_right:"
        elif a2 == 3:
          mine3 = ":mag_right:"
        elif a2 == 4:
          mine4 = ":mag_right:"
        elif a2 == 5:
           mine5 = ":mag_right:"
        elif a2 == 6:
          mine6 = ":mag_right:"
        elif a2 == 7:
          mine7 = ":mag_right:"
        elif a2 == 8:
          mine8 = ":mag_right:"
        elif a2 == 10:
          mine10 = ":mag_right:"
        elif a2 == 11:
          mine11 = ":mag_right:"
        elif a2 == 12:
          mine12 = ":mag_right:"
        elif a2 == 13:
          mine12 = ":mag_right:"
        elif a2 == 14:
          mine12 = ":mag_right:"
        if b2 == 15:
          mine1 = ":mag_right:"
        if b2 == 16:
          mine1 = ":mag_right:"
        elif b2 == 17:
          mine2 = ":mag_right:"
        elif b2 == 18:
          mine3 = ":mag_right:"
        elif b2 == 19:
          mine4 = ":mag_right:"
        elif b2 == 20:
           mine5 = ":mag_right:"
        elif b2 == 21:
          mine6 = ":mag_right:"
        elif b2 == 22:
          mine7 = ":mag_right:"
        elif b2 == 23:
          mine8 = ":mag_right:"
        elif b2 == 24:
          mine10 = ":mag_right:"
        elif b2 == 23:
          mine11 = ":mag_right:"
        elif b2 == 24:
          mine12 = ":mag_right:"
        elif b2 == 25:
          mine12 = ":mag_right:"


        # grey mines

        if a1 == 26:
          mine1 = ":tangerine:"
        elif a1 == 27:
          mine2 = ":tangerine:"
        elif a1 == 28:
          mine3 = ":tangerine:"
        elif a1 == 29:
          mine4 = ":tangerine:"
        elif a1 == 30:
           mine5 = ":tangerine:"
        elif a1 == 31:
          mine6 = ":tangerine:"
        elif a1 == 32:
          mine7 = ":tangerine:"
        elif a1 == 33:
          mine8 = ":tangerine:"
        if b1 == 34:
          mine9 = ":tangerine:"
        elif b1 == 35:
          mine10 = ":tangerine:"
        elif b1 == 36:
          mine11 = ":tangerine:"
        elif b1 == 37:
          mine12 = ":tangerine:"
        elif b1 == 38:
          mine13 = ":tangerine:"
        if c1 == 39:
          mine14 = ":tangerine:"
        elif c1 == 40:
          mine15 = ":tangerine:"
        elif c1 == 41:
          mine16 = ":tangerine:"
        elif c1 == 42:
          mine17 = ":tangerine:"



        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        
        result = f"""
        Mines
        {row1}
        {row2}
        {row3}
        {row4}
        {row5}
        """

        gamedata = f"""
        Info
        ────────────────
        Mines: {mines}
        ────────────────
        :bomb: Is where a bomb could be not sure!
        ────────────────
        :tangerine: Is a common pattern of mines!
        ────────────────
        :white_check_mark: Is a spot where theres a higher chance of picking Robux!
        ────────────────
        :mag_right: Is a 50/50 prediction!
        """
        dfile = open("dataRes.txt", "w")
        dfile.write(result)
        dfile.close()
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="")
        em.add_field(name="Mines Semi predictor", value=result)
        em.add_field(name="Info", value=gamedata)
        await interaction.response.send_message(embed=em)
      elif serverhash == rid:
        dafile = open("dataRes.txt", "r")
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="")
        em.add_field(name="Why u using the same hash again???", value=dafile.read())
        await interaction.response.send_message(embed=em)
        dafile.close()
      rfile.close()


bot.run(token)
