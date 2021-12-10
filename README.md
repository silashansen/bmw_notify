# BMW UNLOCKED NOTIFY
This application will send an SMS to a list of phone nubmers if any of the vehicles listed in the BMW CONNECTED acccount are unlocked at the time of the check.
The specific use-case is running this as a container that is triggered as a lambda function on a schedule.


## To run this
1. Install dependencies
<pre>pip3 install -r requirements.txt</pre>
2. Create a new file called bmw_notify.env and fill it with the following:
<pre>
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
BMW_USERNAME=
BMW_PASSWORD=
SMS_FROM=(your twilio 'from' number)
SMS_RECEIVERS=(comma separated list of receivers)
SEND_SUCCESS_NOTIFICATION=(debug flag true/false)
</pre>
3. Run the app
<pre>python app.py</pre>
