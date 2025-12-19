import json

data_file = "youtube.txt"

def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except:
        return []

def data_helper(videos):
    with open(data_file, 'w') as file:
        json.dump(videos, file)

def list_all_video(videos):
    print("\n")
    for index, video in enumerate(videos, start = 1):
        print(index,": ", video['name'], " ", video['time'])

def add_video(videos):
    name = input("enter name of video: ")
    time = input("enter time of video: ")
    videos.append({'name': name, 'time': time})
    data_helper(videos)

def update_video(videos):
    list_all_video(videos)
    index = int(input("The option to update detail: "))
    if 1 <= index <= len(videos):
        upd_name = input("Enter the new name to update: ")
        upd_time = input("Enter new time to update: ")
        videos[index-1] = {"name": upd_name, "time": upd_time}
        data_helper(videos)
    else:
        print("Invalid index selected!!!!!")

def delete_video(videos):
    list_all_video(videos)
    index = int(input("The option to delete video you want to: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        data_helper(videos)
    else:
        print("Invalid index selected!!!!!")

def main():
    videos = load_data()

    while True:
        print("\n -----------YouTube Mangaer-----------")
        print("1. List all videos saved")
        print("2. Add videos to YouTube")
        print("3. Update a video detail")
        print("4. Delete a video")
        print("5. Exit app")
        choice = input("enter the choice to use: ")

        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case __:
                print("Invalid choice!!!!!!!!")

if __name__ == "__main__":
    main()
