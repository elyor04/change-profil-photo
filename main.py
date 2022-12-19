"""pip3 install Pyrogram opencv-contrib-python"""

from pyrogram import Client
from time import time, sleep, gmtime, strftime
from cv2 import getTextSize, putText, imwrite, FONT_HERSHEY_COMPLEX
from numpy import zeros

apiId = 10902934
apiHash = "e84c6544e9fbe2555fb220db78ad512f"
app = Client("myAccount", apiId, apiHash)


async def main() -> None:
    photos = []
    await app.start()
    while True:
        tm = time()
        sTm = strftime("%H:%M", gmtime(tm + (5 * 3600)))
        tm //= 60

        img = zeros((500, 500, 3), "uint8")
        gts = getTextSize(sTm, FONT_HERSHEY_COMPLEX, 3.0, 3)
        x = (img.shape[1] - gts[0][0]) // 2
        y = (img.shape[0] + gts[0][1]) // 2
        putText(img, sTm, (x, y), FONT_HERSHEY_COMPLEX, 3.0, (0, 255, 0), 3)
        imwrite("surat.jpg", img)

        if photos:
            await app.delete_profile_photos(photos[0].file_id)
        await app.set_profile_photo(photo="surat.jpg")
        photos = [p async for p in app.get_chat_photos("me")]

        while (time() // 60) == tm:
            sleep(0.005)


app.run(main())
