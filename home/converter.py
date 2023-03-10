
from gtts import gTTS 
import os 

def to_mp3(text,name):
	language = 'en'
	myobj = gTTS(text=text, lang=language, slow=False)
	myobj.save("media/"+name)
	# os.system("start media/output.mp3")
	return name

	