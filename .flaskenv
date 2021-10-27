model=models/cc.de.300.bin
data=data/data.csv

# use this for faster startup
FLASK_DEBUG=0
FLASK_ENV=production
# use this automatic checking of the examples
#FLASK_DEBUG=1
#FLASK_ENV=development

FLASK_APP=mcn/app.py