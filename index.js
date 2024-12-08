
var options = {
    urlForSize: function(filename, size) {
        return '/img/' + size + '/' + filename;
      },
      spaceBetweenImages: 2,
      getMinAspectRatio: function(lastWindowWidth) {
        if (lastWindowWidth <= 1200)  // Phones
          return 2;
        else
          return 5;
      },
      getImageSize: function(lastWindowWidth) {
      if (lastWindowWidth <= 1200)  // Phones
          return 250;
        else
          return 500;
      },
};

  // simple sync request to get the legend
  r = new XMLHttpRequest();
  r.open("GET", "/legend.json", false);
  r.send(null);
  var imageData = JSON.parse(r.responseText)
  var pig = new Pig(imageData, options).enable();

  $(".pig-figure").on( "click", function(e) {
    console.log( "Handler for `click` called.", e);
    const imgPath = e.currentTarget.childNodes[0].currentSrc;
    console.log(imgPath);
    const filePathParts = imgPath.split("img/")[1].split("/");
    const fileName = filePathParts[filePathParts.length - 1];
    console.log(fileName);
    const enlargedImagePath = "/img/500/" + fileName;
    console.log(enlargedImagePath);
    // <a href="#" rel="modal:close">Close</a>
    $('<div id="imagemodal" class="modal"><img class="modalimg" src="' + enlargedImagePath + '" /></div>').modal();

  } );