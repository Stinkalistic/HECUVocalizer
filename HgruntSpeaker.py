import winsound
import os
import wave

with open("settings.txt","r") as file:
    settings = file.readlines()
    download = settings[0].removeprefix("asktodownload=")
    download = download.removesuffix("\n")
    outputname=settings[1].removeprefix("outputname=")
def main():
    speech = input("What do you want the HECU to say? \n")
    words = speech.split(" ")
    soundfiles = []
    for i in range(len(words)):
        if not words[i].lower() == words[i]:
            sound = "hgrunt//"+words[i].lower()+"!.wav"
        else:
            sound = "hgrunt//"+words[i].lower()+".wav"
        soundfiles.append(sound)
        if os.path.exists(sound):   
            winsound.PlaySound(sound,winsound.SND_ALIAS)
        else:
            print(f"Sound file ",sound.removeprefix("hgrunt//")," does not exist")
    if download == "yes":
        if input("Would you like to download this as an audio file?(Y/N)").lower() == "y":
            with wave.open(soundfiles[0], "rb") as wav:
                params = wav.getparams()
            with wave.open(outputname,"wb") as output:
                output.setparams(params)
                for soundfile in soundfiles:
                    with wave.open(soundfile, "rb") as wav:
                        output.writeframes(wav.readframes(wav.getnframes()))
            print("audio saved succesfully!")
    main()
main()