# import boto module 

import boto 
import boto.ec2

# connect to boto ec2 instance  
conn = boto.ec2.connect_to_region("us-west-2",
     aws_access_key_id='',
     aws_secret_access_key='')
print "conn is %s" % conn
# get status of all instances from conn 
statuses = conn.get_all_instance_status()
print "status of instances %s" % statuses 

#get instances from reservations 
reservations = conn.get_all_instances()

print "****************************************"
print " reservations are %s" % reservations 
print "****************************************"
# print the id of the instance 
print "reservations id is %s " % reservations[0].instances[0].id 
# print the state of an instance 
print "reservations state is %s " % reservations[0].instances[0].state

# To stop an instance 
#reservations[0].instances[0].stop()

#print "reservation name is %s " %reservations[0].instances[0].name 
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
