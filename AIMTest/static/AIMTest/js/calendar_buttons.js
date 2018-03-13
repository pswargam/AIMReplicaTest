 <script type="text/javascript">
        function displayplus() {
            var x = document.getElementsByClassName('fc-plus-icon');
            for(var a=0; a<x.length;a++){
                    x[a].style.display = "inline";
            }
         }
        function hideplus(){
            var x = document.getElementsByClassName('fc-plus-icon');
            for(var a=0; a<x.length; a++){
                if(x[a].style.display == "inline"){
                    x[a].style.display = "none";
                }
                else{
                    x[a].style.display = "inline";
                }
            }
        }
        function hideplusoncalendar(){
            var x = document.getElementsByClassName('fc-plus-icon');
            for(var a=0; a<x.length;a++){
                    x[a].style.display = "none";
            }
         }
        function showbuttons(){
            var x = document.getElementsByClassName('edit_tabs');
            for(var a=0; a<x.length;a++){
                    x[a].style.display = "inline";
            }
        }
        function hidebuttons(){
            var x = document.getElementsByClassName('edit_tabs');
            for(var a=0; a<x.length;a++){
                x[a].style.display = "none";
            }
        }
        function hide_edit_tabs_plus(){
            hideplusoncalendar();
            hidebuttons();
        }

        document.addEventListener('DOMContentLoaded', function() {
            hidebuttons();
        }, false);

    </script>
