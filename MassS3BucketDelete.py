# login as aws user on cli.
# aws s3 ls >> s3_list.txt
# clean up list to only have bucket names
#Copy list to test with correct formatting example:
# "Buket-B",
# run with python3 MassS3BucketDelete

#Make sure boto3 lib installed. :)

import boto3
test = [ 
	#Bucket list here
	]

s3 = boto3.resource('s3')


for each in test:
	s3.Bucket(each).delete()
	print("Bucket: " + each + " deleted")
