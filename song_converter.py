from pydub import AudioSegment
#pydub available from http://pydub.com/

#Recommend to copy the original flac file to it's own folder

#Run this code from where your original flac file is


numberOfConversions = input("Enter number of conversions: ")

songFlac = "" + raw_input("Enter the name of the file (ending in .flac): ")

validFile = False

startNumber = 1

while validFile == False:
	try:
		song = AudioSegment.from_file(songFlac,
		format="flac") #Load the flac file
		validFile = True
	except:
		songFlac = raw_input("""
Invalid file name.

Enter the name of the file (ending in .flac): """)

		if songFlac == "kill":
			break



songMP3 = songFlac[:-4] + "mp3"

print "I will now create " + str(numberOfConversions) + " conversions!"

print "------------------------"


currentNum = startNumber
while currentNum < numberOfConversions:
	if startNumber == 1:
		song = AudioSegment.from_file(songFlac,
			format="flac") #Load the flac file
	else:
		song = AudioSegment.from_file(str(currentNum) + songFlac,
			format="flac") #Load the flac file

	print("loading file "+ str(currentNum) + "...")


	currentNum += 1

	print("saving (mp3) file "+ str(currentNum) + "...")

	song.export(str(currentNum) + songMP3,
		format="mp3", bitrate="128k") #Save as MP3

	song = AudioSegment.from_file(str(currentNum) + songMP3,
		format="mp3") #Load the newly created MP3

	print("Reloading file "+ str(currentNum) + "...")

	currentNum +=1

	print("saving (flac) file "+ str(currentNum) + "...")

	song.export(str(currentNum) + songFlac,
		format="flac") #Save As Flac

print "------------------------"

print "All completed!"
