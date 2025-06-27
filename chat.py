import google.generativeai as genai

genai.configure(api_key="COLE_SUA_CHAVE_AQUI")

model = genai.GenerativeModel("gemini-1.5-flash-latest")

resposta = model.generate_content("Olá! Quem é você?")
print(resposta.text)
