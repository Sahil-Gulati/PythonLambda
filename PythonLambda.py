#author Sahil Gulati

import urllib
import urllib2

def lambda_handler(event,context):
    
    ##
    # Change url on which you want to receive email complete content
    # with headers
    ##
    url = 'http://html.in/login.php'
    
    ##
    # Creating complete request which will be going to execute
    ##
    requestData = urllib2.Request(url)
    
    ##
    # Generating data for sending over some url
    ##
    data = urllib.urlencode(event)
    
    ##
    # Adding parameters and options to request
    ##
    requestData.add_data(data)
    requestData.add_header('User-Agent', 'Mozilla/5.0');
    requestData.add_header('Referer', 'https://httpbin.org/post')
    
    ##
    # Executing request which will be sent over some URL with data, parameters and headers
    ##
    response = urllib2.urlopen(requestData)
    
    ##
    # Returning the request received from Python Lambda
    ##
    return response.read();