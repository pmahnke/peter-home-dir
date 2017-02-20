;
; ZONE FILE for digitalalliances.com
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
digitalalliances.com.		A	192.168.1.100
www			A	192.168.1.100
ftp			A	192.168.1.100 
mail			A	192.168.1.100 
pop			A	192.168.1.100 
dev			A	192.168.1.101

