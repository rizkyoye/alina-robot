import os
from JisooX.events import register
from JisooX import OWNER_ID
from JisooX import telethn as tbot
from PIL import Image, ImageDraw, ImageFont


@register(pattern="^/logo ?(.*)")
async def lego(event):
 xnxx = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not xnxx:
      xnxx = await event.reply('Provide Some Text To Draw!')
      
    try:
    await xnxx.reply('Creating your logo...wait!')
    img = Image.open('./JisooX/resources/951b8baf6839dccee3bbd7ab16b23813.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./JisooX/resources/4.ttf", 40)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "LogoByZen.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By Zenwisteria")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @Rorflame, {e}')


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__help__ = """
 ❍ /logo text :  Create your logo with your name
 """
__mod_name__ = "Logo"