from .base import VideoDetailsScraper

class DetailsScraper(VideoDetailsScraper):
    def details(self, video_url: str) -> str:
        return self.scrape(video_url)
    def download_high_quality(self, video_url: str, filename: str):
        video_details = self.scrape(video_url)
        high_url = video_details.get('files', {}).get('high')
        if high_url:
            return self.download_high(high_url, filename)

    def download_low_quality(self, video_url: str, filename: str):
        video_details = self.scrape(video_url)
        low_url = video_details.get('files', {}).get('low')
        if low_url:
            return self.download_low(low_url, filename)