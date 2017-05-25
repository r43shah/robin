import snowboydecoder

def detected_callback():
    print "hotword detected"
	# Stop the  detector until google assistant is done
	# Turn on google assistant
	
detector = snowboydecoder.HotwordDetector("Robin.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)

detector.terminate()