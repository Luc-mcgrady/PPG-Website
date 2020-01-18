
function InjectHTML(file,target) {
  $(function() {  $(target).load(file);  }) //Jquery loading template from 
}

function LoadHeaderFooter(header,footer) {
  InjectHTML("header.html",header)
  InjectHTML("footer.html",footer)
}
//function() {}
