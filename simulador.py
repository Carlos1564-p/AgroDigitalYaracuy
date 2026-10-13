# simulador.py
import requests
import time

LOCAL_WEBHOOK_URL = "http://127.0.0.1:8000/webhook/whatsapp"

def simular_saludo_agricultor():
    print("\n[SIMULADOR] 🌾 Agricultor envía un 'Hola' por WhatsApp...")
    payload = {
        "object": "whatsapp_business_account",
        "entry": [{
            "changes": [{
                "value": {
                    "messaging_product": "whatsapp",
                    "messages": [{
                        "from": "584125551122",
                        "id": "wamid.HBgLNTg0MTI1NTUxMTIy",
                        "timestamp": str(int(time.time())),
                        "text": {"body": "Hola"},
                        "type": "text"
                    }]
                },
                "field": "messages"
            }]
        }]
    }
    response = requests.post(LOCAL_WEBHOOK_URL, json=payload)
    print(f"[SERVIDOR RESPONDIÓ]: Código {response.status_code}")

def simular_boton_municipio():
    print("\n[SIMULADOR] 🌾 Agricultor presiona el botón interactivo de 'Chivacoa'...")
    payload = {
        "object": "whatsapp_business_account",
        "entry": [{
            "changes": [{
                "value": {
                    "messaging_product": "whatsapp",
                    "messages": [{
                        "from": "584125551122",
                        "id": "wamid.HBgLNTg0MTI1NTUxMTIy",
                        "timestamp": str(int(time.time())),
                        "type": "interactive",
                        "interactive": {
                            "type": "button_reply",
                            "button_reply": {"id": "mun_chivacoa", "title": "Bruzual (Chivacoa)"}
                        }
                    }]
                },
                "field": "messages"
            }]
        }]
    }
    response = requests.post(LOCAL_WEBHOOK_URL, json=payload)
    print(f"[SERVIDOR RESPONDIÓ]: Código {response.status_code}")

if __name__ == "__main__":
    print("=== INICIANDO SIMULADOR DE WEBHOOKS (ALIMENTOS HCHF4) ===")
    simular_saludo_agricultor()
    time.sleep(2)
    simular_boton_municipio()
    print("\n=== SIMULACIÓN CONCLUIDA ===")