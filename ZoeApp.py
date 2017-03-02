from linkedin import linkedin

API_KEY = '77nymncwcfk86e'
API_SECRET = 'BAfhIKepBzYabuAW'
RETURN_URL = 'http://127.0.0.1:8080/'
#RETURN_URL = 'http://localhost:8000/'
#http://localhost:8080/


authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print authentication.authorization_url  # open this url on your browser
application = linkedin.LinkedInApplication(authentication)
