import lxml.html, requests, urlparse, getpass

login_url = 'https://cmsonline.cern.ch/webcenter/portal/cmsonline/pages_tracker/standardplots?wc.contentSource='

session = requests.Session()
login_page = session.get(login_url)
login_tree = lxml.etree.HTML(login_page.text)
login_form = login_tree.findall('.//form')[0]

login_post_url = urlparse.urljoin(login_page.url, dict(login_form.items()).get('action'))
login_form_inputs = login_form.findall('.//input')
login_post_data = {}
for login_form_input in login_form_inputs:
	login_form_dict = dict(login_form_input.items())
	if login_form_dict['type'].lower() == 'hidden':
		login_post_data[login_form_dict['name']] = login_form_dict.get('value')
	elif login_form_dict['type'].lower() == 'password':
		login_post_data[login_form_dict['name']] = getpass.getpass()
	elif login_form_dict['type'].lower() == 'text':
		login_post_data[login_form_dict['name']] = getpass.getpass('Username: ')

print login_post_url
print login_post_data
login_result = session.post(login_post_url, data = login_post_data)

