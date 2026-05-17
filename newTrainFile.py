import psutil
from fastapi import FastAPI

app=FastAPI()

@app.get("/status")
def get_system_status():
    cpu=psutil.cpu_percent(interval=1)
    mem=psutil.virtual_memory()
    used_memory=round(mem.used/(1024**3),2)
    disk=psutil.disk_usage('/')
    disk=round(disk[2]/(1024**3),2)
    return cpu, used_memory, disk

def add(a: str, b: str)->str:
    res=a+b
    return res

if __name__=="__main__":
    print(f"Result: {add('Hello', 'World')}") 
    print(f"Data of PC:{get_system_status()}")
