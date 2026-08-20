import requests

from config import Config


class AIServiceError(Exception):
    pass


class AIService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "groq/compound"

    def yanit_uret(self, mesaj, gecmis=None):
        if not self.api_key:
            return (
                "Demo modu aktif. Groq API anahtari tanimlandiginda "
                "Al seyahat asistani yanit vermeye baslayacak."
            )

        messages = [
            {
                "role": "system",
                "content": (
                    "Sen Memora Al'in yapay zeka seyahat asistanisin. "
                    "Kullaniciya Turkce, anlasilir ve samimi cevaplar ver. "
                    "Seyahat rotasi, gezi plani ve destinasyon onerileri sun."
                )
            }
        ]

        if gecmis:
            messages.extend(gecmis[-2:])

        messages.append({
            "role": "user",
            "content": mesaj
        })

        data = {
            "model": self.model,
            "messages": messages
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                json=data,
                timeout=60
            )

            if response.status_code != 200:
                raise AIServiceError(
                    f"Groq API hatasi: {response.status_code} - {response.text}"
                )

            result = response.json()

            return result["choices"][0]["message"]["content"]

        except requests.RequestException as error:
            raise AIServiceError(
                f"Groq API baglanti hatasi: {error}"
            ) from error

        except (KeyError, IndexError, TypeError) as error:
            raise AIServiceError(
                "Yapay zeka servisinden beklenmeyen bir yanit alindi."
            ) from error


ai_service = AIService()