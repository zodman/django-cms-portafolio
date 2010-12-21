
function addLoadListener(fn)
{
	if (typeof window.addEventListener != 'undefined')
	{
		window.addEventListener('load', fn, false);
	}
	else if (typeof document.addEventListener != 'undefined')
	{
		document.addEventListener('load', fn, false);
	}
	else if (typeof window.attachEvent != 'undefined')
	{
		window.attachEvent('onload', fn);
	}
	else
	{
		return false;
	}
	
	return true;
};




function attachEventListener(target, eventType, functionRef, capture)
{
    if (typeof target.addEventListener != "undefined")
    {
        target.addEventListener(eventType, functionRef, capture);
    }
    else if (typeof target.attachEvent != "undefined")
    {
        target.attachEvent("on" + eventType, functionRef);
    }
    else
    {
        return false;
    }

    return true;
};