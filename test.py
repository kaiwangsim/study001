from pytz import timezone
from datetime import datetime
import pytz


fmt = '%Y-%m-%d %H:%M:%S %Z%z'

zone_CN = timezone('Asia/Shanghai')
xx=datetime.now().astimezone(zone_CN).strftime(fmt)
zone_London = pytz.BaseTzInfo()

print(xx)