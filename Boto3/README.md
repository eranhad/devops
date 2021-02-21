Bucket created: firstpythonbucket96f195d9-fa41-488d-b120-320e7164ebb4 in Region: eu-central-1
Bucket created: secondpythonbucket956d4836-2cf8-4e26-b27a-cd906774952c in Region: eu-central-1

Bucket firstpythonbucket96f195d9-fa41-488d-b120-320e7164ebb4 Versioning status is: Enabled

File created: ac808bfirstfile.txt
File created: e7d8c8secondfile.txt
File created: 674961thirdfile.txt

First Bucket: s3.Bucket(name='firstpythonbucket96f195d9-fa41-488d-b120-320e7164ebb4')
First Object: s3.Object(bucket_name='firstpythonbucket96f195d9-fa41-488d-b120-320e7164ebb4', key='ac808bfirstfile.txt')
Second Object: s3.Object(bucket_name='firstpythonbucket96f195d9-fa41-488d-b120-320e7164ebb4', key='e7d8c8secondfile.txt')
Third Object: s3.Object(bucket_name='firstpythonbucket96f195d9-fa41-488d-b120-320e7164ebb4', key='674961thirdfile.txt')

Uploading files to S3 bucket
Version of first file: a55eoFr2guF8PAckpDq8ns2i0bQUqN0K

Download file ac808bfirstfile.txt FROM bucket firstpythonbucket96f195d9-fa41-488d-b120-320e7164ebb4 TO /tmp/

Copy file ac808bfirstfile.txt FROM firstpythonbucket96f195d9-fa41-488d-b120-320e7164ebb4 TO secondpythonbucket956d4836-2cf8-4e26-b27a-cd906774952c

Second file Access Control List (Public) [{'Grantee': {'ID': 'b0e4af819744a8483cfd728e37fb759c7dfc43deaa05129706ec9b97d52ae69e', 'Type': 'CanonicalUser'}, 'Permission': 'FULL_CONTROL'}, {'Grantee': {'Type': 'Group', 'URI': 'http://acs.amazonaws.com/groups/global/AllUsers'}, 'Permission': 'READ'}]
Second file Access Control List (Private) [{'Grantee': {'ID': 'b0e4af819744a8483cfd728e37fb759c7dfc43deaa05129706ec9b97d52ae69e', 'Type': 'CanonicalUser'}, 'Permission': 'FULL_CONTROL'}]

Third file Encryption is: AES256
Third file Storage Class is: STANDARD_IA

Empty buckets...

Delete versions [{'Key': '674961thirdfile.txt', 'VersionId': 'e.Rd_4bwypLQ6GiLb6IgLarZrbuwBMR6'}, {'Key': 'ac808bfirstfile.txt', 'VersionId': 'a55eoFr2guF8PAckpDq8ns2i0bQUqN0K'}, {'Key': 'ac808bfirstfile.txt', 'VersionId': 'qp1QchAL3JqzptmH3Eemsc_y_fO2PdHT'}, {'Key': 'e7d8c8secondfile.txt', 'VersionId': 'f4vPOi.MJTQy6Vy3dxjp_aXo72takUof'}, {'Key': '674961thirdfile.txt', 'VersionId': 'V4Wr_7ErUVvZw.41LiAx39uuP5m09Weq'}, {'Key': 'ac808bfirstfile.txt', 'VersionId': 'oSPHHw1IEhxi.pW2ILSI2mpA.dywpKgD'}, {'Key': 'e7d8c8secondfile.txt', 'VersionId': 'qdnsBbXynW6_raYmgexENP_pmPHy85e.'}]: 

Delete buckets!