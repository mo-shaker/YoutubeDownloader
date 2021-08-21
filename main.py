from pytube import YouTube

# variables and CONSTANTS
OUTPUT_PATH = "/home/raq/videos"

# --- functions ---
def on_progress(stream, chunk, bytes_remaining):
    print(' progress:', bytes_remaining, "           ", end='\r', flush=True)

def on_complete(stream, filename):
    print()
    print('--- Completed ---')
    print('stream:', stream)
    print('filename:', filename)

URL = input("Please enter you URL:")

if not URL:
    print("The value entered is incorrect")
    exit()

video = YouTube(URL)
video.register_on_progress_callback(on_progress)
video.register_on_complete_callback(on_complete)
selectstream = video.streams.get_highest_resolution()
filename = selectstream.download(output_path=OUTPUT_PATH)
