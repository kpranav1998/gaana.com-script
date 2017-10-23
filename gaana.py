import requests
import urllib
i=1
j=0
while(j<=7):
  while(i<=50):
    try:
      print(i)
      print(j)
      f=open('song'+str(j)+'.ts','ab')
      f.write(urllib.request.urlopen('https://vodhls-vh.akamaihd.net/i/songs/59/59/52'+str(j)+'52'+str(j)+'_64.mp4/segment'+str(i)+'_0_a.ts?set-akamai-hls-revision=5&hdntl=exp=1508091805~acl=/i/songs/59/59/52'+str(j)+'/52'+str(j)+'_64.mp4/*~data=hdntl~hmac=d60f811096a11b4322b59d84ffdebdeff3ce800b289475a64b19270cd278a09a').read())
      f.close()
      i=i+1
    except urllib.error.HTTPError:
      print("error")
      break
  i=1
  j=j+1
  

'''https://vodhls-vh.akamaihd.net/i/songs/59/59/521/521_64.mp4/segment1_0_a.ts?set-akamai-hls-revision=5&hdntl=exp=1508091895~acl=/i/songs/59/59/521/521_64.mp4/*~data=hdntl~hmac=a23f9343a54074cdfca42830f5ee12a30584a9782262b27d93f22c76a5cc5495

https://vodhls-vh.akamaihd.net/i/songs/59/59/520/520_64.mp4/segment1_0_a.ts?set-akamai-hls-revision=5&hdntl=exp=1508091805~acl=/i/songs/59/59/520/520_64.mp4/*~data=hdntl~hmac=d60f811096a11b4322b59d84ffdebdeff3ce800b289475a64b19270cd278a09a'''

