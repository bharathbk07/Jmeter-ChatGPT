import requests
api_Key = ''

#openAI-----------------------------------------------------------------------------------------------
def openai(question):
    openai_url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_Key}'
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': f'{question}'
            }
        ],
        'temperature': 0.7
    }

    openai_response = requests.post(openai_url, headers=headers, json=data)

    if openai_response.status_code == 200:
        respone = openai_response.json()['choices'][0]['message']['content']
        #print(respone)
        return respone
    else:
        print(f"API request failed with status code: {openai_response.status_code}")
        print(openai_response.json())
        return None
