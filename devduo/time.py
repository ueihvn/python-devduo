from datetime import datetime, timezone
import pytz

datetime_now = datetime.now(tz=timezone.utc)
vn_tz = pytz.timezone('Asia/Ho_Chi_Minh')
datetime_now_vn = datetime_now.astimezone(vn_tz)
print(datetime_now_vn)
