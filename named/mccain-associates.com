;
; ZONE FILE for mccain-associates.com
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
mccain-associates.com.		A	192.168.1.105
www			A	192.168.1.105
ftp			A	192.168.1.105 
mail			A	192.168.1.105 
pop			A	192.168.1.105 
dev			A	192.168.1.106

