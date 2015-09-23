import boto 
import boto.ec2
conn = boto.ec2.connect_to_region("us-west-2",
     aws_access_key_id='AKIAJ76RNMXT3A4W4M5A',
     aws_secret_access_key='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')
print "conn is %s" % conn
statuses = conn.get_all_instance_status()
print "status of instances %s" % statuses 
reservations = conn.get_all_instances()
print "****************************************"
print " reservations are %s" % reservations 
print "****************************************"
print "reservations id is %s " % reservations[0].instances[0].id 
print "reservations state is %s " % reservations[0].instances[0].state
reservations[0].instances[0].stop()
#print "reservation name is %s " %reservations[0].instances[0].name 
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
