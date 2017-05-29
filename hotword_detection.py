import snowboydecoder
from google.assistant import *

def detected_callback():
    print("hotword_detection: hotword detected")

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
	args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    print("hotword_detection: Starting Assistant")
    with Assistant(credentials) as assistant:
    	assistant.start_conversation()
	# Stop the  detector until google assistant is done
	# Turn on google assistant
	
detector = snowboydecoder.HotwordDetector("Robin.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)

detector.terminate()