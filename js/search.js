function submitSearch()
{
	var objSearchForm = document.frmSearch;
	if (validSearch()) {
		mystrng = objSearchForm.txtSearch.value;
		mystrng = cleanupSearchKeywords(mystrng);
		openSearch('http://regionals4.gartner.com/7_search/Search2Frame.jsp?keywords='+ mystrng);
	}
}

function validSearch()
{
	var objSearchForm = document.frmSearch;
	var keywords = objSearchForm.txtSearch.value;

	if (keywords.match(/[A-Z]+/g) ||
	    keywords.match(/[a-z]+/g) ||
	    keywords.match(/[0-9]+/g))
	{
		return true;
	}

	if (keywords.match(/^ *$/g)) {
		alert('Please provide keywords for your search.');
		return false;
	}
	alert('Your search is too general.  Please provide keywords for your search.');
	return false;
}

function cleanupSearchKeywords(k)
{
	var keywords = k;
	if (keywords!=null) {
		keywords = keywords.replace(/\%/g,"%25");
		keywords = keywords.replace(/\"/g,"%22");
		keywords = keywords.replace(/\#/g,"%23");
		keywords = keywords.replace(/\&/g,"%26");
		keywords = keywords.replace(/\'/g,"%27");
		keywords = keywords.replace(/\+/g,"%2B");
		keywords = keywords.replace(/\,/g,"%2C");
		keywords = keywords.replace(/\./g,"%2E");
		keywords = keywords.replace(/\//g,"%2F");
		keywords = keywords.replace(/\:/g,"%3A");
		keywords = keywords.replace(/\;/g,"%3B");
		keywords = keywords.replace(/\</g,"%3C");
		keywords = keywords.replace(/\=/g,"%3D");
		keywords = keywords.replace(/\>/g,"%3E");
		keywords = keywords.replace(/\?/g,"%3F");
		keywords = keywords.replace(/\@/g,"%40");
		keywords = keywords.replace(/\[/g,"%5B");
		keywords = keywords.replace(/\]/g,"%5D");
		keywords = keywords.replace(/\^/g,"%5E");
		keywords = keywords.replace(/\{/g,"%7B");
		keywords = keywords.replace(/\|/g,"%7C");
		keywords = keywords.replace(/\}/g,"%7D");
		keywords = keywords.replace(/\~/g,"%7E");
		keywords = keywords.replace(/ /g,"+");

		for (x = 0; x < keywords.length; x++) {

			d = keywords.charCodeAt(x);

			if (d == 8216 || d == 8217 || d == 8220 || d == 8221) {
		   		if (x == 0) {
		   			if (d == 8216 || d == 8217) {
		   				keywords = "%27" + keywords.substring(1, keywords.length);
		   			} else {
		   				keywords = "%22" + keywords.substring(1, keywords.length);
		   			}
		   		} else if (x == keywords.length) {
		   			if (d == 8216 || d == 8217) {
		   				keywords = keywords.substring(0, x) + "%27";
		   			} else {
		   				keywords = keywords.substring(0, x) + "%22";
		   			}
		   		} else {
		   			if (d == 8216 || d == 8217) {
						keywords = keywords.substring(0, x) + "%27" + keywords.substring(x + 1, keywords.length);
					} else {
						keywords = keywords.substring(0, x) + "%22" + keywords.substring(x + 1, keywords.length);
					}
				}
			}
		}
	}

	return keywords

}


function openSearch(href)
{
	var newname= nameForWindow('search');
	newWin = window.open(href, newname,'width=750,height=540,scrollbars=yes,resizable=yes');
	newWin.focus();
	newWin.opener = self;
	return false;
}

function nameForWindow(suffix)
{
	var newname = eval('document.domain') + '_' + eval('suffix');
	return newname.replace(/\./g, '_');
}

function storeNewWin( newWin )
{
	winCTR = winCTR + 1 ;
	if (winCTR > 40) {
		alert ("No more windows allowed");
		return false;
	} else  {
		childWindow[winCTR] = newWin ;
	}
}


/* open research window */
function openResult(href) {
   window.open(href,'_blank','height=569,width=798,scrollbars=yes,menubar=yes,resizable=yes,status=yes');
}