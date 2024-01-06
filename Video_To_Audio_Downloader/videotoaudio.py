import string

from pytube import YouTube
import os
import shutil
import time

def download_video(video_url, path):
    yt = YouTube(video_url)
    video_stream = yt.streams.filter(only_audio=True).first()

    if video_stream:
        video_stream.download(output_path=path, filename=yt.video_id + '.mp4')
        return True
    else:
        return False

def main():
    video_url = input('Enter YouTube video URL: ')

    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    download_successful = download_video(video_url, path)

    if download_successful:
        video_id = YouTube(video_url).video_id
        original_file_path = path + video_id + '.mp4'

        # Wait until the file is fully downloaded (check every second)
        while not os.path.exists(original_file_path):
            time.sleep(1)

        try:
            # Get the video title and use it for renaming
            video_title = YouTube(video_url).title
            # Remove invalid characters from the filename
            valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
            video_title_cleaned = ''.join(c for c in video_title if c in valid_chars)
            audio_file_path = path + f'{video_title_cleaned}.mp3'

            # Use shutil.move for a safer file move operation
            shutil.move(original_file_path, audio_file_path)
            print(f'Conversion completed: {audio_file_path}')
        except FileNotFoundError:
            print('File not found error during the move operation.')
        except Exception as e:
            print(f'An error occurred during the move operation: {e}')
    else:
        print('No available audio stream for the given video.')

if __name__ == '__main__':
    main()
