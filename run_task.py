import requests
import sys
import subprocess

def main():
    try:
        response = requests.get("https://hitmanservice.azurewebsites.net/api/queue/TEST-pi")
    except:
        print("Service unavailable")
        return
        
    if response.status_code == 400:
        return
    if response.status_code == 404:
        return

    task = response.json()
    print(task)
    outStr=""
    try:
        if task["mode"]=="command":
            outStr = subprocess.check_output(task["content"].split(" "), stderr=subprocess.STDOUT)
        elif task["mode"]=="script":
            outStr = subprocess.check_output(["/bin/bash","-c ","\'" + task["content"] + "\'"], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        outStr = "Error:: "+str(e.output)
    result = {"request" : task, "output" : outStr }
    print(result)
    requests.post("https://hitmanservice.azurewebsites.net/api/queue/TEST-pi-back",data = str(result))
if __name__ == "__main__":
    main()
