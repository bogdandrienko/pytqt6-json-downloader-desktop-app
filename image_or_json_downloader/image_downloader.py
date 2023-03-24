import asyncio
import datetime
import os
import shutil
import aiofiles
import aiohttp


def start(url: str, headers: dict):
    try:
        shutil.rmtree("image_or_json_downloader/images")
    except Exception as error:
        pass
    os.mkdir("image_or_json_downloader/images")

    async def download():
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers) as resp_object:
                response = await resp_object.read()
                async with aiofiles.open(
                        f'image_or_json_downloader/images/image1_{datetime.datetime.now().strftime("%H_%M")}.jpg',
                        mode='wb') as file:
                    await file.write(response)
    asyncio.run(download())


if __name__ == '__main__':
    pass
