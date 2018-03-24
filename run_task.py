import requests
import sys
import subprocess

def main():
    try:
        response = requests.get("https://hitmanservice.azurewebsites.net/api/queue/boss-pi")
    except:
        print("Service unavailable")
        return
        
    if response.status_code == 400:
        return
    if response.status_code == 403:
        return

    task = response.json()
    print(task)
    if task["mode"]=="command":
        proc = subprocess.Popen(task["content"].split(" "), stdout=subprocess.PIPE)
    elif task["mode"]=="script":
        proc = subprocess.Popen(["/bin/bash","-c ","\'" + task["content"] + "\'"] , stdout=subprocess.PIPE)
    std, err = proc.communicate()
    print(std)    
    requests.post("https://hitmanservice.azurewebsites.net/api/queue/boss-pi-back")
if __name__ == "__main__":
    main()
