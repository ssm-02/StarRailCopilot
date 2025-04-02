import requests  
import os  

TOKEN = os.getenv("GH_TOKEN")  
REPO = "smallstoreliu/StarRailCopilot"  # 改成客户要刷的仓库  

for _ in range(100):  
    requests.put(f"https://api.github.com/user/starred/{REPO}", headers={"Authorization": f"token {TOKEN}"})  
