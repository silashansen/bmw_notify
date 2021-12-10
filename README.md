# BMW LOCK NOTIFY

## To run this
1. Install dependencies
<pre>pip3 install -r requirements.txt</pre>
2. Create a new file called bmw_notify.env and fill it with the following:
<pre>
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
BMW_USERNAME=
BMW_PASSWORD=
SMS_FROM=<your twilio 'from' number>
SMS_RECEIVERS=<comma separated list of receivers>
SEND_SUCCESS_NOTIFICATION=<debug flag>
</pre>
3. Run the app
<pre>python app.py</pre>
