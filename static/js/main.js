$(function(){
    $('.carousel').carousel({
        interval: 10000
      })

        $('.openClose').click(function() {
            console.log('clicked')
            var sidebarWidth = document.getElementById("admin-sidebar").offsetWidth;
            console.log(sidebarWidth);
            if (sidebarWidth == 0) {
                document.getElementById("admin-sidebar").style.width = '160px';
                document.getElementById("main").style.margin = '0 160px 0'
            } else {
                document.getElementById("admin-sidebar").style.width = '0';
                document.getElementById("main").style.margin = '0'
            }

        } )

})