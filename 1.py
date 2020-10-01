import speech_recognition as sr

r=sr.Recognizer()

a=sr.AudioFile('1.wav')
with a as source :
	audio=r.record(source)

text=r.recognize_google(audio)


file1=open(r"C:\Users\ADMIN\Downloads\speech-to-text-master\k.txt","a")
file1.writelines(text)
file1.close()