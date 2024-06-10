from pycaw.pycaw import AudioUtilities


def main():

    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.channelAudioVolume()
        print(f"Session {session}")
        count = volume.GetChannelCount()
        print(f"COUNT: {count}")
        volumes = [volume.GetChannelVolume(i) for i in range(count)]
        print(f"    volumes = {volumes}")
        if session.Process and session.Process.name() == "WhatsApp.exe":
            volume.SetChannelVolume(0, 0.1, None)
            print("    Set the volume of left channel to 0.5!")
            volume.SetChannelVolume(1, 0.1, None)
            print("    Set the volume of right channel to 0.5!")


if __name__ == "__main__":
    main()