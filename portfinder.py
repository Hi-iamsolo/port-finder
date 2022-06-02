import requests as rq
print('............PORT FINDER...........')
ip=input('enter ip:')
print('1.http\n2.https')
pro=input('Choose protocol:\n')
print('Enter port range')
rang=input('From:')
rang2=input('To:')
	
if pro==str(1):
		for port in range(int(rang),int(rang2)):
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
			
			
			
			
	
		
								
	
	
	
