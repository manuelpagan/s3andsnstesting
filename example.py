import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAJR5KTIRRTDNQPCJQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'test-bucket-july-27'

s3 = boto3.resource(
  's3',
  aws_access_key_id = ACCESS_KEY_ID,
  aws_secret_access_key = ACCESS_SECRET_KEY,
  config = Config(signature_version = 's3v4')
)

wr = open('/Users/mpagan/PycharmProjects/Python1/1234567890.json', 'w')

# mp = open('/Users/mpagan/PycharmProjects/Python1/manuelandrespagan.json', 'rb')

wr.write("Modified test. I hope you see this in modified_test.json and not in manuelandrespagan.json!")

wr.close()

# mp.close()

mp = open('/Users/mpagan/PycharmProjects/Python1/manuelandrespagan.json', 'rb')

wr = open('/Users/mpagan/PycharmProjects/Python1/1234567890.json', 'rb')

s3.Bucket(BUCKET_NAME).put_object(Key = 'manuelandrespagan.json', Body = mp)

mp.close()
wr.close()

wr = open('/Users/mpagan/PycharmProjects/Python1/1234567890.json', 'rb')

s3.Bucket(BUCKET_NAME).put_object(Key = 'modified_test.json', Body = wr)

s3.Bucket(BUCKET_NAME).download_file('manuelandrespagan.json', '/Users/mpagan/PycharmProjects/Python1/1234567890.json')

wr.close()

print("Done!")



































'''
with open('manuelandrespagan.json', 'wb') as data:
    BUCKET_NAME.download_file('manuelandrespagan.json', 'manuelandrespagan2.json')





print("manuelandrespagan.json")

'''
#s3.Bucket(BUCKET_NAME).put_object(Key='manuelandrespagan.json', Body=data)



