import multiprocessing
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

def main():
    url = "https://fastly.picsum.photos/id/168/200/300.jpg?hmac=ILU5dddz6ohoQEq3_1fmoy2wEFfM1V1JfjLX_JsbOz0"
    pros = []
    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
    

if __name__ == '__main__':
    main()