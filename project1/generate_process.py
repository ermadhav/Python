def text_to_audio(folder):
    pass

def create_reel():
    pass

if __name__ == "__main__":
    with open("done.txt", "r") as f:
        folder = f.readline()

    folders = os.listdir("user_uploads")
    folder = "588....."
    text_to_audio(folder)
    create_reel(folder)