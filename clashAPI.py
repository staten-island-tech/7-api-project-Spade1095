import requests
import tkinter as tk
import json
# 165.155.164.16
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQ5YjI1MWIzLTY5M2QtNGVhZS1iZTkxLTI3NmQxZjdlYjcyOSIsImlhdCI6MTc2NDE2ODAzNCwic3ViIjoiZGV2ZWxvcGVyLzIzYzBlM2JhLWQ1YmQtMzU5Zi1hM2NiLTliMzFiZjk0ZDM5YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNjUuMTU1LjE2NC4xNiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.9AyyT7PJcwWUVZvYeb6eS_IpCTJOfyM6i49lM0byv80xLb-nRk3ku0UamzikhK6L_PTCG9GDJtvPpVk0IoWUtA"
# 165.155.163.5
# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhlZTU1MTg0LTg4MzQtNDI5ZC1iZTE5LTI3ODhhNWM2MjM0NyIsImlhdCI6MTc2NDE2ODEwMiwic3ViIjoiZGV2ZWxvcGVyLzIzYzBlM2JhLWQ1YmQtMzU5Zi1hM2NiLTliMzFiZjk0ZDM5YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNjUuMTU1LjE2My41Il0sInR5cGUiOiJjbGllbnQifV19.qDGz1KhmbidyL0HsNEmoipsXDOFrZJhetbfOYlDb7sI9TW6VUsvkMAHJOMOIR8tRxRW0kq8VJEMxgtvyhxUibA"
api_key = {"Authorization": f"Bearer {token}"}
endpoint = "/cards"
def getCardData(endpoint, name):
    response = requests.get("https://api.clashroyale.com/v1" + endpoint, api_key)
    if response.status_code != 200:
        print("Error fetching data!")
        print(response.json)
        return None
    response = response.json
    print(response)
    for i in range(len(response['items'])):
        if i["name"] == name:
            cardid = response[i]["id"]
            return "https://api.clashroyale.com/v1" + endpoint + "/" + cardid, api_key
getCardData(endpoint,"Knight")