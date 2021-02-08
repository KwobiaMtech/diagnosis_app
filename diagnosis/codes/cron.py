import pusher

pusher_client = pusher.Pusher(
    app_id='1151410',
    key='f0870f9290a23dc9e32c',
    secret='6104f860e79b2589cd4a',
    cluster='mt1',
    ssl=True
)


def my_cron_job():
    pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
