from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re
import requests
import os
class VideoDetailsScraper:
    def __init__(self):
        self.puppeteer_config = {
            'headless': True, 
            'slow_mo': 50,     
            'args': ['--no-sandbox', '--disable-setuid-sandbox']
        }

    def get_meta(self, soup):
        title = soup.find('meta', property='og:title')['content']
        duration = soup.find('meta', property='og:duration')['content']
        image = soup.find('meta', property='og:image')['content']
        video_type = soup.find('meta', property='og:type')['content']
        description_meta = soup.find('meta', attrs={'name': 'description'})
        description = description_meta['content'] if description_meta else None
        return title, duration, image, video_type, description

    def get_views(self, soup):
        views_element = soup.select_one('#v-views strong.mobile-hide')
        views = views_element.get_text(strip=True) if views_element else None
        return views

    def get_likes(self, soup):
        like_percentage_element = soup.select_one('.vote-action-good .rating-good-perc')
        like_percentage = like_percentage_element.get_text(strip=True) if like_percentage_element else None
        dislike_percentage_element = soup.select_one('.vote-action-bad .rating-bad-perc')
        dislike_percentage = dislike_percentage_element.get_text(strip=True) if dislike_percentage_element else None
        return like_percentage, dislike_percentage

    def get_comments(self, soup):
        comments_button = soup.select_one('.comments .badge')
        comments_count = comments_button.get_text(strip=True) if comments_button else None
        return comments_count

    def get_files(self, soup):
        video_script = soup.select_one('#video-player-bg > script:nth-child(6)').string
        files = {
            'low': self.extract_file_url(video_script, 'html5player.setVideoUrlLow\\(\'(.*?)\'\\);'),
            'high': self.extract_file_url(video_script, 'html5player.setVideoUrlHigh\\(\'(.*?)\'\\);'),
            'HLS': self.extract_file_url(video_script, 'html5player.setVideoHLS\\(\'(.*?)\'\\);'),
            'thumb': self.extract_file_url(video_script, 'html5player.setThumbUrl\\(\'(.*?)\'\\);'),
            'thumb69': self.extract_file_url(video_script, 'html5player.setThumbUrl169\\(\'(.*?)\'\\);'),
            'thumbSlide': self.extract_file_url(video_script, 'html5player.setThumbSlide\\(\'(.*?)\'\\);'),
            'thumbSlideBig': self.extract_file_url(video_script, 'html5player.setThumbSlideBig\\(\'(.*?)\'\\);'),
        }
        return files

    def get_models(self, soup):
        models = soup.select('.model')
        model_data = []
        for model in models:
            model_link = model.select_one('a')['href']
            model_name = model.select_one('.name').text
            model_id = model.select_one('a')['data-id']
            model_data.append({
                'name': model_name,
                'profile_url': model_link,
                'id': model_id
            })
        return model_data

    def get_tags(self, soup):
        tags = soup.select('.is-keyword')
        tag_list = [tag.text for tag in tags]
        return tag_list

    def scrape(self, url: str) -> dict:
        with sync_playwright() as p:
            browser = p.chromium.launch(**self.puppeteer_config)
            page = browser.new_page()
            page.goto(url, wait_until='networkidle')
            html = page.content()
            soup = BeautifulSoup(html, 'html.parser')
            browser.close()
            
            title, duration, image, video_type, description = self.get_meta(soup)
            views = self.get_views(soup)
            like_percentage, dislike_percentage = self.get_likes(soup)
            comments_count = self.get_comments(soup)
            files = self.get_files(soup)
            model_data = self.get_models(soup)
            tag_list = self.get_tags(soup)

            return {
                'title': title,
                'url': url,
                'duration': duration,
                'image': image,
                'views': views,
                'videoType': video_type,
                'description': description,
                'files': files,
                'models': model_data,
                'tags': tag_list,
                'likePercentage': like_percentage,
                'dislikePercentage': dislike_percentage,
                'commentsCount': comments_count,
            }

    def extract_file_url(self, script_content: str, pattern: str) -> str:
        match = re.search(pattern, script_content)
        return match.group(1) if match else None
    
    def download_video(self, url: str, filename: str) -> str:
        if not filename.endswith('.mp4'): filename += '.mp4'
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        else:
            return None
        return filename

    def download_high(self, high_url: str, filename: str) -> str:
        return self.download_video(high_url, filename)

    def download_low(self, low_url: str, filename: str) -> str:
        return self.download_video(low_url, filename)




