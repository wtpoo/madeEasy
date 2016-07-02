# Thanking everyone who wished me on my birthday
import requests
import json
import facebook
import simplejson

def get_posts(oauth_access_token):
	"""
		Returns dictionary of id, first names of people who posted on my wall
		between start and end time
	"""
	timestamp='1388514600'
	limit='500'
	page_url = "https://graph.facebook.com/me/feed?access_token="+oauth_access_token+"&limit="+limit+"&since="+timestamp
	print(page_url)
	page = requests.get(page_url)
	result = page.text
	parsed_data = simplejson.loads(result)
	graph = facebook.GraphAPI(oauth_access_token)
	profile = graph.get_object("me")	
	for eachid in parsed_data['data']:
		id=eachid['id']
		from_name=eachid['from']['name']
		#print(id)
		if(from_name.split(' ')[0] != "Er"):
			print(from_name.split(' ')[0])
			graph.put_object(id, "comments", message="Thank you "+from_name.split(' ')[0]+"!")
			graph.put_object(id, "likes")
	print("Total posts received are "+str(len(parsed_data['data'])))
	return	
	
#graph.put_object("834102483289314_876433005722928", "comments", message="Reply")
#graph.put_object("834102483289314_876433005722928", "likes")
#834102483289314_876433005722928/comments?message=This+is+a+test+comment


if __name__ == '__main__':
	posts=[]
	oauth_access_token="CAACEdEose0cBADp01p08LuorqUtJwIp7hLhZAsZCHpAylMx4nDzcYZAfLtZCTGdYskIyrORgD2j960fa8oBXnJCgBxYrLXzuAtBlf7yYYNIHHSGSZA8Quac3rkDPvfEGh3u3lFBZCSaeHmFhzp9ZAh1ZCRCtD8ZB7ETiE6odvVwGPdDvfaZB1XWtiZC6mNXDfaZALtKIyS36pJ0iiWpKbhUqNUKn"
	#writeFile = open("results.txt", "w")
	#writeFile.write(get_posts(oauth_access_token))
	get_posts(oauth_access_token)