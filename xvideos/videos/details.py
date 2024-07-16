from .base import VideoDetailsScraper

import re
from functools import wraps

def validate_video_url(func):
    @wraps(func)
    def wrapper(self, video_url, *args, **kwargs):
        pattern = re.compile(r'^https://(www\.)?xvideos\.com/video.[a-zA-Z0-9._-]+/.+')
        if not pattern.match(video_url):
            raise ValueError(f"Invalid video URL: {video_url}")
        return func(self, video_url, *args, **kwargs)
    return wrapper


class DetailsScraper(VideoDetailsScraper):
    @validate_video_url
    def details(self, video_url: str) -> str:
        return self.scrape(video_url)
    @validate_video_url
    def download_high_quality(self, video_url: str, filename: str):
        video_details = self.scrape(video_url)
        high_url = video_details.get('files', {}).get('high')
        if high_url:
            return self.download_high(high_url, filename)
    @validate_video_url
    def download_low_quality(self, video_url: str, filename: str):
        video_details = self.scrape(video_url)
        low_url = video_details.get('files', {}).get('low')
        if low_url:
            return self.download_low(low_url, filename)