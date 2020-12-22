# TwitterTrendsVisualizer

[sample](https://radiant-earth-80654.herokuapp.com/)

## Specification
This script save　tweet from twitter timelines. When the date changes, save the data to JSON. 

## API application and key acquisition
Apply for Twitter API and get consumer key in this site.
[Developer Site](https://developer.twitter.com/en)

List of key

* Consumer Key
* Consumer Secret Key
* Access Token
* Access Secret Token

Save the obtained key in `config.py`.

	#config.py
    
    Consumer_Key = "Comsumer Key"
	Consumer_Secret_Key = "Consumer Secret Key"
	Access_Token = "Access Token"
	Access_Secret_Token = "Access Secret Token"