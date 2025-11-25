import requests
import tkinter as tk
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc5ZjI5NmUwLTg5MzYtNGRlNi05NmFiLWVlMGQ0MzZmOTRmNSIsImlhdCI6MTc2NDA4MzE4Nywic3ViIjoiZGV2ZWxvcGVyLzIzYzBlM2JhLWQ1YmQtMzU5Zi1hM2NiLTliMzFiZjk0ZDM5YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNjUuMTU1LjE2My41Il0sInR5cGUiOiJjbGllbnQifV19.RKfwry0EAZlgvQy-Bq5BjVs-VqfzQykKidrF18BSt37_dsYvj5yznxwdY_eoBnazgRqJ1AoOocA92gtaB4J-vg"
api_key = {"Authorization": f"Bearer {token}"}
endpoint = "/cards"
def getCardData(endpoint, name):
    response = requests.get("https://api.clashroyale.com/v1" + endpoint, api_key)
    if response.status_code != 200:
        print("Error fetching data!")
        print(response.json())
        return None
    for i in range(len(response)):
        if response[i]["name"] == name:
            cardid = response[i]["id"]
            return "https://api.clashroyale.com/v1" + endpoint + "/" + cardid, api_key
getCardData(endpoint,"Knight")