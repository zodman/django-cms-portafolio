
checkBrowserWidth();

attachEventListener(window, "resize", checkBrowserWidth, false);




function checkBrowserWidth()
{
	var theWidth = getBrowserWidth();
	
	if (theWidth == 0)
	{
		var resolutionCookie = document.cookie.match(/(^|;)tmib_res_layout[^;]*(;|$)/);

		if (resolutionCookie != null)
		{
			setStylesheet(unescape(resolutionCookie[0].split("=")[1]));
		}
		
		addLoadListener(checkBrowserWidth);
		
		return false;
	}

	if (theWidth <= 320)
	{
		setStylesheet("320");
		document.cookie = "tmib_res_layout=" + escape("320");
	}
	
	
	else
	{
		setStylesheet("");
		document.cookie = "tmib_res_layout=";
	}
	
	return true;
};




function getBrowserWidth()
{
	if (window.innerWidth)
	{
		return window.innerWidth;
	}
	else if (document.documentElement && document.documentElement.clientWidth != 0)
	{
		return document.documentElement.clientWidth;
	}
	else if (document.body)
	{
		return document.body.clientWidth;
	}
	
	return 0;
};




function setStylesheet(styleTitle)
{
	var currTag;

	if (document.getElementsByTagName)
	{
		for (var i = 0; (currTag = document.getElementsByTagName("link")[i]); i++)
		{
			if (currTag.getAttribute("rel").indexOf("style") != -1 && currTag.getAttribute("title"))
			{
				currTag.disabled = true;

				if(currTag.getAttribute("title") == styleTitle)
				{
					currTag.disabled = false;
				}
			}
		}
	}
	
	return true;
};