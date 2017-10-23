import requests
import urllib

i=1
j=0
while(i<=50):
  try:
    print(i)
    f=open('numb.ts','ab')
    f.write(urllib.request.urlopen('https://vodhls-vh.akamaihd.net/i/mp4/64/4/189804/2235689.mp4/segment'+str(i)+'_0_a.ts?set-akamai-hls-revision=5&hdntl=exp=1508831594~acl=/i/mp4/64/4/189804/2235689.mp4/*~data=hdntl~hmac=289943fc178ca2230a048005d585875a3e3669c7183d8e3f3d882c11eef7e7a6').read())
    f.close()
    i=i+1
  except urllib.error.HTTPError:
    print("song downloaded")
   

    break
