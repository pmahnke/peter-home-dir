;
; ZONE FILE for vitucci.com
;
;
@               IN      SOA     baby.internal.network. peter.internal.network. (
                                20000921        ; Serial, today's date 
                                8H      	; Refresh, seconds
                                2H     		; Retry, seconds
                                1W      	; Expire, seconds
                                1D)     	; Minimum TTL, setconds
                        NS      baby		; name server
			MX	10 baby  	; Primary Mail Exchanger
;
vitucci.com.		A	192.168.1.45
www			A	192.168.1.45
ftp			A	192.168.1.45 
mail			A	192.168.1.45 
pop			A	192.168.1.45 
dev			A	192.168.1.46

