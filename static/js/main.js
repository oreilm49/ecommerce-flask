$(function(){
    $('.carousel').carousel({
        interval: 10000
      })

        $('.openClose').click(function() {
            var sidebarWidth = document.getElementById("admin-sidebar").offsetWidth;
            console.log(sidebarWidth);
            if (sidebarWidth == 0) {
                document.getElementById("admin-sidebar").style.width = '250px';
                document.getElementById("main").style.margin = '0 250px 0'
            } else {
                document.getElementById("admin-sidebar").style.width = '0';
                document.getElementById("main").style.margin = '0'
            }

        } )
        $('.accordion_btn').click(function() {
            card_id = $( this ).attr("data-target");
            element = document.getElementById(card_id)
            if (element.classList.length > 1) {
                element.classList.remove('show')
            } else {
                element.classList.add('show')
            }
        });
})