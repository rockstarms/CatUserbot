import os
import sys
import asyncio
from telethon import events
from userbot.utils import admin_cmd

@borg.on(admin_cmd("bigoof"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    await event.edit("┏━━━┓╋╋╋╋┏━━━┓ \n┃┏━┓┃╋╋╋╋┃┏━┓┃ \n┃┃╋┃┣┓┏┓┏┫┃╋┃┃ \n┃┃╋┃┃┗┛┗┛┃┃╋┃┃ \n┃┗━┛┣┓┏┓┏┫┗━┛┃ \n┗━━━┛┗┛┗┛┗━━━┛")
    animation_chars = [
            "╭━━━╮╱╱╱╭━╮ \n┃╭━╮┃╱╱╱┃╭╯ \n┃┃╱┃┣━━┳╯╰╮ \n┃┃╱┃┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃┃┃ \n╰━━━┻━━╯╰╯ ",
            "╭━━━╮╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃┃┃ \n ╰━━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯"
         ]
          
    for i in animation_ttl:        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 36])

@borg.on(admin_cmd(pattern="g1 ?(.*)"))
async def payf(event):
    paytext=event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1)
    await event.edit(pay)

@borg.on(admin_cmd(pattern="uff ?(.*)"))      
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1    
    animation_ttl = range(0, 13)    
    animation_chars = [
            "U",
            "Uf",    
            "Uff",
            "Ufffff",
            "Uffffff",
            "Ufffffff",
            "Uffffffff",
            "Ufffffffff",
            "Uffffffffff",    
            "Ufffffffffff",
            "Uffffffffffff",
            "Ufffffffffffff",
            "Uffffffffffffff"
        ]
    for i in animation_ttl:        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])

@borg.on(admin_cmd(pattern="ctext ?(.*)"))
async def payf(event):
    paytext=event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2, paytext*8, paytext*8)
    await event.edit(pay)
      
@borg.on(admin_cmd(pattern="ftext ?(.*)"))
async def payf(event):
    paytext=event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*6, paytext*6, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2)
    await event.edit(pay)      
