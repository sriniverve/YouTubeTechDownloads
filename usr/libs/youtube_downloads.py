import json
import requests


class YouTubeDownloads:
    def __init__(self, api_key, search_string):
        self.api_key = api_key
        self.search_string = search_string
        self.channel_stats = None

    def get_video_details(self):
        search_url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&max_results=100&q={self.search_string}&key={self.api_key}'
        print(search_url)
        response = requests.get(search_url)
        json_response = json.loads(response.text)
        video_data = []
        try:
            for item in range(50):
                if json_response["items"][item]["id"]["kind"] == "youtube#video":
                    try:
                        videoID = json_response["items"][item]["id"]["videoId"]
                        videoTitle = json_response["items"][item]["snippet"]["title"]
                        video_data.append({"Title": videoTitle, "Video Link": "https://www.youtube.com/watch?v=" + videoID})
                        if len(video_data) == 11:
                            break
                    except:
                        found = None

            return video_data

        except:
            if json_response["error"]["errors"][0]["reason"] == "dailyLimitExceeded" or "quotaExceeded":
                print("There are only a thousand times where you can call the APIs. Try after a day ;-)")
                return None

    def get_channel_stats(self):
        url = f'https://www.googleapis.com/youtube/v3/channels/?part=statistics&id={self.channel_id}&key={self.api_key}'
        print(url)

        response = requests.get(url)
        json_response = json.loads(response.text)
        print(json_response)
        try:
            data = json_response["items"][0]["statistics"]
        except:
            data = None

        self.get_channel_stats = data
        return data

