import os.path
from urllib.request import Request, urlopen


class ProductService:
    def download_img(self, url: str):
        site_url = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(site_url) as web_file:
            img_data = web_file.read()

        if not img_data:
            raise ValueError(f"Error: cannot load the image from {url}")

        file_name = os.path.basename(url)
        with open(file_name, "wb") as f:
            f.write(img_data)

        return f"Download image successfully, {file_name}"
