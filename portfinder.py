import requests as rq

ip=input('enter ip:')
print('1.http\n2.https')
pro=input('Choose protocol:')
	
if pro==str(1):
		for port in range(7999,8090):
			try:
				rq.get('http://'+ip+':'+str(port))
				print('http://'+ip+':'+str(port))
			except:
					
					r=6
					
					
else:
				for port in range(8000,8090):
					try:
						rq.get('https://'+ip+':'+str(port))
						print('https://'+ip+':'+str(port))
					except:
						r=6
			
			
			
			
	
		
								
	
	
	

	
	

