
from gtts import gTTS 
import os 
from base.settings import BASE_DIR
def to_mp3(text,name):
	language = 'ar'
	myobj = gTTS(text=text, lang=language, slow=False)
	myobj.save(str(BASE_DIR)+"media/"+name)
	# os.system("start media/output.mp3")
	return name

	