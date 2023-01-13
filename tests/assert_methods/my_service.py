class MyService:
    def download_img(self, url: str) -> bool:
        if url:
            return True

        raise ValueError("url is not valid")
