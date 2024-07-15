Here's how you can update your `README.md` to include the details and download functions for your `xvideos-py` library.

### Updated `README.md`

```markdown
# xvideos-py
A powerful Python library to scrape xvideos.com.

## 💻 Installation

```bash
$ pip install xvideos-py
```

## 🍑 Usage

### 🍒 Importing the Library

```python
from xvideos import XVideos
```

### 🍒 Retrieve Fresh Videos

```python
xvideos = XVideos()

# Retrieve fresh videos from the first page
fresh = xvideos.fresh(page=1)

# Log details of the retrieved videos
print(fresh['videos'])  # List of video objects with properties like url, path, title, duration, profile, views
print(fresh['pagination']['pages'])  # List of available page numbers
```

### 🍒 Retrieve Verified Videos

```python
# Retrieve verified videos from the first page
verified = xvideos.get_verified(page=1)

# Log details of the retrieved videos
print(verified['videos'])  # List of verified video objects with properties like url, path, title, duration, profile, views
print(verified['pagination'])  # List of available page numbers
```

### 🍒 Search Videos

```python
# Search for videos with a specific keyword
search_results = xvideos.search(page=1, k="example", sort="relevance")

# Log details of the search results
print(search_results['videos'])  # List of video objects with properties based on the search parameters
print(search_results['pagination'])  # List of available page numbers
```

#### 🍐 Params explanation

| Parameter | Default        | Options                                                                                  |
|-----------|----------------|------------------------------------------------------------------------------------------|
| `page`    | `1`            | (any positive integer)                                                                   |
| `k`       | `""`           | (any search keyword)                                                                     |
| `sort`    | `"relevance"`  | `"uploaddate"`, `"rating"`, `"length"`, `"views"`, `"random"`                            |
| `datef`   | `"all"`        | `"today"`, `"week"`, `"month"`, `"3month"`, `"6month"`, `"all"`                         |
| `durf`    | `"allduration"`| `"1-3min"`, `"3-10min"`, `"10min_more"`, `"10-20min"`, `"20min_more"`, `"allduration"` |
| `quality` | `"all"`        | `"hd"`, `"1080P"`, `"all"`                                                                |
| `pewmium` | `False`        | `False, True`                                                                            |

### 🍒 Retrieve Video Details

```python
# Retrieve details of a specific video
video_url = "https://www.xvideos.com/video12345678/example_video"
details = xvideos.details(video_url)

# Log details of the retrieved video
print(details)  # Dictionary with properties like title, url, duration, image, views, videoType, description, files, models, tags, likePercentage, dislikePercentage, commentsCount
```

### 🍒 Download Videos

```python
# Download high-quality version of a specific video
video_url = "https://www.xvideos.com/video12345678/example_video"
filename = "example_video_high"
downloaded_path = xvideos.download_high(video_url, filename)

print(f"High quality video saved at: {downloaded_path}")

# Download low-quality version of a specific video
filename = "example_video_low"
downloaded_path = xvideos.download_low(video_url, filename)

print(f"Low quality video saved at: {downloaded_path}")
```

## 🍑 Development

### 🍒 Running Tests

To run tests, you can use `pytest`. Ensure you have it installed in your development environment.

```bash
$ pytest
```
---
### 🐼 @me

You can find me on twitter as 🐤 <a href="https://twitter.com/osinthappyemo">@osinthappyemo</a>
or on instagram as 🍢 <a href="https://instagram.com/osintxv">@osintxv</a>
