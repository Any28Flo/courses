import boto3
llave=open("llave.pem",'r')
llave=llave.read()
llave=str(llave)
#llave="-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAhDXu5hJSpaQQwsqrDn9TbJPVOp1BK7Lo6MgEsxTXJyw6ByGT\nQ9ni4rDS9E9VLhXW4eP3Mgo4Y/YeNtns00UP/vF3BFHGlHj3bNrTdPRE+XKF+GrA\nTuWvia96Jpjzp/SiCjU7Ldk9pRprG3rbiZQhv211eDs1UUzmK6Nsp+HMOjs5xKSo\nLSjaHOWyGkWINFGKTyvcfG4AZ7p5Bubu9MvotmH0lWvghQBVoAxxSyjD8JYob788\nEH35ALomTf2MhmRWeR8kZvi1wlyTX9DWTX0iosGvXh5kMK9NGSYxem95Y0MSvkAl\nucFdYJWWAlPCQ4eNz/WcRwhFP51In/bbj3CUfQIDAQABAoIBAAgHbnaybip5CDuM\nK086FErnv29L1YVd3B8m5oIppddPLEb6lwLr3Id/zY/gsX+W+/HD8mMrk7keXT9f\nhK5f51TIPT4Z6UFjB0OpFmZn3zh26APqF7uy3zIxYe2uJD3y8VRFX06tfrzkGdUV\nZPe580K41wVyMw646NGFnzei0tBGaiX9vCdwVUmj+3ulJb6D5CGtGc4E5063toVG\nuxB1YSH6ORabJl7qidgkx7kf7xmuNuqcjz2urx0oLshfhVqRUb6m36AZO8Ho0jVf\nV+1mGY6SpfH+uQpC6/8JKJhDc9ks/xKXvN41uNtEti4hTVcYKnHmUdyb+zZsoA8+\n5wiQRAECgYEAu/NS6T+e7REpjt5nhyrp3XRPFFAJxr8cLPn7eiiFjnZ3p0uZBCBw\nW96AXVArmUFnSYAr+4oEfkpX81yJKEVw4+BAVLZN+Hub2cTa46a6kycZP55Fvry9\nWSGSGO+XQ5SS5bbv/SULhgkzrekp/KhAdGxs6Sb95Twi+y7fF