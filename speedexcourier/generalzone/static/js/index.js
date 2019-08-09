var images=["222.jpg","333.jpg","444.jpg"];
        var i=0;
        baseUrl="{%static 'images/'%}";
        function slide()
        {
        if(i==images.length)
        {
        i=0;
        }
        document.getElementById("slide").src=baseUrl+images[i];
        i++;
        window.setTimeout("slide()",2000);
        }