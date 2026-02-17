import os

def text_to_audio(folder):
    pass

def create_reel():
    pass

if __name__ == "__main__":
    with open("done.txt", "r") as f:
        done_folders = f.readlines()

    folders = os.listdir("user_uploads")
    for folder in folders:
        if(folder not in done_folders):
        text_to_audio(folder)
        create_reel(folder)
    