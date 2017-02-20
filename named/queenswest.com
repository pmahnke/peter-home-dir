;
; ZONE FILE for queenswest.com
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
queenswest.com.		A	192.168.1.70
www			A	192.168.1.70
ftp			A	192.168.1.70 
mail			A	192.168.1.70 
pop			A	192.168.1.70 
dev			A	192.168.1.71

