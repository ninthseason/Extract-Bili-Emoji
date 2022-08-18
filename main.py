import asyncio
import re
import httpx
import pathlib

# 修改这里
dom = ''''''

urls = ["https:" +
        i for i in re.findall(r"//i0.hdslb.com/bfs/emote/.*?.png", dom)]
download_folder = pathlib.Path(__file__).with_name("emojis")
if not (download_folder.exists() and download_folder.is_dir()):
    download_folder.mkdir()
headers = {
    'authority': 'i0.hdslb.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}


async def download(url: str, ids: int) -> None:
    save_name: str = str(ids) + '.png'
    complete_path: str = str(download_folder) + "/" + save_name
    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers)
        with open(complete_path, "wb") as f:
            f.write(res.content)


async def main() -> None:
    tasks = []
    for ids, url in enumerate(urls):
        tmp = asyncio.create_task(download(url, ids))
        tasks.append(tmp)
    await asyncio.wait(tasks)


asyncio.run(main())
