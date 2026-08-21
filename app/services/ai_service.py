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

        kullanici_mesaji = str(mesaj).strip()

        if not kullanici_mesaji:
            return "Lütfen bir mesaj yazın."

        # Çok uzun mesajları sınırla
        kullanici_mesaji = kullanici_mesaji[:500]

        messages = [
            {
                "role": "system",
                "content": (
                    "Sen Memora Al'in yapay zeka seyahat asistanisin. "
                    "Kullaniciya Turkce, anlasilir ve samimi cevaplar ver. "
                    "Seyahat rotasi, gezi plani ve destinasyon onerileri sun."
                )
            },
            {
                "role": "user",
                "content": kullanici_mesaji
            }
        ]

        data = {
            "model": self.model,
            "messages": messages,
            "max_tokens": 500
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
                timeout=30
            )

            if response.status_code != 200:
                # Gerçek hata sunucu logunda kalır
                print(
                    f"Groq API hatasi: "
                    f"{response.status_code} - {response.text}"
                )

                raise AIServiceError(
                    "Al şu anda yanıtını oluşturamadı. "
                    "Lütfen tekrar deneyin. ✨"
                )

            result = response.json()

            return result["choices"][0]["message"]["content"]

        except requests.RequestException as error:
            print(f"Groq baglanti hatasi: {error}")

            raise AIServiceError(
                "Al şu anda yanıtını oluşturamadı. "
                "Lütfen tekrar deneyin. ✨"
            ) from error

        except (KeyError, IndexError, TypeError) as error:
            print(f"Groq yanit hatasi: {error}")

            raise AIServiceError(
                "Al şu anda yanıtını oluşturamadı. "
                "Lütfen tekrar deneyin. ✨"
            ) from error


ai_service = AIService()