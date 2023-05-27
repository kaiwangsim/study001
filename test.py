from pytz import timezone
from datetime import datetime


fmt = '%Y-%m-%d %H:%M:%S %Z%z'

zone_CN = timezone('Asia/Shanghai')
xx=datetime.now().astimezone(zone_CN).strftime(fmt)


print(xx)