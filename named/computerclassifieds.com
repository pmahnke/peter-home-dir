;
; ZONE FILE for computerclassifieds.com
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
computerclassifieds.com.		A	192.168.1.60
www			A	192.168.1.60
ftp			A	192.168.1.60 
mail			A	192.168.1.60 
pop			A	192.168.1.60 
dev			A	192.168.1.61

