# TwitterTrendsVisualizer


## Specification
This script save　tweet from twitter timelines. When the date changes, save the data to CSV. 
Example of data to be saved
|  TweetID  |  text  |  Word  |  Week  |  Month  |  Day  |  Hour  |  Minute  |  Second  |  Year  |
|  -------  |  ---------  |  --------  |  ------------  |  -------------  |  ---------  |  ---------  |  -------  |  ----------  |  ---------  |
|  1249121888112128000  |  今日も一日 https://t.co/8JLXdARugO  |  今日  |  Sat  |  04  |  11  |   23  |   47  |   20  |  2020   |

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