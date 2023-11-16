function loadNavbar(elementId) {
    var xhr = new XMLHttpRequest();
  
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        document.getElementById(elementId).innerHTML = xhr.responseText;
      }
    };
    xhr.open('GET', 'navbar.html', true);
    xhr.send();
  }
  
  loadNavbar('navbar-container');
  