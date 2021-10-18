from kafka import KafkaProducer
from json import dumps
import sys

arguments = len(sys.argv) - 1
inputStr = "default input"
print("with arguments " +str(arguments))
loopcount=100
if arguments>=1:
   inputStr=sys.argv[1]
   if arguments==2:
      loopcount=int(sys.argv[2])
print("with input " +inputStr)
producer = KafkaProducer(
   value_serializer=lambda m: dumps(m).encode('utf-8'), 
   #bootstrap_servers=['172.17.0.1:32783','172.17.0.1:32782','172.17.0.1:32781'])
   bootstrap_servers=['119.13.83.68'])
for i in range(loopcount):
   producer.send("testTopic", value={"hello"+str(i): " from "+str(inputStr)})
producer.flush()
producer.close()