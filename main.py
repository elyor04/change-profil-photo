"""pip install Pyrogram opencv-contrib-python"""
from pyrogram import Client
from time import time, sleep, localtime, strftime
from cv2 import getTextSize, putText, imwrite, FONT_HERSHEY_COMPLEX
from numpy import zeros
from pathlib import Path
from sys import argv

WORK_DIR = Path(argv[0]).parent / "data"
WORK_DIR.mkdir(exist_ok=True)

apiId = ...
apiHash = ...

app = Client("myAccount", apiId, apiHash, workdir=WORK_DIR)
photos = []


async def changePhoto() -> None:
    global photos
    strTime = strftime("%H:%M", localtime())
    img = zeros((500, 500, 3), "uint8")
    gts = getTextSize(strTime, FONT_HERSHEY_COMPLEX, 3.0, 3)
    x = (img.shape[1] - gts[0][0]) // 2
    y = (img.shape[0] + gts[0][1]) // 2
    putText(img, strTime, (x, y), FONT_HERSHEY_COMPLEX, 3.0, (0, 255, 0), 3)
    imwrite(str(WORK_DIR / "surat.jpg"), img)
    if photos:
        await app.delete_profile_photos(photos[0].file_id)
    await app.set_profile_photo(photo=WORK_DIR / "surat.jpg")
    photos = [p async for p in app.get_chat_photos("me")]


async def main() -> None:
    await app.start()
    while True:
        _tm = time() // 60
        await changePhoto()
        while (time() // 60) == _tm:
            sleep(0.005)


app.run(main())
