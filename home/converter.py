
from gtts import gTTS 


def text_to_mp3(text,mp3_path):
	language = 'ar'
	myobj = gTTS(text=text, lang=language, slow=False)
	myobj.save(mp3_path)
	# os.system("start media/output.mp3")
	return 0

	