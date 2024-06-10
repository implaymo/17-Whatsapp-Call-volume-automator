from pycaw.pycaw import AudioUtilities



def change_whatsapp_volume():
    try:
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            if session.Process and session.Process.name() == "Whatsapp.exe":
                volume.SetMasterVolume(0.5, None)
                print("Volume adjusted for WhatsApp.")
    except Exception as e:
        print(f"ERROR FOUND: {e}")

def main():
    change_whatsapp_volume()
    
if __name__ == "__main__":
    main()