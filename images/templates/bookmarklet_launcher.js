(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else{
        document.body.appendChild(document.createElement('script')).src='http://127.0.0.1:8000/static/js/bookmarklet.js?r='+math.floor(math.random()*99999999999999999999)
    }
    }
)();
